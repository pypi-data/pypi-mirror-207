from dataclasses import dataclass
import random
from typing import List

from foru.core.enum import Mode


@dataclass
class Song:
    source: str = ''
    sid: str = ''
    title: str = ''
    artist: str = ''
    artist_id: str = ''
    album: str = ''
    album_id: str = ''
    duration: float = 0.0
    url: str = ''
    lyric: str = ''

    @property
    def fullname(self):
        return f'{self.title} - {self.artist}'

    def __hash__(self):
        return hash(self.source + self.sid)


@dataclass
class SongInPlaylist(Song):
    plid: str = ''


@dataclass
class Playlist:
    id: str = ''
    name: str = '新建歌单'
    detail: str = ''
    number: int = 0
    duration: float = 0.0

    def __hash__(self):
        return hash(self.id)


@dataclass
class Album:
    name: str
    id: str
    date: str
    artist: str
    artist_id: str
    number: int
    duration: float

    def __hash__(self):
        return hash(self.id)


class Playinglist:

    def __init__(self, mode=Mode.NORMAL, curidx=-1):
        self._mode: Mode = mode
        self._curidx: int = curidx
        self._songs: List[Song] = []
        self._shuffle: List[int] = []

    def next(self):
        if self._mode == Mode.NORMAL:
            if self._curidx < len(self._songs) - 1:
                self._curidx += 1
            else:
                return -1
        elif self._mode == Mode.REPEAT_ALL:
            self._curidx = (self._curidx + 1) % len(self._songs)
        elif self._mode == Mode.SHUFFLE:
            self._shuffle.append(self._curidx)
            self._curidx = random.randint(0, len(self._songs) - 1)
            # while len(self._shuffle_queue) > 0 and self._curidx == self._shuffle_queue[-1]:
            #     self._curidx = random.randint(0, len(self._playinglist) - 1)
        return self._curidx

    def previous(self):
        if self._mode == Mode.NORMAL:
            if self._curidx > 0:
                self._curidx -= 1
            else:
                return -1
        elif self._mode == Mode.REPEAT_ALL:
            self._curidx = (self._curidx + len(self._songs) - 1) % len(self._songs)
        else:
            if self._shuffle:
                self._curidx = self._shuffle.pop()
            else:
                return -1
        return 0

    def remove(self, idx):
        if idx == self._curidx:
            return -1
        if 0 <= idx < len(self._songs):
            self._songs.pop(idx)
            if idx < self._curidx:
                self._curidx -= 1
            return 0
        return -1

    def clear(self):
        self._songs.clear()
        self._curidx = -1

    def stop(self):
        self._curidx = -1

    @property
    def current(self):
        return self._curidx

    @current.setter
    def current(self, value):
        self._curidx = value

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value

    @property
    def songs(self):
        return self._songs

    def add(self, song):
        try:
            if song not in self._songs:
                self._songs.append(song)
        except Exception as e:
            print(e)

    def adds(self, songs: List[Song]):
        for song in songs:
            self.add(song)

    def removes(self, idxes: List[int]):
        for idx in idxes:
            self.remove(idx)

    def __repr__(self) -> str:
        return f'Playing songs: {len(self._songs)}'
