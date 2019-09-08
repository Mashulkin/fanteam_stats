# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(610, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # label Kind of sport
        self.lbSport = QtWidgets.QLabel(self.centralwidget)
        self.lbSport.setGeometry(QtCore.QRect(30, 20, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setUnderline(False)
        self.lbSport.setFont(font)
        self.lbSport.setObjectName("lbSport")
        # label Tournament
        self.lbTournament = QtWidgets.QLabel(self.centralwidget)
        self.lbTournament.setGeometry(QtCore.QRect(450, 20, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lbTournament.setFont(font)
        self.lbTournament.setObjectName("lbTournament")
        # label Gameweek
        self.lbGw = QtWidgets.QLabel(self.centralwidget)
        self.lbGw.setGeometry(QtCore.QRect(250, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lbGw.setFont(font)
        self.lbGw.setObjectName("lbGw")
        # radio button Football
        self.rbFootball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbFootball.setGeometry(QtCore.QRect(30, 60, 100, 20))
        self.rbFootball.setObjectName("rbFootball")
        # radio button Hockey
        self.rbHockey = QtWidgets.QRadioButton(self.centralwidget)
        self.rbHockey.setGeometry(QtCore.QRect(30, 90, 100, 20))
        self.rbHockey.setObjectName("rbHockey")
        # radio button Basketball
        self.rbBasketball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbBasketball.setGeometry(QtCore.QRect(30, 120, 100, 20))
        self.rbBasketball.setObjectName("rbBasketball")
        # radio button Baseball
        self.rbBaseball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbBaseball.setGeometry(QtCore.QRect(30, 180, 100, 20))
        self.rbBaseball.setObjectName("rbBaseball")
        # radio button Tennis
        self.rbTennis = QtWidgets.QRadioButton(self.centralwidget)
        self.rbTennis.setGeometry(QtCore.QRect(30, 150, 100, 20))
        self.rbTennis.setObjectName("rbTennis")
        # radio button American Football
        self.rbAmericanFootball = QtWidgets.QRadioButton(self.centralwidget)
        self.rbAmericanFootball.setGeometry(QtCore.QRect(30, 210, 150, 20))
        self.rbAmericanFootball.setObjectName("rbAmericanFootball")
        # combo box Tournament
        self.cbTournament = QtWidgets.QComboBox(self.centralwidget)
        self.cbTournament.setGeometry(QtCore.QRect(420, 55, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbTournament.setFont(font)
        self.cbTournament.setObjectName("cbTournament")
        # vertical line
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(170, 50, 10, 190))
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        # spin box Gameweek
        self.sbGw = QtWidgets.QSpinBox(self.centralwidget)
        self.sbGw.setGeometry(QtCore.QRect(260, 110, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sbGw.setFont(font)
        self.sbGw.setMinimum(1)
        self.sbGw.setMaximum(299)
        self.sbGw.setObjectName("sbGw")
        # button Start parsing
        self.btnParser = QtWidgets.QPushButton(self.centralwidget)
        self.btnParser.setGeometry(QtCore.QRect(215, 160, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnParser.setFont(font)
        self.btnParser.setObjectName("btnParser")
        # check box Skip non-playing players
        self.chbSkip = QtWidgets.QCheckBox(self.centralwidget)
        self.chbSkip.setGeometry(QtCore.QRect(190, 60, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chbSkip.setFont(font)
        self.chbSkip.setObjectName("chbSkip")
        # vertical line2
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(395, 50, 10, 190))
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        # check box Enable Ownership1
        self.chbEnableOwnership1 = QtWidgets.QCheckBox(self.centralwidget)
        self.chbEnableOwnership1.setGeometry(QtCore.QRect(420, 100, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chbEnableOwnership1.setFont(font)
        self.chbEnableOwnership1.setObjectName("chbEnableOwnership1")
        # check box Enable Ownership2
        self.chbEnableOwnership2 = QtWidgets.QCheckBox(self.centralwidget)
        self.chbEnableOwnership2.setGeometry(QtCore.QRect(420, 170, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chbEnableOwnership2.setFont(font)
        self.chbEnableOwnership2.setObjectName("chbEnableOwnership2")
        # line edit Number Tournament1
        self.leNumTourn1 = QtWidgets.QLineEdit(self.centralwidget)
        self.leNumTourn1.setGeometry(QtCore.QRect(470, 130, 80, 25))
        self.leNumTourn1.setObjectName("leNumTourn1")
        # line edit Number Tournament2
        self.leNumTourn2 = QtWidgets.QLineEdit(self.centralwidget)
        self.leNumTourn2.setGeometry(QtCore.QRect(470, 200, 80, 25))
        self.leNumTourn2.setObjectName("leNumTourn2")
        # label Number Tournament1
        self.lbNumTourn1 = QtWidgets.QLabel(self.centralwidget)
        self.lbNumTourn1.setGeometry(QtCore.QRect(450, 130, 30, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lbNumTourn1.setFont(font)
        self.lbNumTourn1.setObjectName("lbNumTourn1")
        # label Number Tournament2
        self.lbNumTourn2 = QtWidgets.QLabel(self.centralwidget)
        self.lbNumTourn2.setGeometry(QtCore.QRect(450, 200, 30, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lbNumTourn2.setFont(font)
        self.lbNumTourn2.setObjectName("lbNumTourn2")
        # vertical line
        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(440, 165, 118, 3))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")

        MainWindow.setCentralWidget(self.centralwidget)
        # statusbar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Stats on Fanteam v1.3.0 (by Vadim Arsenev)"))
        self.lbSport.setText(_translate("MainWindow", "Kind of sport"))
        self.lbTournament.setText(_translate("MainWindow", "Tournaments"))
        self.lbGw.setText(_translate("MainWindow", "Gameweek"))
        self.rbFootball.setText(_translate("MainWindow", "Football"))
        self.rbHockey.setText(_translate("MainWindow", "Hockey"))
        self.rbBasketball.setText(_translate("MainWindow", "Basketball"))
        self.rbBaseball.setText(_translate("MainWindow", "Baseball"))
        self.rbTennis.setText(_translate("MainWindow", "Tennis"))
        self.rbAmericanFootball.setText(_translate(
            "MainWindow", "American football"))
        self.btnParser.setText(_translate("MainWindow", "Start"))
        self.chbSkip.setText(_translate(
            "MainWindow", "Skipping non-playing players"))
        self.chbEnableOwnership1.setText(_translate(
            "MainWindow", "Enable ownership"))
        self.chbEnableOwnership2.setText(_translate(
            "MainWindow", "Enable ownership"))
        self.lbNumTourn1.setText(_translate("MainWindow", "№"))
        self.lbNumTourn2.setText(_translate("MainWindow", "№"))
