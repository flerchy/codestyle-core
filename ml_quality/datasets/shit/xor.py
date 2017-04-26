#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4 import QtCore, QtGui
from artificallib.network import Network

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Xor(QtGui.QWidget):
    
    def __init__(self):
        super(Xor, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('XOR')
        
        self.network = Network(0.5, 0.8, [2, 2, 1])
        self.network.setWeights([0.129952, -0.923123, 0.570345, -0.328932, 0.164732, 0.752621])
        self.network.setBiasValues(0, [0.341232, -0.115223])
        self.network.setBiasValues(1, [-0.993423])


        self.init()
        self.show()

    def process_input(self):
        input1 = self.input1.value()
        input2 = self.input2.value()
        
        expected_result = input1 ^ input2
        result = self.network.process([input1, input2])
        error = "%s - %s = %s" % (expected_result, result[0], (expected_result-result[0]))
        QtGui.QMessageBox.information(self, 'Result', str(result) + "\n" + error)
        
    def init(self):
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 50, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.input1 = QtGui.QSpinBox(self)
        self.input1.setGeometry(QtCore.QRect(80, 50, 62, 27))
        self.input1.setObjectName(_fromUtf8("input1"))
        self.input2 = QtGui.QSpinBox(self)
        self.input2.setGeometry(QtCore.QRect(80, 200, 62, 27))
        self.input2.setObjectName(_fromUtf8("input2"))
        self.process = QtGui.QPushButton(self)
        self.process.setGeometry(QtCore.QRect(20, 260, 131, 27))
        self.process.setMinimumSize(QtCore.QSize(131, 0))
        self.process.setObjectName(_fromUtf8("process"))

        self.train = QtGui.QPushButton(self)
        self.train.setGeometry(QtCore.QRect(450, 260, 131, 27))
        self.train.setMinimumSize(QtCore.QSize(131, 0))
        self.train.setObjectName(_fromUtf8("process"))
        
        self.process.clicked.connect(self.process_input) 
        self.train.clicked.connect(self.train_network) 
        
        self.weight0 = QtGui.QLabel(self)
        self.weight0.setGeometry(QtCore.QRect(225, 50, 40, 40))

        self.weight1 = QtGui.QLabel(self)
        self.weight1.setGeometry(QtCore.QRect(225, 80, 40, 40))

        self.weight2 = QtGui.QLabel(self)
        self.weight2.setGeometry(QtCore.QRect(225, 190, 40, 40))
        
        self.weight3 = QtGui.QLabel(self)
        self.weight3.setGeometry(QtCore.QRect(225, 225, 40, 40))
        
        self.weight4 = QtGui.QLabel(self)
        self.weight4.setGeometry(QtCore.QRect(350, 75, 40, 40))
        
        self.weight5 = QtGui.QLabel(self)
        self.weight5.setGeometry(QtCore.QRect(350, 225, 40, 40))
        
        self.bias0 = QtGui.QLabel(self)
        self.bias0.setGeometry(QtCore.QRect(310, 60, 40, 40))
        
        self.bias1 = QtGui.QLabel(self)
        self.bias1.setGeometry(QtCore.QRect(310, 210, 40, 40))
        
        self.bias2 = QtGui.QLabel(self)
        self.bias2.setGeometry(QtCore.QRect(460, 135, 40, 40))
        
        self.setWindowTitle(QtGui.QApplication.translate("self", "self", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("self", "Input 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("self", "Input 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.process.setText(QtGui.QApplication.translate("self", "Process", None, QtGui.QApplication.UnicodeUTF8))
        self.train.setText(QtGui.QApplication.translate("self", "Train", None, QtGui.QApplication.UnicodeUTF8))
        self.retranslateUi()
    
    def train_network(self):
        self.network.train([[0,0], [1,1], [1,0], [0,1]], [0, 0, 1, 1])
        self.retranslateUi()
        QtGui.QMessageBox.information(self, 'Result', "Network trained %s times." % self.network.TRAINING_CYCLES)

    def retranslateUi(self):
        weights = self.network.getWeights()
        bias = self.network.getBias()

        for i in range(len(weights)):
            label = getattr(self, "weight" + str(i)) 
            label.setText(QtGui.QApplication.translate("self", str(round(weights[i], 3)), None, QtGui.QApplication.UnicodeUTF8))
        for i in range(len(bias)):
            label = getattr(self, "bias" + str(i)) 
            label.setText(QtGui.QApplication.translate("self", str(round(bias[i], 3)), None, QtGui.QApplication.UnicodeUTF8))

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
      
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
       

        self.label = QtGui.QLabel(self)
        self.label.setGeometry(160, 40, 80, 30)

        qp.setBrush(QtGui.QColor(230, 250, 0))
        qp.drawRect(150, 50, 50, 50)
        qp.drawLine(200, 75, 300, 75 )
        qp.drawLine(200, 75, 300, 225 )

        qp.setBrush(QtGui.QColor(230, 250, 0))
        qp.drawRect(150, 200, 50, 50)
        qp.drawLine(200, 225, 300, 225 )
        qp.drawLine(200, 225, 300, 75 )

        qp.setBrush(QtGui.QColor(230, 250, 0))
        qp.drawEllipse(300,50,50,50);
        qp.drawLine(350, 75, 450, 150 )
        
        qp.setBrush(QtGui.QColor(230, 250, 0))
        qp.drawEllipse(300,200,50,50);
        qp.drawLine(350, 225, 450, 150 )
        
        qp.setBrush(QtGui.QColor(230, 250, 0))
        qp.drawEllipse(450,125,50,50);
       # qp.setBrush(QtGui.QColor(200, 0, 0))
       # qp.drawRect(10, 15, 90, 60)

       # qp.setBrush(QtGui.QColor(255, 80, 0, 160))
       # qp.drawRect(130, 15, 90, 60)

       # qp.setBrush(QtGui.QColor(25, 0, 90, 200))
       # qp.drawRect(250, 15, 90, 60)
