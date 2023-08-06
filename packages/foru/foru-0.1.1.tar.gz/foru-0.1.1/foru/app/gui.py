import asyncio
import locale
import logging.config
import os
import sys

from resource import resources

from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
import qasync


from app.base import BaseAPP
from app.server import Server
from core import LPlayer
from ui.main import MainWindow
from utils import aio
from utils.show import change_style



class UISignal(QObject):
    play_search = Signal()
    show_playlist = Signal(int)
    show_album = Signal(str)


class GuiAPP(BaseAPP):
    def __init__(self, player):
        super().__init__(player)
        self.win = None
        self.signal = UISignal()

    def run(self):
        _app = QApplication(sys.argv)
        locale.setlocale(locale.LC_NUMERIC, 'C')
        _app.setWindowIcon(QIcon(':/icons/icon.png'))

        change_style(_app, 'light')

        tray = QSystemTrayIcon()
        tray.setIcon(QIcon(':/icons/icon.png'))
        tray.setVisible(True)
        _app.setQuitOnLastWindowClosed(False)

        loop = qasync.QEventLoop(_app)
        asyncio.set_event_loop(loop)

        self.win = MainWindow(self)
        self.win.show()

        menu = QMenu()
        _show = QAction("显示主界面")
        _show.triggered.connect(self.show_window)
        menu.addAction(_show)

        _quit = QAction("退出")
        _quit.triggered.connect(_app.quit)
        menu.addAction(_quit)

        tray.setContextMenu(menu)
        tray.activated.connect(self.show_window)

        server = Server(self, self.cp)
        aio.create(server.start_server())

        _app.aboutToQuit.connect(self.quit)
        _app.exec()

    def show_window(self):
        self.win.showNormal()
        self.win.activateWindow()

    def quit(self):
        self.player.stop()


if __name__ == '__main__':

    app = GuiAPP(LPlayer())
    app.run()
