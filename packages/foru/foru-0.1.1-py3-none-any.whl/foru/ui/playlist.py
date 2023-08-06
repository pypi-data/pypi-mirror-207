import logging
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFormLayout, QMessageBox

from ui.models import PlaylistSongsModel
from ui.songlist import SongListWidget
from utils import aio
from utils.show import show_duration

logger = logging.getLogger('foru.ui.playlist')


class PlaylistSongsWidget(SongListWidget):
    def __init__(self, app, model, *args, **kwargs):
        super().__init__(app, model, *args, **kwargs)

        delete = self.pop_menu.addAction(QIcon(':icons/close.png'), '从歌单中删除')
        delete.triggered.connect(self.delete_from_playlist)

    def delete_from_playlist(self):
        song_ids = list(set([self._model.songs[i.row()].plid for i in self.content_list.selectedIndexes()]))
        mb = QMessageBox(self)
        mb.setText('确认删除')
        mb.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        mb.setButtonText(QMessageBox.StandardButton.Yes, '确认')
        mb.setButtonText(QMessageBox.StandardButton.Cancel, '取消')
        ret = mb.exec()
        if ret == QMessageBox.StandardButton.Yes:
            aio.create(self._delete_from_playlist(song_ids, self._model.pid))
        mb.close()

    async def _delete_from_playlist(self, plid, pid):
        a = await self._app.default_provider.delete_from_playlist(plid, pid)
        if a:
            await self._model.get_songs()
            await self._app.default_provider.get_playlists()
            self.parent().playlist = self.parent().index


class PlaylistSongs(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self._index = -1
        self._playlist = None

        self.model = PlaylistSongsModel(app)
        self.playlist_songs_ui = PlaylistSongsWidget(app, self.model, self)

        self.playlist_name = QLabel()
        self.playlist_name.setObjectName('playlist_name')
        self.detail = QLabel()
        self.detail.setObjectName('playlist_detail')

        info_layout = QFormLayout()
        self.songs_number = QLabel()
        self.duration = QLabel()
        info_layout.addRow('曲目： ', self.songs_number)
        info_layout.addRow('时长： ', self.duration)
        info_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        info_w = QWidget()
        info_w.setLayout(info_layout)

        up_layout = QHBoxLayout()
        up_layout.addWidget(self.playlist_name, 0, Qt.AlignmentFlag.AlignLeft)
        up_layout.addWidget(self.detail)
        up_layout.addWidget(info_w, 0, Qt.AlignmentFlag.AlignRight)
        up_w = QWidget()
        up_w.setLayout(up_layout)
        up_w.setObjectName('playlist_header')

        layout = QVBoxLayout()
        layout.addWidget(up_w)
        layout.addWidget(self.playlist_songs_ui)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    @property
    def playlist(self):
        return self._playlist

    @playlist.setter
    def playlist(self, value):
        self.playlist_songs_ui.content_list.clearSelection()
        self._index = value
        self._playlist = self._app.default_provider.playlists[value]
        self.model.pid = self._playlist.id
        self.playlist_name.setText(self._playlist.name)
        self.detail.setText(self._playlist.detail)
        self.songs_number.setText(str(self._playlist.number))
        self.duration.setText(show_duration(self._playlist.duration))

    @property
    def index(self):
        return self._index
