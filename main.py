# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
import design
import ftStats


__author__ = 'Vadim Arsenev'
__version__ = '1.1.1'
__data__ = '03.08.2019'


class DialogError(QtWidgets.QDialog):

    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root
        label = QtWidgets.QLabel('No parsing information!')
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
        self.rbFootball.setChecked(True)
        self.bgSport.buttonClicked.connect(self.bgSport_Clicked)

        # *** comboBox Tournaments ***
        self.comboBoxInit_football()
        self.comboBox.activated.connect(self.comboBox_Activated)

        # *** spinBox Gameweek. maximum and now ***
        self.comboBox_Activated()

        # *** Button ***
        self.btnParser.clicked.connect(self.pushButton_Parser)

        # *** Error window ***
        self.dialogError = DialogError(self)

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
            self.dialogError.exec_()

    def comboBoxInit_football(self):
        for league in LEAGUES:
            if league['kindOfSport'] == 'football':
                self.comboBox.addItem(league['name'])

    def comboBoxInit_hockey(self):
        for league in LEAGUES:
            if league['kindOfSport'] == 'hockey':
                self.comboBox.addItem(league['name'])

    def comboBoxInit_basketball(self):
        for league in LEAGUES:
            if league['kindOfSport'] == 'basket':
                self.comboBox.addItem(league['name'])

    def comboBoxInit_baseball(self):
        for league in LEAGUES:
            if league['kindOfSport'] == 'baseball':
                self.comboBox.addItem(league['name'])

    def comboBox_Activated(self):
        for item in LEAGUES:
            if self.comboBox.currentText() == item['name']:
                try:
                    self.spinBox.setMaximum(
                        self.seasons[item['season_id']]['finalRound'])
                except KeyError:
                    self.spinBox.setMaximum(item['finalRound'])
                try:
                    self.spinBox.setValue(
                        self.seasons[item['season_id']]['lastRound'])
                except KeyError:
                    self.spinBox.setValue(item['finalRound'])
                except TypeError:
                    self.spinBox.setValue(1)
                break

    def bgSport_Clicked(self, button):
        self.comboBox.clear()
        if button.text() == 'Football':
            self.comboBoxInit_football()
        elif button.text() == 'Hockey':
            self.comboBoxInit_hockey()
        elif button.text() == 'Basketball':
            self.comboBoxInit_basketball()
        elif button.text() == 'Baseball':
            self.comboBoxInit_baseball()
        self.comboBox_Activated()


def main():
    seasons = ftStats.get_season()
    # print(seasons)

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(seasons)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    LEAGUES = [{'name': 'EPL 19-20', 'season_id': 387,
                'kindOfSport': 'football',
                'finalRound': 38, },
               {'name': 'EPL 18-19', 'season_id': 234,
                'kindOfSport': 'football',
                'finalRound': 38, },
            #    {'name': 'NHL 19-20', 'season_id': 000,
            #     'kindOfSport': 'hockey',
            #     'finalRound': 000, },
               {'name': 'NHL 18-19', 'season_id': 286,
                'kindOfSport': 'hockey',
                'finalRound': 223, },
               {'name': 'NBA 18-19', 'season_id': 308,
                'kindOfSport': 'basket',
                'finalRound': 217, },
               {'name': 'MLB 2019', 'season_id': 358,
                'kindOfSport': 'baseball',
                'finalRound': 185, },
               ]
    main()
