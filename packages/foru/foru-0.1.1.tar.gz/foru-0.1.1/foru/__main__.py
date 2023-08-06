from app.gui import GuiAPP
from core import LPlayer

if __name__ == '__main__':
    app = GuiAPP(LPlayer())
    app.run()
