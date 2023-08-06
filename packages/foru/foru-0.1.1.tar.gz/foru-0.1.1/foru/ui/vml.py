import logging

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QPushButton, QSlider, QHBoxLayout

from core.enum import Mode
from ui.playinglist import PlayingWidget

logger = logging.getLogger('foru.ui.vml')


class VML(QWidget):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._app = app
        self._volume = 0

        self.mode_bt = QPushButton()
        self.playing_bt = QPushButton()
        self.playing_bt.setIcon(QIcon(':/icons/playinglist.png'))
        self.volume_bt = QPushButton()
        self.volume_bt.setIcon(QIcon(':/icons/volume_half.png'))

        self.mode_bt.setProperty('class', 'icon_button')
        self.playing_bt.setProperty('class', 'icon_button')
        self.volume_bt.setProperty('class', 'icon_button')

        self.volume_bt.clicked.connect(self.mute)
        self.volume_sl = QSlider(Qt.Orientation.Horizontal)
        self.volume_sl.setFixedWidth(100)
        self.volume_sl.setMaximum(100)
        self.volume_sl.actionTriggered.connect(self.handle)
        self.volume_sl.setToolTip(f'{self.volume_sl.value()}')

        self._app.player.signal.volume_changed.connect(self._update_volume_ui)
        self._app.player.signal.mode_changed.connect(self._update_mode_ui)

        layout = QHBoxLayout()
        layout.addWidget(self.mode_bt)
        layout.addWidget(self.volume_bt)
        layout.addWidget(self.volume_sl)

        layout.addWidget(self.playing_bt)
        layout.setSpacing(10)

        self.mode_bt.clicked.connect(self._change_mode)
        self.volume_sl.valueChanged.connect(self._change_volume)
        self.playing_bt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.playing_bt.clicked.connect(self._show_playing)

        self.playing_ui = PlayingWidget(self._app, self.parent().parent())
        self.playing_ui.setObjectName('playing')
        self.playing_ui.setGeometry(780, 0, 300, 640)
        self.playing_ui.hide()

        self.setLayout(layout)

        self.init()

    def init(self):
        self._update_mode_ui()
        self._update_volume_ui()

    def _change_mode(self):
        if self._app.player.mode == Mode.NORMAL:
            self._app.player.mode = Mode.REPEAT_ALL
        elif self._app.player.mode == Mode.REPEAT_ALL:
            self._app.player.mode = Mode.REPEAT_ONE
        elif self._app.player.mode == Mode.REPEAT_ONE:
            self._app.player.mode = Mode.SHUFFLE
        else:
            self._app.player.mode = Mode.NORMAL

    def _update_mode_ui(self):
        if self._app.player.mode == Mode.NORMAL:
            self.mode_bt.setIcon(QIcon(':/icons/order.png'))
        elif self._app.player.mode == Mode.REPEAT_ALL:
            self.mode_bt.setIcon(QIcon(':/icons/repeat.png'))
        elif self._app.player.mode == Mode.REPEAT_ONE:
            self.mode_bt.setIcon(QIcon(':/icons/repeat_one.png'))
        else:
            self.mode_bt.setIcon(QIcon(':/icons/shuffle.png'))

    def _change_volume(self):
        self._app.player.volume = self.volume_sl.value()

    def _update_volume_ui(self):
        self.volume_sl.setValue(self._app.player.volume)
        if self._app.player.volume == 0:
            self.volume_bt.setIcon(QIcon(':/icons/mute.png'))
        elif self._app.player.volume < 50:
            self.volume_bt.setIcon(QIcon(':/icons/volume_half.png'))
        else:
            self.volume_bt.setIcon(QIcon(':/icons/volume_full.png'))
        self.volume_sl.setToolTip(f'{self._app.player.volume}')

    def _show_playing(self):
        if self.playing_ui.isVisible():
            self.playing_ui.hide()
        else:
            self.playing_ui.show()
            self.playing_ui.raise_()

    def handle(self, action):
        if action == QSlider.SliderAction.SliderSingleStepSub:
            self.volume_sl.setValue(self.volume_sl.value() - 1)
        elif action == QSlider.SliderAction.SliderSingleStepAdd:
            self.volume_sl.setValue(self.volume_sl.value() + 1)
        elif action == QSlider.SliderAction.SliderPageStepAdd:
            self.volume_sl.setValue(self.volume_sl.value() + 5)
        elif action == QSlider.SliderAction.SliderPageStepSub:
            self.volume_sl.setValue(self.volume_sl.value() - 5)

    def mute(self):
        if self._app.player.volume != 0:
            self._volume = self._app.player.volume
            self._app.player.volume = 0
        else:
            self._app.player.volume = self._volume
