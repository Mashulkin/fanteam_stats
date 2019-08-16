# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(555, 219)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rbFootball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbFootball.setGeometry(QtCore.QRect(30, 60, 100, 20))
        self.rbFootball.setObjectName("rbFootball")
        self.rbHockey = QtWidgets.QRadioButton(self.centralwidget)
        self.rbHockey.setGeometry(QtCore.QRect(30, 90, 100, 20))
        self.rbHockey.setObjectName("rbHockey")
        self.rbBasketball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbBasketball.setGeometry(QtCore.QRect(30, 120, 100, 20))
        self.rbBasketball.setObjectName("rbBasketball")
        self.rbBaseball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbBaseball.setGeometry(QtCore.QRect(30, 150, 100, 20))
        self.rbBaseball.setObjectName("rbBaseball")
        self.lbSport = QtWidgets.QLabel(self.centralwidget)
        self.lbSport.setGeometry(QtCore.QRect(20, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbSport.setFont(font)
        self.lbSport.setObjectName("lbSport")
        self.lbTournament = QtWidgets.QLabel(self.centralwidget)
        self.lbTournament.setGeometry(QtCore.QRect(220, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lbTournament.setFont(font)
        self.lbTournament.setObjectName("lbTournament")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 70, 161, 26))
        self.comboBox.setObjectName("comboBox")
        self.lbGw = QtWidgets.QLabel(self.centralwidget)
        self.lbGw.setGeometry(QtCore.QRect(420, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lbGw.setFont(font)
        self.lbGw.setObjectName("lbGw")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(440, 70, 61, 24))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(299)
        self.spinBox.setObjectName("spinBox")
        self.btnParser = QtWidgets.QPushButton(self.centralwidget)
        self.btnParser.setGeometry(QtCore.QRect(220, 130, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnParser.setFont(font)
        self.btnParser.setObjectName("btnParser")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(50, 190, 20, 20))
        self.checkBox.setObjectName("checkBox")
        self.lbSkip = QtWidgets.QLabel(self.centralwidget)
        self.lbSkip.setGeometry(QtCore.QRect(70, 183, 150, 31))
        self.lbSkip.setObjectName("lbSkip")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Stats on Fanteam v.1.2.0 (by Vadim Arsenev)"))
        self.rbFootball.setText(_translate("MainWindow", "Football"))
        self.rbHockey.setText(_translate("MainWindow", "Hockey"))
        self.rbBasketball.setText(_translate("MainWindow", "Basketball"))
        self.rbBaseball.setText(_translate("MainWindow", "Baseball"))
        self.lbSport.setText(_translate("MainWindow", "Kind of sport"))
        self.lbTournament.setText(_translate("MainWindow", "Tournaments"))
        self.lbGw.setText(_translate("MainWindow", "Gameweek"))
        self.btnParser.setText(_translate("MainWindow", "Start parsing"))
        self.checkBox.setText(_translate("MainWindow", ""))
        self.lbSkip.setText(_translate("MainWindow", "Skipping non-playing players"))
