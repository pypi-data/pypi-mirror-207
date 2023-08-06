import asyncio
import logging

from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout

from foru.core import LPlayer
from foru.utils import aio

logger = logging.getLogger('foru.ui.info')


class Info(QWidget):
    def __init__(self, app):
        super().__init__()
        self.loop = asyncio.get_event_loop()
        self._app = app
        self._player: LPlayer = app.player

        self.album_img = QLabel()
        self.album_img.setObjectName('info_album_image')
        self.album_img.setFixedSize(64, 64)
        self.title = QLabel('')
        self.title.setObjectName('info_title')
        self.artist = QLabel('')
        self.artist.setObjectName('info_artist')
        self.album = QLabel('')
        self.album.setObjectName('info_album')

        vb = QVBoxLayout()
        vb.addWidget(self.title)
        vb.addWidget(self.album)
        vb.addWidget(self.artist)
        vb.setSpacing(2)

        hb = QHBoxLayout()
        hb.addWidget(self.album_img)
        hb.addLayout(vb)

        self.setLayout(hb)
        self._player.signal.start_file.connect(self._update_info)

        self._update_info()

    def _update_info(self):
        if self._player.current:
            self.title.setText(self._player.current.title)
            self.artist.setText(self._player.current.artist)
            self.album.setText(self._player.current.album)
            aio.create(self.get_album_image(self._player.current.album_id))

    async def get_album_image(self, aid):
        img = await self._app.default_provider.get_album_image(aid, 64)
        image = QPixmap(64, 64)
        if img:
            image.loadFromData(QByteArray(img))
        else:
            image.load(':/icons/default_album.png')
        self.album_img.setPixmap(image)
