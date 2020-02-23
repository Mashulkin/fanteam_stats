# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtGui
import design
import ftStats


__author__ = 'Vadim Arsenev'
__version__ = '1.3.0'
__data__ = '08.09.2019'


class DialogError(QtWidgets.QDialog):

    def __init__(self, root, textError, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        # label = QtWidgets.QLabel('No parsing information!')
        label = QtWidgets.QLabel(textError)
        btnOk = QtWidgets.QPushButton('Ok')
        btnOk.clicked.connect(self.pushButton_Ok)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(btnOk)
        self.setLayout(layout)

    def pushButton_Ok(self):
        self.close()


class MyWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self, seasons):
        super().__init__()
        self.setupUi(self)

        # list of seasons with platform
        self.seasons = seasons

        # *** radio button Kind of Sport ***
        self.bgSport = QtWidgets.QButtonGroup()
        self.bgSport.addButton(self.rbFootball)
        self.bgSport.addButton(self.rbHockey)
        self.bgSport.addButton(self.rbBasketball)
        self.bgSport.addButton(self.rbBaseball)
        self.bgSport.addButton(self.rbTennis)
        self.bgSport.addButton(self.rbAmericanFootball)
        self.rbFootball.setChecked(True)
        self.rbTennis.setDisabled(True)
        self.bgSport.buttonClicked.connect(self.bgSport_Clicked)

        # *** comboBox Tournaments ***
        self.cbTournamentInit_football()
        self.cbTournament.activated.connect(self.cbTournament_Activated)

        # *** spinBox Gameweek. maximum and now ***
        self.cbTournament_Activated()

        # *** checkBox Skip ***
        self.chbSkip.setChecked(True)
        self.skipNonPlaying = True
        self.chbSkip.stateChanged.connect(self.chbSkip_Changed)

        # *** checkBox Enable Ownership 1 ***
        self.chbEnableOwnership1.setChecked(False)
        self.enableOwnership1 = False
        self.chbEnableOwnership1.stateChanged.connect(
            self.chbEnableOwnership1_Changed)

        # *** checkBox Enable Ownership 2 ***
        self.chbEnableOwnership2.setChecked(False)
        self.enableOwnership2 = False
        self.chbEnableOwnership2.stateChanged.connect(
            self.chbEnableOwnership2_Changed)
        self.chbEnableOwnership2.setDisabled(True)

        # *** lineEdit Number Tournament 1 ***
        leIntValidator = QtGui.QIntValidator(self)
        self.leNumTourn1.setValidator(leIntValidator)
        self.leNumTourn1.setEnabled(False)

        # *** lineEdit Number Tournament 2 ***
        self.leNumTourn2.setValidator(leIntValidator)
        self.leNumTourn2.setEnabled(False)

        # *** button Start***
        self.btnParser.clicked.connect(self.pushButton_Parser)

    def pushButton_Parser(self):
        """Start parsing"""
        gameweek = int(self.sbGw.value())
        numTourn1 = self.leNumTourn1.text()
        for league in LEAGUES:
            if self.cbTournament.currentText() == league['name']:
                season_id = league['season_id']
                kindOfSport = league['kindOfSport']
                break

        try:
            ftStats.main(kindOfSport, season_id, gameweek,
                         self.skipNonPlaying, numTourn1, self.enableOwnership1)
        except TypeError:
            self.textError = 'No parsing information!'
            self.dialogError = DialogError(self, textError=self.textError)
            self.dialogError.exec_()
        except KeyError:
            self.textError = 'Enter tournament number'
            self.dialogError = DialogError(self, textError=self.textError)
            self.dialogError.exec_()

    def cbTournamentInit_football(self):
        """Adding football tournaments"""
        for league in LEAGUES:
            if league['kindOfSport'] == 'football':
                self.cbTournament.addItem(league['name'])

    def cbTournamentInit_hockey(self):
        """Adding hockey tournaments"""
        for league in LEAGUES:
            if league['kindOfSport'] == 'hockey':
                self.cbTournament.addItem(league['name'])

    def cbTournamentInit_basketball(self):
        """Adding basketball tournaments"""
        for league in LEAGUES:
            if league['kindOfSport'] == 'basket':
                self.cbTournament.addItem(league['name'])

    def cbTournamentInit_baseball(self):
        """Adding baseball tournaments"""
        for league in LEAGUES:
            if league['kindOfSport'] == 'baseball':
                self.cbTournament.addItem(league['name'])

    def cbTournamentInit_tennis(self):
        """Adding tennis tournaments"""
        for league in LEAGUES:
            if league['kindOfSport'] == 'tennis':
                self.cbTournament.addItem(league['name'])

    def cbTournamentInit_americanFootball(self):
        """Adding american football tournaments"""
        for league in LEAGUES:
            if league['kindOfSport'] == 'american_football':
                self.cbTournament.addItem(league['name'])

    def cbTournament_Activated(self):
        """Adding the last and final rounds to the Gameweek spin box
        to set now and the maximum value"""
        for item in LEAGUES:
            if self.cbTournament.currentText() == item['name']:
                try:
                    self.sbGw.setMaximum(
                        self.seasons[item['season_id']]['finalRound'])
                except KeyError:
                    self.sbGw.setMaximum(item['finalRound'])
                try:
                    self.sbGw.setValue(
                        self.seasons[item['season_id']]['lastRound'])
                except KeyError:
                    self.sbGw.setValue(item['finalRound'])
                except TypeError:
                    self.sbGw.setValue(1)
                break

    def bgSport_Clicked(self, button):
        """Sport choice"""
        self.cbTournament.clear()
        if button.text() == 'Football':
            self.cbTournamentInit_football()
        elif button.text() == 'Hockey':
            self.cbTournamentInit_hockey()
        elif button.text() == 'Basketball':
            self.cbTournamentInit_basketball()
        elif button.text() == 'Baseball':
            self.cbTournamentInit_baseball()
        elif button.text() == 'Tennis':
            self.cbTournamentInit_tennis()
        elif button.text() == 'American football':
            self.cbTournamentInit_americanFootball()
        self.cbTournament_Activated()

    def chbSkip_Changed(self):
        """Choice skip or not non-playing players"""
        if self.chbSkip.isChecked():
            self.skipNonPlaying = True
        else:
            self.skipNonPlaying = False

    def chbEnableOwnership1_Changed(self):
        """Enable and disable Ownership 1"""
        if self.chbEnableOwnership1.isChecked():
            self.enableOwnership1 = True
            self.leNumTourn1.setEnabled(True)
        else:
            self.enableOwnership1 = False
            self.leNumTourn1.setEnabled(False)

    def chbEnableOwnership2_Changed(self):
        """Enable and disable Ownership 2"""
        if self.chbEnableOwnership2.isChecked():
            self.enableOwnership2 = True
            self.leNumTourn2.setEnabled(True)
        else:
            self.enableOwnership2 = False
            self.leNumTourn2.setEnabled(False)


