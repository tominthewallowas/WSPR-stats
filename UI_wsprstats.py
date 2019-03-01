# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_wsprstats.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tblStats = QtWidgets.QTableView(self.centralwidget)
        self.tblStats.setGeometry(QtCore.QRect(30, 390, 631, 161))
        self.tblStats.setObjectName("tblStats")
        self.tblStats.horizontalHeader().setDefaultSectionSize(65)
        self.cmbReporters = QtWidgets.QComboBox(self.centralwidget)
        self.cmbReporters.setGeometry(QtCore.QRect(30, 40, 151, 22))
        self.cmbReporters.setObjectName("cmbReporters")
        self.cmbXmits = QtWidgets.QComboBox(self.centralwidget)
        self.cmbXmits.setGeometry(QtCore.QRect(200, 40, 151, 22))
        self.cmbXmits.setObjectName("cmbXmits")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 101, 16))
        self.label_2.setObjectName("label_2")
        self.lblCallsignFacts = QtWidgets.QLabel(self.centralwidget)
        self.lblCallsignFacts.setGeometry(QtCore.QRect(30, 345, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCallsignFacts.setFont(font)
        self.lblCallsignFacts.setText("")
        self.lblCallsignFacts.setObjectName("lblCallsignFacts")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menu_Quit = QtWidgets.QMenu(self.menubar)
        self.menu_Quit.setObjectName("menu_Quit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.menu_Quit.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_Quit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Reporting Stations"))
        self.label_2.setText(_translate("MainWindow", "Transmitting Stations"))
        self.menu_Quit.setTitle(_translate("MainWindow", "&File"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))

