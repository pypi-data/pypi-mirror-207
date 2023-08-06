from foru.app.gui import GuiAPP
from foru.core import LPlayer


def main():
    app = GuiAPP(LPlayer())
    app.run()
