from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout

from core.enum import Status


class Control(QWidget):

    def __init__(self, app):
        super().__init__()
        self._player = app.player

        self.previous = QPushButton()
        self.toggle = QPushButton()
        self.next = QPushButton()

        self.previous.setIcon(QIcon(':/icons/previous.png'))
        self.toggle.setIcon(QIcon(':/icons/play.png'))
        self.next.setIcon(QIcon(':/icons/next.png'))

        self.previous.setProperty('class', 'icon_button')
        self.toggle.setProperty('class', 'icon_button')
        self.next.setProperty('class', 'icon_button')

        self.toggle.setIconSize(QSize(32, 32))

        layout = QHBoxLayout()
        layout.addWidget(self.previous)
        layout.addWidget(self.toggle)
        layout.addWidget(self.next)
        layout.setSpacing(20)

        self.setLayout(layout)

        self._player.signal.status_changed.connect(self.update_ui)

        self.previous.clicked.connect(self._previous)
        self.toggle.clicked.connect(self._toggle)
        self.next.clicked.connect(self._next)

    def _next(self):
        self._player.next()

    def _toggle(self):
        if self._player.status == Status.PLAYING:
            self._player.pause()
        else:
            self._player.resume()

    def update_ui(self):
        if self._player.status == Status.PLAYING:
            self.toggle.setIcon(QIcon(':/icons/pause.png'))
        elif self._player.status == Status.PAUSE:
            self.toggle.setIcon(QIcon(':/icons/play.png'))
        else:
            self.toggle.setIcon(QIcon(':/icons/stop.png'))

    def _previous(self):
        self._player.previous()
