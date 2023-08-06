import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableView, QAbstractItemView, QHeaderView, QVBoxLayout

logger = logging.getLogger('foru.ui.albumlist')


class AlbumListWidget(QWidget):
    def __init__(self, app, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self.model = model

        self.content_list = QTableView()
        self.content_list.setObjectName('album_table')

        # set headers
        self.content_list.setShowGrid(False)
        self.content_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.content_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        header = self.content_list.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        header.setStretchLastSection(True)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.content_list.verticalHeader().hide()

        v_header = self.content_list.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        v_header.setDefaultSectionSize(80)

        layout = QVBoxLayout()
        layout.addWidget(self.content_list)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

        self.content_list.setModel(self.model)

        self.content_list.setColumnWidth(0, 120)
        self.content_list.setColumnWidth(1, 500)
        self.content_list.setColumnWidth(2, 120)
        self.content_list.setColumnWidth(3, 40)

        self.content_list.doubleClicked.connect(
            lambda idx: self._app.signal.show_album.emit(self.model.albums[idx.row()].id))
