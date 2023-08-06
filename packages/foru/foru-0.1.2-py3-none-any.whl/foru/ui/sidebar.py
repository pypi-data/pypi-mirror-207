import logging
import typing

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, QPoint, QSize
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QWidget, QListView, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QStyledItemDelegate, \
    QLineEdit, QMenu, QAbstractItemView, QInputDialog, QMessageBox

from foru.utils import aio

logger = logging.getLogger('foru.ui.sidebar')


class PlaylistsModel(QAbstractListModel):
    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self._app.default_provider.playlists)

    def data(self, index, role=None):
        if role == Qt.ItemDataRole.DisplayRole:
            playlists = self._app.default_provider.playlists
            pl = playlists[index.row()]
            return pl.name

    # 要让item可编辑，必须重写flags与setData方法， 其中flags需要返回带ItemIsEditable， setData控制如何处理编辑的值
    def flags(self, index: QModelIndex):
        return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled

    def setData(self, index: QModelIndex, value: typing.Any, role: int = ...) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            playlists = self._app.default_provider.playlists
            pl = playlists[index.row()]
            if pl.name != value:
                pl.name = value
                aio.create(self.change_playlist_name(pl, index))
        return True

    async def change_playlist_name(self, pl, index):
        a = await self._app.default_provider.put_playlist(pl)
        if a == 200:
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.EditRole])


class PlaylistDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        value = index.model().data(index, Qt.ItemDataRole.DisplayRole)
        editor.setText(value)

    def setModelData(self, editor: QLineEdit, model, index):
        value = editor.text()
        model.setData(index, value, Qt.ItemDataRole.EditRole)


class Sidebar(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.playlist_ui = QListView(self)
        self.playlist_ui.setProperty('class', 'under_in')
        self.model = PlaylistsModel(app=app)

        self.label = QLabel('我的歌单')
        self.add_pl = QPushButton()
        self.add_pl.setProperty('class', 'icon_button')
        self.add_pl.setIconSize(QSize(24, 24))

        self.add_pl.setIcon(QIcon('../resource/icons/folder_plus.png'))
        self.add_pl.clicked.connect(self.add_ui)

        up_layout = QHBoxLayout()
        up_layout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)
        up_layout.addWidget(self.add_pl, 0, Qt.AlignmentFlag.AlignRight)
        up_layout.setSpacing(0)
        header = QWidget()
        header.setProperty('class', 'header')
        header.setLayout(up_layout)

        layout = QVBoxLayout()
        layout.addWidget(header)
        layout.addWidget(self.playlist_ui)
        layout.setSpacing(4)
        layout.setContentsMargins(2, 0, 2, 2)
        self.setLayout(layout)

        # 开启编辑
        self.playlist_ui.setEditTriggers(QAbstractItemView.EditTrigger.SelectedClicked)
        delegate = PlaylistDelegate(self.playlist_ui)
        self.playlist_ui.setItemDelegate(delegate)

        # 开启右键菜单
        self.playlist_ui.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.playlist_ui.customContextMenuRequested[QPoint].connect(lambda p: self.right_menu(p))
        self.playlist_ui.doubleClicked.connect(lambda x: self.show_playlist(x.row()))
        self.playlist_ui.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.playlist_ui.setModel(self.model)

        self.init()

    def init(self):
        aio.create(self.get_playlists())

    async def get_playlists(self):
        logger.debug('start login before get playlists')
        await self._app.default_provider.init(self._app.cp)
        logger.debug('start get playlists')
        await self._app.default_provider.get_playlists()
        self.model.layoutChanged.emit()

    async def add_playlist(self, name):
        if name:
            a = await self._app.default_provider.add_playlist(name)
            if a:
                await self.get_playlists()

    def add_ui(self):
        qd = QInputDialog(self)
        qd.setOkButtonText('添加')
        qd.setCancelButtonText('取消')
        qd.setLabelText('添加歌单')
        ok = qd.exec()
        if ok:
            logger.debug('start add coro')
            aio.create(self.add_playlist(qd.textValue()))

    def right_menu(self, point: QPoint):
        index = self.playlist_ui.indexAt(point)
        if index.row() != -1:
            pop_menu = QMenu()
            _open = pop_menu.addAction(QIcon(':icons/open_folder.png'), '打开')
            _open.triggered.connect(self.show_playlist(index.row()))
            delete = pop_menu.addAction(QIcon(':icons/close.png'), '删除')
            delete.triggered.connect(lambda: self.delete_ui(index))
            pop_menu.exec(QCursor.pos())

    def delete_ui(self, index):
        mb = QMessageBox(self)
        mb.setText(f'是否删除歌单 {self._app.default_provider.playlists[index.row()].name}')
        mb.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        mb.setButtonText(QMessageBox.StandardButton.Yes, '确认')
        mb.setButtonText(QMessageBox.StandardButton.Cancel, '取消')
        ret = mb.exec()
        if ret == QMessageBox.StandardButton.Yes:
            aio.create(self.delete_playlist(index.row()))
        mb.close()

    async def delete_playlist(self, idx):
        logger.debug('Start delete coro')
        a = await self._app.default_provider.delete_playlist(self._app.default_provider.playlists[idx].id)
        if a:
            await self.get_playlists()
        else:
            logger.warning('Delete playlist failed.')

    def show_playlist(self, index):
        self._app.signal.show_playlist.emit(index)