def main():
    seasons = ftStats.get_season()
    # print(seasons)

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(seasons)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    LEAGUES = [{'name': 'EPL 2019/20', 'season_id': 387,
                'kindOfSport': 'football',
                'finalRound': 38, },
               {'name': 'EPL 2018/19', 'season_id': 234,
                'kindOfSport': 'football',
                'finalRound': 38, },
               {'name': 'Serie A 2019/20', 'season_id': 418,
                'kindOfSport': 'football',
                'finalRound': 38, },
               {'name': 'La Liga 2019/20', 'season_id': 405,
                'kindOfSport': 'football',
                'finalRound': 38, },
               {'name': 'NHL 2019/20', 'season_id': 455,
                'kindOfSport': 'hockey',
                'finalRound': 179, },
               {'name': 'NHL 2018/19', 'season_id': 286,
                'kindOfSport': 'hockey',
                'finalRound': 223, },
               {'name': 'NBA 2019/20', 'season_id': 464,
                'kindOfSport': 'basket',
                'finalRound': 168, },
               {'name': 'NBA 2018/19', 'season_id': 308,
                'kindOfSport': 'basket',
                'finalRound': 217, },
               {'name': 'MLB 2019', 'season_id': 358,
                'kindOfSport': 'baseball',
                'finalRound': 185, },
            #    {'name': 'Tennis 2019', 'season_id': 000,
            #     'kindOfSport': 'tennis',
            #     'finalRound': 000, },
               {'name': 'NFL 2019', 'season_id': 439,
                'kindOfSport': 'american_football',
                'finalRound': 17, },
               ]
    main()
