import logging
from typing import List

from PySide6.QtCore import QPoint
from PySide6.QtGui import Qt, QIcon, QCursor
from PySide6.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView, QVBoxLayout, QMenu, QInputDialog

from utils import aio

logger = logging.getLogger('foru.ui.songlist')


class SongListWidget(QWidget):
    def __init__(self, app, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self._model = model
        self.menu_idx = -1

        self.content_list = QTableView()

        # set headers
        self.content_list.setShowGrid(False)
        self.content_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.content_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        header = self.content_list.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        header.setStretchLastSection(True)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.content_list.verticalHeader().hide()

        layout = QVBoxLayout()
        layout.addWidget(self.content_list)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

        self.content_list.setModel(self._model)
        self.content_list.doubleClicked.connect(lambda x: self.play(x.row()))

        self.content_list.setColumnWidth(0, 40)
        self.content_list.setColumnWidth(1, 240)
        self.content_list.setColumnWidth(2, 240)
        self.content_list.setColumnWidth(3, 240)
        self.content_list.setColumnWidth(4, 50)

        self.content_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.content_list.customContextMenuRequested[QPoint].connect(lambda p: self.right_menu(p))

        self.pop_menu = QMenu()
        add_to = self.pop_menu.addAction(QIcon(':icons/folder_plus.png'), '添加到歌单')
        add_to.triggered.connect(self.add_ui)
        go_album = self.pop_menu.addAction(QIcon(':icons/album.png'), '查看专辑')
        go_album.triggered.connect(lambda: self._app.signal.show_album.emit(self._model.songs[self.menu_idx].album_id))

    def play(self, index):
        self._app.player.playinglist.stop()
        self._app.player.playinglist.clear()
        self._app.player.playinglist.adds(self._model.songs)
        self._app.signal.play_search.emit()
        self._app.player.play(index)

    def right_menu(self, point: QPoint):
        index = self.content_list.indexAt(point)
        if index.row() != -1:
            self.menu_idx = index.row()
            self.pop_menu.exec(QCursor.pos())

    def add_ui(self):
        # 注意是每个单元格在选择内，会导致每行的每个列都会有索引，导致重复的row
        song_ids = list(set([self._model.songs[i.row()].sid for i in self.content_list.selectedIndexes()]))
        select = QInputDialog(self)
        select.setComboBoxItems([f'{i+1} {x.name}' for i, x in enumerate(self._app.default_provider.playlists)])
        select.setOkButtonText('添加')
        select.setCancelButtonText('取消')
        select.setLabelText('添加歌单')
        ok = select.exec()
        if ok:
            aio.create(self.add_song_to_playlist(song_ids, int(select.textValue().split(' ')[0])-1))

    async def add_song_to_playlist(self, sids: List[str], playlist):
        pid = self._app.default_provider.playlists[playlist].id
        logger.debug(f'Prepare to add songs: {sids} to playlist {pid}')
        a = await self._app.default_provider.add_to_playlist(sids, pid)
        if a:
            await self._app.default_provider.get_playlists()
