import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber

import time

class VariableListItem():
    def __init__(self,parent,ind):
        self.ind = ind
        self.formatStr = ''
        self.value = 1.23456
        self.VariableLine = QtWidgets.QGroupBox(parent)
        self.VariableLine.setMinimumSize(QtCore.QSize(0, 35))
        self.VariableLine.setMaximumSize(QtCore.QSize(16777215, 35))
        self.VariableLine.setBaseSize(QtCore.QSize(0, 20))
        self.VariableLine.setAutoFillBackground(False)
        self.VariableLineGrid = QtWidgets.QGridLayout(self.VariableLine)
        self.VariableLineGrid.setContentsMargins(0, 0, 0, 0)
        self.variableLabel = QtWidgets.QLabel(str(ind+1),self.VariableLine)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variableLabel.sizePolicy().hasHeightForWidth())
        self.variableLabel.setSizePolicy(sizePolicy)
        self.variableLabel.setMinimumSize(QtCore.QSize(10, 0))
        self.variableLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.variableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.VariableLineGrid.addWidget(self.variableLabel, 0, 0, 1, 1)
        self.variableFormatSpec = QtWidgets.QLineEdit(self.VariableLine)
        self.VariableLineGrid.addWidget(self.variableFormatSpec, 0, 1, 1, 1)
        self.variableValue = DataLabel(self.VariableLine)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.variableValue.sizePolicy().hasHeightForWidth())
        self.variableValue.setSizePolicy(sizePolicy)
        self.variableValue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variableValue.setDigitCount(4)
        self.variableValue.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.variableValue.setProperty("value", self.value)
        self.VariableLineGrid.addWidget(self.variableValue, 0, 2, 1, 1)
        self.radioPlotSel = QtWidgets.QCheckBox(self.VariableLine)
        self.radioPlotSel.setObjectName("radioPlotSel")
        self.radioPlotSel.setText("")
        self.VariableLineGrid.addWidget(self.radioPlotSel, 0, 3, 1, 1)
        self.radioSaveSel = QtWidgets.QCheckBox(self.VariableLine)
        self.radioSaveSel.setObjectName("radioSaveSel")
        self.radioSaveSel.setText("")
        self.VariableLineGrid.addWidget(self.radioSaveSel, 0, 4, 1, 1)
        self.variableFormatSpec.editingFinished.connect(self.updateFormatStr)
    def getWidget(self):
        return self.VariableLine
    def updateFormatStr(self):
        self.formatStr = self.variableFormatSpec.text()
    def setFormatStr(self,newFormat):
        self.formatStr = newFormat
        self.variableFormatSpec.setText(self.formatStr)
    def getFormatStr(self):
        return self.formatStr
    def updateValue(self,newVal):
        self.value = newVal
        self.variableValue.updateValue(self.value)
    def setPlotSel(self,toPlot):
        self.radioPlotSel = che
        
class DataLabel(QLCDNumber):
    def __init__(self,parent):
        QLCDNumber.__init__(self,parent)
        self.lastUpdateTime = time.time()
    def updateValue(self,newVal):
        if time.time()-self.lastUpdateTime>0.1:
            self.display(newVal)
            self.lastUpdateTime = time.time()
