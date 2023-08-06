import logging
from configparser import ConfigParser

from aiohttp import web

from foru.app.base import BaseAPP
from foru.core.enum import Mode
from foru.utils.show import list_songs, list_providers, show_duration

logger = logging.getLogger('foru.app.server')


class Server:
    def __init__(self, _app, cp):
        self.app: BaseAPP = _app
        self.cp: ConfigParser = cp

    async def _status(self, request: web.Request):
        return web.Response(
            text=f'mode: {self.app.player.mode.name}\n'
                 f'song: {self.app.player.current.fullname if self.app.player.playinglist.current != -1 else ""}\n'
                 f'postition: {self.app.player.position}\n'
                 f'status: {self.app.player.status.name}\n'
                 f'duration: {show_duration(self.app.player.duration)}\n'
                 f'lyric: {self.app.player.lyric}\n'
                 f'provider: {self.app.default_provider}')

    async def _playinglist(self, request: web.Request):
        if len(self.app.player.playinglist.songs) == 0:
            return web.Response(text=list_songs([]))
        return web.Response(text=list_songs(self.app.player.playinglist.songs))

    async def _play(self, request):
        idx = request.match_info['index']
        res = self.app.player.play(int(idx))
        return web.Response(text='', status=200 if res == 0 else 401)

    async def _stop(self, request):
        self.app.player.stop()
        return web.Response(text='')

    async def _next(self, request):
        self.app.player.next()
        return web.Response(text='')

    async def _previous(self, request):
        self.app.player.previous()
        return web.Response(text='')

    async def _pause(self, request):
        self.app.player.pause()
        return web.Response(text='')

    async def _resume(self, request):
        self.app.player.resume()
        return web.Response(text='')

    async def _add(self, request):
        idx = int(request.match_info['index'])
        if 0 <= idx < len(self.app.default_provider.result):
            res = self.app.player.playinglist.add(self.app.default_provider.result[idx])
            return web.Response(text=res)
        return web.Response(text='Invalid index', status=400)

    async def _remove(self, request):
        idx = request.match_info['index']
        res = self.app.player.playinglist.remove(int(idx))
        return web.Response(text='', status=200 if res == 0 else 400)

    async def _lyric(self, request):
        return web.Response(text=self.app.player.lyric)

    async def _search_song(self, request):
        kw = request.match_info['kw']
        if self.app.default_provider:
            song = await self.app.default_provider.search_songs(kw)
            return web.Response(text=list_songs(self.app.default_provider.result))
        else:
            return web.Response(text='No provider', status=404)

    async def _providers(self, request):
        return web.Response(text=list_providers(self.app.providers, self.app.default_provider))

    async def _select(self, request):
        kw = request.match_info['kw']
        self.app.select(int(kw))
        return web.Response(text='')

    async def _mode(self, request):
        kw = request.match_info['kw']
        self.app.player.mode = Mode(int(kw))
        return web.Response(text='')

    def setup_route(self, app):
        app.router.add_get('/status', self._status)
        app.router.add_get('/playinglist', self._playinglist)
        app.router.add_get('/play/{index}', self._play)
        app.router.add_get('/stop', self._stop)
        app.router.add_get('/previous', self._previous)
        app.router.add_get('/next', self._next)
        app.router.add_get('/pause', self._pause)
        app.router.add_get('/resume', self._resume)
        app.router.add_get('/add/{index}', self._add)
        app.router.add_get('/remove/{index}', self._remove)
        app.router.add_get('/searchSong/{kw}', self._search_song)
        app.router.add_get('/lyric', self._lyric)
        app.router.add_get('/providers', self._providers)
        app.router.add_get('/select/{kw}', self._select)
        app.router.add_get('/mode/{kw}', self._mode)

    async def start_server(self):
        _app = web.Application()
        self.setup_route(_app)

        server = self.cp['foru'].get('server')
        port = self.cp['foru'].getint('port')

        runner = web.AppRunner(_app, handle_signals=True)
        await runner.setup()
        logger.info(f'Starting server: {server}:{port}')
        site = web.TCPSite(runner, server, port)
        await site.start()
