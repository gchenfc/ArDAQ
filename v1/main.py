import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dialog import Ui_Dialog

import threading
import time

from ArduinoInterface import ArduinoInterface
from AlicatInterface import AlicatInterface
from DataCanvas import DataCanvas
from CustomWidgetWrappers import VariableListItem
from DataHandler import DataHandler

from serial.tools import list_ports

DEFAULT_FORMAT = ["{:g}s",
                  "{:g}V","{:g}A","{:g}W\t",
                  "{:g}V","{:g}A","{:g}W\t",
                  "{:%}","{:%}","{:g}°F"]
DEFAULT_FORMAT = ["t = {:g}s","V = {:g}V","I = {:g}A","{:w}"]

class MainProgram(Ui_Dialog):
    def __init__(self,dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        # graph setup
        frameSize = self.plotFrame.contentsRect().size()
        self.dataPlot = DataCanvas(self.plotFrame,
                                   width=frameSize.width()/100,
                                   height=frameSize.height()/100,
                                   dpi=100)
        self.plotFrameLayout.addWidget(self.dataPlot)
        self.plotting = False

        # serial setup
        self.initSerialNames()
        self.initSerialBaud()
        self.arduino = ArduinoInterface()
        self.alicat = AlicatInterface()

        # variable ui setup
        self.VariableLines = [];
        self.initVariableLines()

        # data handler setup
        self.data = DataHandler(len(DEFAULT_FORMAT)+1)

        # ui callbacks
        self.serialStart.pressed.connect(self.startData)
        self.serialStop.pressed.connect(self.stopData)
        self.plotClearButton.pressed.connect(self.dataPlot.clearData)
        self.numColSel.valueChanged.connect(self.updateVariableLines)
        self.fileSaveButton.pressed.connect(self.saveData)
        self.dataClearButton.pressed.connect(self.clearData)
        self.commandStringEdit.returnPressed.connect(self.sendSerialCommand)

    # serial methods
    def initSerialNames(self):
        self.serialList = list_ports.comports()
        for i in range(len(self.serialList)):
            self.serialNameComboBox.addItem(self.serialList[i].device)
        self.serialNameComboBox.activated.connect(self.changeSerialName)
        if (self.serialList[-1].device=='/dev/cu.usbserial'):
            self.changeSerialName(len(self.serialList)-2)
        else:
            self.changeSerialName(len(self.serialList)-1)
    def updateSerialNames(self):
        self.serialNameComboBox.clear()
        self.serialList = list_ports.comports()
        for i in range(len(self.serialList)):
            self.serialNameComboBox.addItem(self.serialList[i].device)
    def changeSerialName(self, ind):
        self.serialObj = self.serialList[ind]
        self.updateSerialNames()
        self.serialNameComboBox.setCurrentIndex(ind)
    def initSerialBaud(self):
        self.serialBaudComboBox.currentIndexChanged.connect(self.changeSerialBaud)
        self.changeSerialBaud(self.serialBaudComboBox.currentIndex())
    def changeSerialBaud(self,ind):
        self.serialBaud = int(self.serialBaudComboBox.itemText(ind))
    def sendSerialCommand(self):
        toSend = str(self.commandStringEdit.text());
        print("**********"+toSend)
        self.commandStringEdit.setText('');
        sendThread = threading.Thread(target=self.arduino.sendLine,kwargs={'textToSend':toSend})
        sendThread.start()

    # variable info methods
    def initVariableLines(self):
        self.numColSel.setValue(len(DEFAULT_FORMAT))
        for i,formStr in enumerate(DEFAULT_FORMAT):
            toApp = VariableListItem(self.VariablesList,i)
            toApp.setFormatStr(formStr)
            self.VariablesListLayout.insertWidget(len(self.VariableLines),toApp.getWidget())
            self.VariableLines.append(toApp)
    def updateVariableLines(self,numVars):
        while (self.VariablesListLayout.count()-1)>numVars: #1 for vertical space
            self.VariablesListLayout.removeWidget(self.VariableLines[-1].getWidget())
            self.VariableLines[-1].getWidget().deleteLater()
            del self.VariableLines[-1]
        while (self.VariablesListLayout.count()-1)<numVars:
            toAdd = VariableListItem(self.VariablesList,self.VariablesListLayout.count()-1)
            self.VariablesListLayout.insertWidget(len(self.VariableLines),toAdd.getWidget())
            self.VariableLines.append(toAdd)

    # live plotting and data collection methods
    def startData(self):
        self.plotting = True
        lineFormat = ''
        for i in self.VariableLines:
            lineFormat += i.getFormatStr()+"\t"
        lineFormat = lineFormat[0:-1]
        self.arduino.setLineFormat(lineFormat)
        self.plotThread = threading.Thread(target=self.addToPlot)
        self.plotThread.start()
    def stopData(self):
        self.plotting = False
    def addToPlot(self):
        self.arduino.setSerialName(self.serialObj.device)
        self.arduino.setBaud(self.serialBaud)
        self.arduino.start()
        self.alicat.start()
        while self.plotting:
            newPt = self.arduino.readLineFormat()
            # print(newPt);
            #newPt = self.arduino.readLineFloats(self.numColSel.value())
            if newPt!=None:
                # print('gotPt')
                toSave = [];
                for i in newPt:
                    toSave.append(i);
                toSave.append(float(self.alicat.getMostRecentData()[4]))
                self.data.addLine(toSave)
                self.dataPlot.addPoint(newPt[0],newPt[1])
                for i,v in enumerate(newPt):
                    self.VariableLines[i].updateValue(v)
                #print('doneIter')
        self.alicat.stop();
        self.arduino.close()
    # value display
    def displayValues(self):
        pass

    # save
    def saveData(self):
        self.data.saveDataMatlab();
    def clearData(self):
        self.data.clearData();
    # clean up on close
    def reject():
        self.plotting = false
        while (self.plotThread.isAlive):
            pass
        self.arduino.close()
        Ui_Dialog.reject()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MainProgram(dialog)

    dialog.show()
    sys.exit(app.exec_())
