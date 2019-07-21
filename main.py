# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
import design
import ftStats


__author__ = 'Vadim Arsenev'
__version__ = '1.0.2'
__data__ = '21.07.2019'


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
        self.rbFootball.setChecked(True)
        self.bgSport.buttonClicked.connect(self.bgSport_Clicked)

        # *** comboBox Tournaments ***
        self.comboBoxInit_football()
        self.comboBox.activated.connect(self.comboBox_Activated)

        # *** spinBox Gameweek. maximum and now ***
        self.comboBox_Activated()

        # *** Button ***
        self.btnParser.clicked.connect(self.pushButton_Parser)

    def pushButton_Parser(self):
        gameweek = int(self.spinBox.value())
        for league in LEAGUES:
            if self.comboBox.currentText() == league['name']:
                season_id = league['season_id']
                kindOfSport = league['kindOfSport']
                break

        try:
            ftStats.main(kindOfSport, season_id, gameweek)
        except TypeError:
            print('Invalid')

    def comboBoxInit_football(self):
        for league in LEAGUES:
            if league['kindOfSport'] == 'football':
                self.comboBox.addItem(league['name'])

    def comboBoxInit_hockey(self):
        for league in LEAGUES:
            if league['kindOfSport'] == 'hockey':
                self.comboBox.addItem(league['name'])

    def comboBox_Activated(self):
        for item in LEAGUES:
            if self.comboBox.currentText() == item['name']:
                self.spinBox.setMaximum(
                    self.seasons[item['season_id']]['finalRound'])
                try:
                    self.spinBox.setValue(
                        self.seasons[item['season_id']]['lastRound'])
                except TypeError:
                    self.spinBox.setValue(1)
                break

    def bgSport_Clicked(self, button):
        self.comboBox.clear()
        if button.text() == 'Football':
            self.comboBoxInit_football()
        elif button.text() == 'Hockey':
            self.comboBoxInit_hockey()
        self.comboBox_Activated()


def main():
    seasons = ftStats.get_season()

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(seasons)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    LEAGUES = [{'name': 'EPL 19-20', 'season_id': 387,
                'kindOfSport': 'football', },
               {'name': 'EPL 18-19', 'season_id': 234,
                'kindOfSport': 'football', },
               {'name': 'NHL 18-19', 'season_id': 286,
                'kindOfSport': 'hockey', },
               ]
    main()
