import logging

from PySide6.QtCore import QByteArray
from PySide6.QtGui import Qt, QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QFormLayout

from ui.models import AlbumSongsModel
from ui.songlist import SongListWidget
from utils import aio
from utils.show import show_duration

logger = logging.getLogger('foru.ui.playlist')


class AlbumSongs(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self._album_id = None

        self.model = AlbumSongsModel(app)
        self.playlist_songs_ui = SongListWidget(app, self.model, self)

        self.album_image = QLabel()
        self.album_image.setObjectName('album_image')

        self.album_name = QLabel()
        self.album_name.setObjectName('album_name')
        self.artist_name = QLabel()
        self.artist_name.setObjectName('album_artist')
        self.album_year = QLabel()
        self.album_year.setObjectName('album_year')

        llayout = QVBoxLayout()
        llayout.addWidget(self.album_name)
        llayout.addWidget(self.artist_name)
        llayout.addWidget(self.album_year)

        left_layout = QHBoxLayout()
        left_layout.addWidget(self.album_image)
        left_layout.addLayout(llayout)
        left_layout.setSpacing(10)

        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        info_layout = QFormLayout()
        self.songs_number = QLabel()
        self.duration = QLabel()
        info_layout.addRow('曲目： ', self.songs_number)
        info_layout.addRow('时长： ', self.duration)
        info_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        info_w = QWidget()
        info_w.setLayout(info_layout)

        up_layout = QHBoxLayout()
        up_layout.addWidget(left_widget, 0, Qt.AlignmentFlag.AlignLeft)
        up_layout.addWidget(info_w, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        up_w = QWidget()
        up_w.setLayout(up_layout)
        up_w.setObjectName('playlist_header')

        layout = QVBoxLayout()
        layout.addWidget(up_w)
        layout.addWidget(self.playlist_songs_ui)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        self._album_id = value
        self.model.album_id = value
        self.update_ui()

    def update_ui(self):
        aio.create(self._update_ui())

    async def _update_ui(self):
        album = await self._app.default_provider.get_album_info(self._album_id)
        logger.debug(f'Show album songs: {album}')
        self.album_name.setText(album.name)
        self.album_year.setText(str(album.date))
        self.artist_name.setText(album.artist)
        self.duration.setText(show_duration(album.duration))
        self.songs_number.setText(str(album.number))
        img = await self._app.default_provider.get_album_image(self._album_id, 128)
        image = QPixmap()
        if img:
            image.loadFromData(QByteArray(img))
        else:
            image.load('../resource/default_album.png')
        self.album_image.setPixmap(image)
