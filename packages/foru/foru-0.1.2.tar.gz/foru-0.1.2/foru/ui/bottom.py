import logging

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from foru.ui.control import Control
from foru.ui.info import Info
from foru.ui.progress_bar import ProgressBar
from foru.ui.vml import VML

logger = logging.getLogger('foru.ui.bottom')


class Bottom(QWidget):

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.info = Info(app)
        self.control = Control(app)
        self.progress = ProgressBar(app)
        self.vml = VML(app, self)

        blayout = QHBoxLayout()
        blayout.addWidget(self.info, 0, Qt.AlignmentFlag.AlignLeft)
        blayout.addWidget(self.control, 0, Qt.AlignmentFlag.AlignCenter)
        blayout.addWidget(self.vml, 0, Qt.AlignmentFlag.AlignRight)

        layout = QVBoxLayout()
        layout.addWidget(self.progress)
        layout.addLayout(blayout)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
