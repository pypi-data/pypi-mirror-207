import logging

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout


from foru.ui.bottom import Bottom
from foru.ui.content import MainContent
from foru.ui.sidebar import Sidebar

logger = logging.getLogger('foru.ui.main')


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self._app = app

        self.setWindowTitle("ForU Player")
        self.setFixedSize(1080, 720)

        self.main_content = MainContent(app, self)
        self.sidebar = Sidebar(app, self)
        self.sidebar.setFixedWidth(240)
        self.sidebar.setObjectName('sidebar')
        up_layout = QHBoxLayout()
        up_layout.addWidget(self.sidebar)
        up_layout.addWidget(self.main_content)
        up_layout.setContentsMargins(0, 0, 0, 0)
        up_layout.setSpacing(0)

        self.bottom = Bottom(app, self)
        self.bottom.setFixedHeight(80)

        self.container = QWidget(self)
        self.container.setObjectName('container')

        layout = QVBoxLayout()
        layout.addLayout(up_layout)
        layout.addWidget(self.bottom)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.container.setLayout(layout)

        self.setCentralWidget(self.container)
        self.setContentsMargins(0, 0, 0, 0)
