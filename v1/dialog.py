# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.FileControls = QtWidgets.QGroupBox(Dialog)
        self.FileControls.setMinimumSize(QtCore.QSize(0, 100))
        self.FileControls.setObjectName("FileControls")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.FileControls)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fileSaveButton = QtWidgets.QPushButton(self.FileControls)
        self.fileSaveButton.setObjectName("fileSaveButton")
        self.gridLayout_3.addWidget(self.fileSaveButton, 0, 0, 1, 1)
        self.fileLoadButton = QtWidgets.QPushButton(self.FileControls)
        self.fileLoadButton.setObjectName("fileLoadButton")
        self.gridLayout_3.addWidget(self.fileLoadButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.FileControls, 1, 0, 1, 1)
        self.SerialControls = QtWidgets.QGroupBox(Dialog)
        self.SerialControls.setMinimumSize(QtCore.QSize(150, 190))
        self.SerialControls.setMaximumSize(QtCore.QSize(200, 300))
        self.SerialControls.setObjectName("SerialControls")
        self.formLayout = QtWidgets.QFormLayout(self.SerialControls)
        self.formLayout.setObjectName("formLayout")
        self.serialNameLabel = QtWidgets.QLabel(self.SerialControls)
        self.serialNameLabel.setObjectName("serialNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.serialNameLabel)
        self.serialNameComboBox = QtWidgets.QComboBox(self.SerialControls)
        self.serialNameComboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.serialNameComboBox.setObjectName("serialNameComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.serialNameComboBox)
        self.serialBaudLabel = QtWidgets.QLabel(self.SerialControls)
        self.serialBaudLabel.setObjectName("serialBaudLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.serialBaudLabel)
        self.serialBaudComboBox = QtWidgets.QComboBox(self.SerialControls)
        self.serialBaudComboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.serialBaudComboBox.setObjectName("serialBaudComboBox")
        self.serialBaudComboBox.addItem("")
        self.serialBaudComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.serialBaudComboBox)
        self.numColLabel = QtWidgets.QLabel(self.SerialControls)
        self.numColLabel.setObjectName("numColLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.numColLabel)
        self.numColSel = QtWidgets.QSpinBox(self.SerialControls)
        self.numColSel.setMinimum(1)
        self.numColSel.setMaximum(15)
        self.numColSel.setProperty("value", 2)
        self.numColSel.setObjectName("numColSel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.numColSel)
        self.serialStart = QtWidgets.QPushButton(self.SerialControls)
        self.serialStart.setObjectName("serialStart")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.serialStart)
        self.serialStop = QtWidgets.QPushButton(self.SerialControls)
        self.serialStop.setObjectName("serialStop")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.serialStop)
        self.gridLayout.addWidget(self.SerialControls, 0, 0, 1, 1)
        self.VariableControls = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VariableControls.sizePolicy().hasHeightForWidth())
        self.VariableControls.setSizePolicy(sizePolicy)
        self.VariableControls.setMinimumSize(QtCore.QSize(150, 0))
        self.VariableControls.setAutoFillBackground(True)
        self.VariableControls.setObjectName("VariableControls")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.VariableControls)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.VariablesLabel = QtWidgets.QGroupBox(self.VariableControls)
        self.VariablesLabel.setObjectName("VariablesLabel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.VariablesLabel)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.VariablesLabel)
        self.label.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.VariablesLabel)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.VariablesLabel)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.VariablesLabel)
        self.VariablesList = QtWidgets.QWidget(self.VariableControls)
        self.VariablesList.setObjectName("VariablesList")
        self.VariablesListLayout = QtWidgets.QVBoxLayout(self.VariablesList)
        self.VariablesListLayout.setContentsMargins(0, 0, 0, 0)
        self.VariablesListLayout.setSpacing(0)
        self.VariablesListLayout.setObjectName("VariablesListLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.VariablesListLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.VariablesList)
        self.gridLayout.addWidget(self.VariableControls, 0, 1, 2, 1)
        self.plotControls = QtWidgets.QGroupBox(Dialog)
        self.plotControls.setMinimumSize(QtCore.QSize(0, 100))
        self.plotControls.setObjectName("plotControls")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.plotControls)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plotClearButton = QtWidgets.QPushButton(self.plotControls)
        self.plotClearButton.setObjectName("plotClearButton")
        self.gridLayout_4.addWidget(self.plotClearButton, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.plotControls, 3, 3, 1, 2)
        self.plotFrame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy)
        self.plotFrame.setMinimumSize(QtCore.QSize(400, 400))
        self.plotFrame.setSizeIncrement(QtCore.QSize(0, 0))
        self.plotFrame.setBaseSize(QtCore.QSize(400, 400))
        self.plotFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plotFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.plotFrame.setObjectName("plotFrame")
        self.plotFrameLayout = QtWidgets.QGridLayout(self.plotFrame)
        self.plotFrameLayout.setObjectName("plotFrameLayout")
        self.gridLayout.addWidget(self.plotFrame, 0, 3, 3, 2)

        self.retranslateUi(Dialog)
        self.serialNameComboBox.setCurrentIndex(-1)
        self.serialBaudComboBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Arduino Data Acquisition"))
        self.FileControls.setTitle(_translate("Dialog", "Save/Open"))
        self.fileSaveButton.setText(_translate("Dialog", "Save"))
        self.fileLoadButton.setText(_translate("Dialog", "Load"))
        self.SerialControls.setTitle(_translate("Dialog", "Arduino Settings"))
        self.serialNameLabel.setText(_translate("Dialog", "Serial Port"))
        self.serialBaudLabel.setText(_translate("Dialog", "Baud Rate"))
        self.serialBaudComboBox.setItemText(0, _translate("Dialog", "9600"))
        self.serialBaudComboBox.setItemText(1, _translate("Dialog", "115200"))
        self.numColLabel.setText(_translate("Dialog", "# of Data"))
        self.serialStart.setText(_translate("Dialog", "Start"))
        self.serialStop.setText(_translate("Dialog", "Stop"))
        self.VariableControls.setTitle(_translate("Dialog", "Variables"))
        self.label.setText(_translate("Dialog", "#"))
        self.label_2.setText(_translate("Dialog", "Format"))
        self.label_3.setText(_translate("Dialog", "Value"))
        self.plotControls.setTitle(_translate("Dialog", "Plot Controls"))
        self.plotClearButton.setText(_translate("Dialog", "Clear Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
