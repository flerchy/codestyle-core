# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:41:08 2013

@author: Ben
"""

from __future__ import division
import time

# import like this because everything starts with Q anyways and it keeps
# the code just slightly cleaner
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import *

import numpy as np
import ui_yay

import visa


# Not sure what this is for - it's copy-paste from some example.
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class YayWindow(QMainWindow, ui_yay.Ui_MainWindow):
    
    def __init__(self, parent=None):
        # run the initializer of the class inherited from
        super(YayWindow, self).__init__()
        
        # this is where most of the GUI is made
        self.setupUi(self)    

    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        print "Yay!"
        ax = self.banana.figure.add_subplot(1,1,1)

        ax.plot([1,2,1,3,4,2])
        
        self.banana.figure.canvas.draw()        
        
            
# This snippet makes it run as a standalone program
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = YayWindow()
    form.show()
    app.exec_()    