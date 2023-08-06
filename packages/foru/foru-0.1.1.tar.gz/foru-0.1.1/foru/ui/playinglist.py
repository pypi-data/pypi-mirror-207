from typing import Union, Any

import PySide6.QtGui
from PySide6.QtCore import Qt, QModelIndex, QAbstractTableModel, QSize
from PySide6.QtGui import QIcon, QPainter, QMovie
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTableView, QAbstractItemView, QLabel,\
    QStyledItemDelegate, QStyleOptionViewItem, QStyleOptionButton, QApplication, QStyle


class PlayingModel(QAbstractTableModel):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self._app.player.signal.start_file.connect(self.layoutChanged.emit)

    def data(self, index, role=None):
        if role == Qt.ItemDataRole.DisplayRole:
            song = self._app.player.playinglist.songs[index.row()]
            if index.column() == 1:
                return f'{song.title} - {song.artist}'
            else:
                return index.row() + 1

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return 3

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._app.player.playinglist.songs)

    def setData(self, index: Union[PySide6.QtCore.QModelIndex, PySide6.QtCore.QPersistentModelIndex], value: Any,
                role: int = ...) -> bool:
        return super().setData(index, value, role)

    @property
    def current(self):
        return self._app.player.playinglist.current


class PlayingDelegate(QStyledItemDelegate):
    def __init__(self, parent=None, player=None):
        super().__init__(parent)
        self._player = player
        self.movie = QMovie(':/icons/playing.gif')
        self.movie.start()
        self.icon = QIcon(':icons/trash.svg')
        self.bt = QPushButton()
        self.bt.setProperty('class', 'icon_button')

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index) -> None:
        if index.column() == 0 and index.row() == self._player.playinglist.current:
            option: QStyleOptionViewItem = option.__class__(option)
            pixmap = self.movie.currentPixmap()
            painter.drawPixmap(option.rect, pixmap)
        elif index.column() == 2:
            opt = QStyleOptionButton()
            opt.rect = option.rect
            opt.icon = self.icon
            opt.iconSize = QSize(24, 24)
            QApplication.style().drawControl(QStyle.ControlElement.CE_PushButton, opt, painter, self.bt)
        else:
            super().paint(painter, option, index)

    def sizeHint(self, option, index):
        super().sizeHint(option, index)


class MTableView(QTableView):
    def focusOutEvent(self, event: PySide6.QtGui.QFocusEvent) -> None:
        self.parent().hide()

    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None:
        self.setFocus()


class PlayingWidget(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app

        self.playinglist_ui = MTableView(self)
        self.playinglist_ui.setShowGrid(False)
        self.playinglist_ui.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.playinglist_ui.setObjectName('playing')
        self.playinglist_ui.setProperty('class', 'under_in')

        self.playinglist_ui.verticalHeader().hide()
        self.playinglist_ui.horizontalHeader().hide()
        self.playinglist_ui.doubleClicked.connect(lambda x: self._app.player.play(x.row()))
        self.playinglist_ui.clicked.connect(lambda x: self.delete_playing_song(x))

        self.model = PlayingModel(app)
        self.playinglist_ui.setModel(self.model)
        self.playinglist_ui.setColumnWidth(0, 40)
        self.playinglist_ui.setColumnWidth(1, 180)
        self.playinglist_ui.setColumnWidth(2, 40)

        self.tip = QLabel('正在播放', self)
        self.clear_bt = QPushButton('清空', self)
        self.clear_bt.setIcon(QIcon(':/icons/trash.svg'))
        self.clear_bt.clicked.connect(self._clear)

        # 设置delegate
        self.delegate = PlayingDelegate(self.playinglist_ui, app.player)
        self.playinglist_ui.setItemDelegate(self.delegate)

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.tip, 0, Qt.AlignmentFlag.AlignLeft)
        header_layout.addWidget(self.clear_bt, 0, Qt.AlignmentFlag.AlignRight)
        header = QWidget(self)
        header.setLayout(header_layout)
        header.setProperty('class', 'header')

        layout = QVBoxLayout()
        layout.addWidget(header)
        layout.addWidget(self.playinglist_ui)
        layout.setSpacing(0)
        layout.setContentsMargins(2, 0, 2, 2)

        self.setLayout(layout)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self._app.signal.play_search.connect(self.model.layoutChanged.emit)
        self._app.player.signal.position_changed.connect(self.playinglist_ui.viewport().update)

    def _clear(self):
        self._app.player.playinglist.clear()
        self._app.player.stop()
        self.model.layoutChanged.emit()

    def delete_playing_song(self, index):
        if index.column() == 2:
            self._app.player.playinglist.remove(index.row())
            self.model.layoutChanged.emit()
