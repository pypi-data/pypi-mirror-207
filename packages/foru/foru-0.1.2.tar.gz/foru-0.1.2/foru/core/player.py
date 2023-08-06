import logging
import os.path
import pickle
from typing import Union

from PySide6.QtCore import QObject, Signal
from mpv import MPV, MpvEventID

from foru.core.enum import Status
from foru.config import global_settings
from foru.core.lyric import parse_lyric
from foru.core.models import Playinglist, Song
from foru.utils.mode import singleton

logger = logging.getLogger('foru.core.player')


class PlayerSignal(QObject):
    position_changed = Signal()
    start_file = Signal()
    volume_changed = Signal()
    mode_changed = Signal()
    status_changed = Signal()


@singleton
class LPlayer:
    def __init__(self, position=0, status=Status.STOP, volume=100, playinglist: Playinglist = None):
        self._position = position
        self._status: Status = status
        self.signal = PlayerSignal()

        self._volume: int = volume

        self._playinglist: Playinglist = playinglist if playinglist else Playinglist()

        self._lyric_map = {}
        self._lyric = ''
        self.mpv = MPV()

        self.mpv.observe_property(
            'time-pos',
            lambda name, time_pos: self._on_position_changed(time_pos)
        )

        self.mpv.register_event_callback(self._on_event)

        self.load_state()

    def play(self, idx):
        logger.debug(f'prepare to play {idx}')
        if not self._playinglist.songs or (idx < 0 or idx >= len(self._playinglist.songs)):
            return -1
        else:
            # play正在播放的歌曲无动作
            if self._status == Status.PLAYING and self._playinglist.current == idx:
                return 0
            else:
                self._playinglist.current = idx
                self.mpv.play(self._playinglist.songs[self._playinglist.current].url)
                self.mpv.pause = False
                self._status = Status.PLAYING
                self.signal.status_changed.emit()
                return 0

    def resume(self):
        if self._status == Status.PAUSE:
            self.mpv.command('cycle', 'pause')
            self._status = Status.PLAYING
            self.signal.status_changed.emit()
            return 0
        # 启动时恢复了上次放状态
        elif self._status == Status.STOP and self._playinglist.current != -1:
            self.mpv.loadfile(self.current.url, start=f'+{self._position}')
            return 0
        return -1

    def pause(self):
        if self._status == Status.PLAYING:
            self.mpv.command('cycle', 'pause')
            self._status = Status.PAUSE
            self.signal.status_changed.emit()
        return 0

    def stop(self):
        self._status = Status.STOP
        self.signal.status_changed.emit()
        self._save_state()
        self._playinglist.stop()
        self._position = 0
        self._lyric = ''
        self._lyric_map.clear()
        self.mpv.stop()
        return 0

    def next(self):
        r = self._playinglist.next()
        logger.debug(f'next idx: {r}')
        if r != -1:
            self.mpv.play(self._playinglist.songs[self._playinglist.current].url)
            return 0
        return -1

    def previous(self):
        r = self._playinglist.previous()
        if r != -1:
            self.mpv.play(self._playinglist.songs[self._playinglist.current].url)
            return 0
        return -1

    @property
    def position(self):
        return self._position

    def seek(self, value):
        if self._playinglist.current != -1:
            if self._status == Status.STOP:
                self.mpv.loadfile(self.current.url, start=f'+{value}')
            else:
                self.mpv.seek(value, reference='absolute')

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self.mpv.volume = value
        self._volume = value
        self.signal.volume_changed.emit()

    @property
    def status(self):
        return self._status

    @property
    def mode(self):
        return self._playinglist.mode

    @mode.setter
    def mode(self, value):
        self._playinglist.mode = value
        self.signal.mode_changed.emit()

    @property
    def duration(self):
        if self._playinglist.current != -1:
            return self._playinglist.songs[self._playinglist.current].duration
        return 0

    @property
    def current(self) -> Union[Song, None]:
        if self._playinglist.current != -1:
            return self._playinglist.songs[self._playinglist.current]
        return None

    @property
    def playinglist(self) -> Playinglist:
        return self._playinglist

    @property
    def lyric(self):
        return self._lyric

    def _on_position_changed(self, position):
        self._position = position
        self.signal.position_changed.emit()
        if position and self._lyric_map:
            k = int(position * 1000)
            keys = sorted(list(self._lyric_map.keys()))
            i = 0
            while i < len(keys) and keys[i] < k:
                i += 1
            self._lyric = self._lyric_map[keys[i - 1]]

    def _on_event(self, event):
        try:
            eid = event.event_id.value
            if eid == MpvEventID.END_FILE:
                logger.debug(f'End file event, reason {event.data.reason}')
                if event.data.reason == 0:
                    # 有下一首则播放
                    a = self._playinglist.next()
                    self.mpv.play(self._playinglist.songs[self._playinglist.current].url)
                    if a == -1:
                        self.stop()
            elif eid == MpvEventID.START_FILE:
                logger.debug('Start file event')
                self.signal.start_file.emit()
                self._status = Status.PLAYING
                self.signal.status_changed.emit()
                if self.current.lyric:
                    self._lyric_map = parse_lyric(self.current.lyric)
        except Exception as e:
            logger.exception(e)

    def _save_state(self):
        logger.info('Save state')
        state = {'_position': self._position,
                 '_playinglist': self._playinglist,
                 '_volume': self._volume}
        home = os.path.expanduser('~')
        state_file = os.path.join(home, global_settings.config_dir, global_settings.state_file)
        try:
            with open(state_file, 'wb') as f:
                pickle.dump(state, f)
        except Exception as e:
            logger.exception(e)

    def load_state(self):
        home = os.path.expanduser('~')
        state_file = os.path.join(home, global_settings.config_dir, global_settings.state_file)
        if os.path.exists(state_file):
            with open(state_file, 'rb') as f:
                logger.info('Load state')
                state = pickle.load(f)
                self._position = state['_position']
                self.volume = state['_volume']
                self._playinglist = state['_playinglist']
                logger.debug(self._playinglist)
