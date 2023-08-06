from enum import IntEnum


class Status(IntEnum):
    STOP = 0
    PAUSE = 1
    PLAYING = 2


class Mode(IntEnum):
    NORMAL = 0
    REPEAT_ALL = 1
    REPEAT_ONE = 2
    SHUFFLE = 3


class SongIndex(IntEnum):
    title = 1
    artist = 2
    album = 3
    duration = 4
