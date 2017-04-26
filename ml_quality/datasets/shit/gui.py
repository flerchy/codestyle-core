#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from xor import Xor

class Gui(QtGui.QMainWindow):
    
    def __init__(self):
        super(Gui, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        self.statusBar().showMessage('Ready')
        xor = Xor()

        self.setCentralWidget(xor)
        self.setGeometry(300, 300, 640, 320)
        self.setWindowTitle('XOR')    
        self.show()
