import logging

from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QSlider

from foru.utils.show import show_duration

logger = logging.getLogger('foru.ui.progressBar')


class ProgressSignal(QObject):
    clicked = Signal(int)


class ProgressSlider(QSlider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.signal = ProgressSignal()
        self.drag = False

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        x = ev.pos().x()
        start = x / self.width() * self.maximum()
        if self.value() - 1 <= start <= self.value() + 1:
            super().mousePressEvent(ev)
            self.drag = True

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        if self.drag:
            super().mouseReleaseEvent(ev)
        else:
            x = ev.pos().x()
            logger.debug(f'Slider current x : {x}')
            a = x / self.width() * self.maximum()
            logger.debug(f'Slider current width: {self.width()}, max: {self.maximum()}, a: {a}')
            self.signal.clicked.emit(int(a))
            self.drag = False


class ProgressBar(QWidget):

    def __init__(self, app):
        super().__init__()
        self._player = app.player
        self._moving = False

        self.played = QLabel('00:00')
        self.total = QLabel('00:00')
        self.played.setProperty('class', 'time')
        self.total.setProperty('class', 'time')

        self.progress_bar = ProgressSlider(Qt.Orientation.Horizontal, self)
        self.progress_bar.setObjectName('progress_slider')
        self.progress_bar.sliderPressed.connect(self.press)
        self.progress_bar.sliderMoved.connect(self.moving)
        self.progress_bar.sliderReleased.connect(self.release)
        self.progress_bar.signal.clicked.connect(lambda x: self.seek(x))
        # self.progress_bar.actionTriggered.connect(lambda a: self.handle(a))

        layout = QHBoxLayout()
        layout.addWidget(self.played)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.total)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

        self._player.signal.position_changed.connect(self.update_progress)
        self._player.signal.start_file.connect(self.init_progress)

        self.init()

    def init(self):
        if self._player.current:
            if self._player.position:
                self.progress_bar.setMaximum(int(self._player.current.duration))
                self.progress_bar.setValue(int(self._player.position))
                self.played.setText(show_duration(self._player.position))
            self.total.setText(show_duration(self._player.duration))

    def init_progress(self):
        self.progress_bar.setMaximum(int(self._player.current.duration))
        self.total.setText(show_duration(self._player.duration))

    def update_progress(self):
        if self._player.position and not self._moving:
            self.progress_bar.setValue(int(self._player.position))
            self.played.setText(show_duration(self._player.position))

    def press(self):
        self._moving = True

    def moving(self):
        self.played.setText(show_duration(self.progress_bar.value()))

    def release(self):
        self._player.seek(self.progress_bar.value())
        self._moving = False

    def seek(self, a):
        self._player.seek(a)
