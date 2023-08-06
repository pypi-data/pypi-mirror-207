import logging

import PySide6.QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget, QPushButton

from foru.ui.album import AlbumSongs
from foru.ui.playlist import PlaylistSongs
from foru.ui.searchtab import SearchTab

logger = logging.getLogger('foru.ui.content')


class MainContent(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.stack_back_idxs = []
        self.stack_forward_idxs = []

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText('搜索歌曲')
        self.search_bar.setMinimumWidth(300)
        search = QAction(QIcon(':/icons/search.svg'), 'search', self)
        search.triggered.connect(self.show_search)
        self.search_bar.setClearButtonEnabled(True)
        self.search_bar.addAction(search, QLineEdit.ActionPosition.TrailingPosition)
        self.search_bar.returnPressed.connect(self.show_search)

        self.lyric = QLabel()
        self.lyric.setObjectName('top_lyric')
        self._app.player.signal.position_changed.connect(lambda: self.lyric.setText(self._app.player.lyric))

        self.back = QPushButton()
        self.back.setIcon(QIcon(':/icons/angle_left.png'))
        self.back.setProperty('class', 'icon_button')

        self.forward = QPushButton()
        self.forward.setIcon(QIcon(':/icons/angle_right.png'))
        self.forward.setProperty('class', 'icon_button')

        navi_layout = QHBoxLayout()
        navi_layout.addWidget(self.back)
        navi_layout.addWidget(self.forward)
        navi_layout.setSpacing(0)
        navi_layout.setContentsMargins(0, 0, 0, 0)
        navi_w = QWidget()
        navi_w.setLayout(navi_layout)

        up_layout = QHBoxLayout()
        up_layout.addWidget(navi_w, 0, Qt.AlignmentFlag.AlignLeft)
        up_layout.addWidget(self.search_bar, 0, Qt.AlignmentFlag.AlignCenter)
        up_layout.addWidget(self.lyric, 0, Qt.AlignmentFlag.AlignRight)

        header = QWidget()
        header.setProperty('class', 'header')
        header.setLayout(up_layout)

        self.search_tab = SearchTab(app, self)
        self.playlist_song = PlaylistSongs(app, self)
        self.album_song = AlbumSongs(app, self)

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.search_tab)
        self.stack.addWidget(self.playlist_song)
        self.stack.addWidget(self.album_song)

        self._app.signal.show_playlist.connect(self.show_playlist)
        self._app.signal.show_album.connect(self.show_album)

        self.back.clicked.connect(self.stack_back)
        self.forward.clicked.connect(self.stack_forward)

        layout = QVBoxLayout()
        layout.addWidget(header)
        layout.addWidget(self.stack)
        layout.setSpacing(4)
        layout.setContentsMargins(2, 0, 2, 2)
        self.setLayout(layout)

    def stack_back(self):
        if self.stack_back_idxs:
            self.stack_forward_idxs.append(self.stack.currentIndex())
            idx = self.stack_back_idxs.pop()
            self.stack.setCurrentIndex(idx)

    def stack_forward(self):
        if self.stack_forward_idxs:
            self.stack_back_idxs.append(self.stack.currentIndex())
            idx = self.stack_forward_idxs.pop()
            self.stack.setCurrentIndex(idx)

    def show_search(self):
        if self.stack.currentIndex() != 0:
            self.stack_back_idxs.append(self.stack.currentIndex())
            self.stack_forward_idxs.clear()
        self.stack.setCurrentWidget(self.search_tab)
        self.search_tab.search(self.search_bar.text())

    def show_playlist(self, pl):
        if self.stack.currentIndex() != 1:
            self.stack_back_idxs.append(self.stack.currentIndex())
            self.stack_forward_idxs.clear()
        self.playlist_song.playlist = pl
        self.stack.setCurrentWidget(self.playlist_song)

    def show_album(self, aid):
        if self.stack.currentIndex() != 2:
            self.stack_back_idxs.append(self.stack.currentIndex())
            self.stack_forward_idxs.clear()
        self.album_song.album_id = aid
        self.stack.setCurrentWidget(self.album_song)

    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.XButton1:
            self.stack_back()
        elif event.button() == Qt.MouseButton.XButton2:
            self.stack_forward()
        else:
            super().mousePressEvent(event)
