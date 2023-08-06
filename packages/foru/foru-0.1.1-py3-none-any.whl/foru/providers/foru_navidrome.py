import json
import logging
from typing import List

import aiohttp

from foru.core.models import Song, Playlist, SongInPlaylist, Album
from providers.base import BaseProvider
from utils.mode import singleton

logger = logging.getLogger('foru.providers.navidrome')


@singleton
class NaviProvider(BaseProvider):

    def __init__(self):
        super().__init__()
        self._server: str = 'localhost'
        self._port: int = 4533
        self._username: str = 'username'
        self._password: str = 'password'
        self._name: str = 'navidrome'
        self._result: List[Song] = []

        # for subsonic
        self._salt = ''
        self._stoken = ''

        self.base_url = f'http://{self._server}:{self._port}'
        self.headers = {'Referer': f'{self.base_url}/app'}

        self._status = False

    async def init(self, cp):
        try:
            if self._status:
                return
            navi = cp['navidrome']
            self._username = navi['username']
            self._password = navi['password']
            self._server = navi.get('server', 'localhost')
            self._port = navi.getint('port', 4533)
            async with aiohttp.ClientSession() as session:
                async with session.post(f'http://{self._server}:{self._port}/auth/login', headers=self.headers,
                                        data=json.dumps(
                                            {'username': self._username, 'password': self._password})) as res:
                    if res.ok:
                        auth = await res.json()
                        token = auth['token']
                        self._salt = auth['subsonicSalt']
                        self._stoken = auth['subsonicToken']
                        self.headers['x-nd-authorization'] = f'Bearer {token}'
                        self._status = True
                        logger.info(f'Provider {self._name} login successfully.')
                    else:
                        logger.debug(res.text)
                        self._status = False
                        logger.warning(f'Source {self.source} login failed')
        except Exception as e:
            logger.exception(e)

    def from_id_to_url(self, value):
        return f"http://{self._server}:{self._port}/rest/" \
               f"stream?u={self._username}&t={self._stoken}&s={self._salt}&f=json&v=1.8.0&c=foru&id={value}"

    async def search_songs(self, query):
        url = f'{self.base_url}/api/song?_order=ASC&_sort=title&_start=0'
        logger.debug(f'Search song url: {url}')
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params={'title': query}, headers=self.headers) as res:
                songs = []
                result = await res.json()
                if result:
                    for s in result:
                        songs.append(Song(self.name, s['id'], s['title'], s['artist'], s['artistId'],
                                          s['album'], s['albumId'], s['duration'], self.from_id_to_url(s['id'])))
                        if 'lyrics' in s:
                            songs[-1].lyric = s['lyrics']
                    self._result.clear()
                    self._result.extend(songs)
                logger.debug(f'Search song result: {songs}')
                return songs

    async def get_playlists(self):
        logger.debug('Get playlists...')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{self._server}:{self._port}/api/playlist', headers=self.headers) as resp:
                a = await resp.json()
                self._playlists.clear()
                for pl in a:
                    self._playlists.append(Playlist(pl['id'], pl['name'], pl['comment'],
                                                    pl['songCount'], pl['duration']))
                logger.debug(f'Get all playlists: {self._playlists}')

    async def add_playlist(self, name):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'http://{self._server}:{self._port}/api/playlist',
                                    data=json.dumps({'name': name, 'public': True}),
                                    headers=self.headers) as resp:
                a = await resp.json()
                logger.debug(f'Add playlist result : {a}')
                return resp.ok

    async def put_playlist(self, pl: Playlist):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://{self._server}:{self._port}/api/playlist/{pl.id}',
                                   headers=self.headers) as resp:
                new_pl = await resp.json()
                new_pl['name'] = pl.name
            async with session.put(f'http://{self._server}:{self._port}/api/playlist/{pl.id}',
                                   data=json.dumps(new_pl),
                                   headers=self.headers) as resp:
                logger.debug(f'Modify playlist result: {resp.ok}')
                return resp.ok

    async def delete_playlist(self, pid):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f'http://{self._server}:{self._port}/api/playlist/{pid}',
                                      headers=self.headers) as resp:
                logger.debug(f'Delete playlist result: {resp.ok}')
                return resp.ok

    async def get_album_image(self, aid, size):
        logger.debug("Get album image...")
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/rest/getCoverArt',
                                   params={
                                       'u': self._username,
                                       't': self._stoken,
                                       's': self._salt,
                                       'f': 'json',
                                       'v': '1.8.0',
                                       'c': 'NavidromeUI',
                                       'id': f'al-{aid}',
                                       'size': size
                                   }) as resp:
                logger.debug(f'Get album status: {resp.ok}')
                if resp.ok:
                    return await resp.read()
                return None

    async def add_to_playlist(self, sids: List[str], pid: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.base_url}/api/playlist/{pid}/tracks',
                                    data=json.dumps({'ids': sids}),
                                    headers=self.headers) as resp:
                return resp.ok

    async def get_playlist_songs(self, pid):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/api/playlist/{pid}/tracks', headers=self.headers) as res:
                songs = []
                result = await res.json()
                if result:
                    for s in result:
                        songs.append(SongInPlaylist(self.name, s['mediaFileId'], s['title'], s['artist'],
                                                    s['artistId'], s['album'], s['albumId'], s['duration'],
                                                    self.from_id_to_url(s['mediaFileId']), '', s['id']))
                        if 'lyrics' in s:
                            songs[-1].lyric = s['lyrics']
                logger.debug(f'Get playlist {pid} songs: {songs}')
                return songs

    async def delete_from_playlist(self, plids, pid):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f'{self.base_url}/api/playlist/{pid}/tracks', params={'id': plids},
                                      headers=self.headers) as res:
                return res.ok

    async def get_albums(self, kw=''):
        logger.debug(f'Start search albums with kw: {kw}')
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/api/album', params={'name': kw}, headers=self.headers) as res:
                res = await res.json()
                albums = []
                for al in res:
                    albums.append(Album(al['name'], al['id'], al['minYear'], al['artist'],
                                        al['artistId'], al['songCount'], al['duration']))
                logger.debug(f'Search album result: {albums}')
                return albums

    async def get_album_info(self, aid):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/api/album/{aid}',
                                   headers=self.headers) as res:
                res = await res.json()
                return Album(res['name'], res['id'], res['minYear'], res['artist'],
                             res['artistId'], res['songCount'], res['duration'])

    async def get_album_songs(self, aid) -> List[Song]:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}/api/song', params={'album_id': aid}, headers=self.headers) as res:
                songs = []
                result = await res.json()
                if result:
                    for s in result:
                        songs.append(Song(self.name, s['id'], s['title'], s['artist'], s['artistId'],
                                          s['album'], s['albumId'], s['duration'], self.from_id_to_url(s['id'])))
                        if 'lyrics' in s:
                            songs[-1].lyric = s['lyrics']
                logger.debug(f'Get album songs: {songs}')
                return songs


provider = NaviProvider()
