# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\heiko\code\SL1toPhoton\gui\mainwindow.ui',
# licensing of 'C:\Users\heiko\code\SL1toPhoton\gui\mainwindow.ui' applies.
#
# Created: Sat May  4 15:46:18 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 291)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Germany))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_outfile = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_outfile.setObjectName("lineEdit_outfile")
        self.gridLayout_2.addWidget(self.lineEdit_outfile, 1, 1, 1, 1)
        self.lineEdit_infile = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_infile.setObjectName("lineEdit_infile")
        self.gridLayout_2.addWidget(self.lineEdit_infile, 0, 1, 1, 1)
        self.pushButton_open_out = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_open_out.setObjectName("pushButton_open_out")
        self.gridLayout_2.addWidget(self.pushButton_open_out, 1, 2, 1, 1)
        self.pushButton_open_in = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_open_in.setObjectName("pushButton_open_in")
        self.gridLayout_2.addWidget(self.pushButton_open_in, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.exposureLabel = QtWidgets.QLabel(self.groupBox_2)
        self.exposureLabel.setObjectName("exposureLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.exposureLabel)
        self.exposureSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.exposureSpinBox.setMaximum(999)
        self.exposureSpinBox.setObjectName("exposureSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.exposureSpinBox)
        self.exposureBottomLayersLabel = QtWidgets.QLabel(self.groupBox_2)
        self.exposureBottomLayersLabel.setObjectName("exposureBottomLayersLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.exposureBottomLayersLabel)
        self.exposureBottomLayersSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.exposureBottomLayersSpinBox.setMaximum(999)
        self.exposureBottomLayersSpinBox.setObjectName("exposureBottomLayersSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.exposureBottomLayersSpinBox)
        self.bottomLayersLabel = QtWidgets.QLabel(self.groupBox_2)
        self.bottomLayersLabel.setObjectName("bottomLayersLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bottomLayersLabel)
        self.bottomLayersSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.bottomLayersSpinBox.setMaximum(999)
        self.bottomLayersSpinBox.setObjectName("bottomLayersSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bottomLayersSpinBox)
        self.layerHeightLabel = QtWidgets.QLabel(self.groupBox_2)
        self.layerHeightLabel.setObjectName("layerHeightLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.layerHeightLabel)
        self.layerHeightDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.layerHeightDoubleSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.layerHeightDoubleSpinBox.setReadOnly(True)
        self.layerHeightDoubleSpinBox.setPrefix("")
        self.layerHeightDoubleSpinBox.setDecimals(3)
        self.layerHeightDoubleSpinBox.setSingleStep(0.05)
        self.layerHeightDoubleSpinBox.setObjectName("layerHeightDoubleSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.layerHeightDoubleSpinBox)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_convert = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.horizontalLayout.addWidget(self.pushButton_convert)
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "SL1 to Photon Converter", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "File Selection", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Output File", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Input File", None, -1))
        self.lineEdit_outfile.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Path to the Photon-File", None, -1))
        self.lineEdit_infile.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Path to the SL1-File", None, -1))
        self.pushButton_open_out.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.pushButton_open_in.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Parameters", None, -1))
        self.exposureLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Exposure", None, -1))
        self.exposureBottomLayersLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Exposure (Bottom Layers)", None, -1))
        self.bottomLayersLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Bottom Layers", None, -1))
        self.layerHeightLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Layer Height", None, -1))
        self.pushButton_convert.setText(QtWidgets.QApplication.translate("MainWindow", "Convert", None, -1))

