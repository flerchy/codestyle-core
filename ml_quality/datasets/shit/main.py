#from artificallib.network import Network
import sys
from PyQt4 import QtGui
from gui.gui import Gui

app = QtGui.QApplication(sys.argv)
ex = Gui()
sys.exit(app.exec_())


