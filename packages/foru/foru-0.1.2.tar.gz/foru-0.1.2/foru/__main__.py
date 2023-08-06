from foru.app.gui import GuiAPP
from foru.core import LPlayer

if __name__ == '__main__':
    app = GuiAPP(LPlayer())
    app.run()
