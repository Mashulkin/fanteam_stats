# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
import design
import ftStats
from modules.parser import Parser



class MyWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, seasons):
        super().__init__()
        self.setupUi(self)

        # list of seasons with fanteam
        self.seasons = seasons

        # *** radio button Kind of Sport ***
        self.bgSport = QtWidgets.QButtonGroup()
        self.bgSport.addButton(self.rbFootball)
        self.bgSport.addButton(self.rbHockey)

        self.rbFootball.setChecked(True)
        self.bgSport.buttonClicked.connect(self.rbSport_Clicked)

        # *** comboBox Tournaments ***
        self.comboBox.addItem('EPL 18-19')

        # *** spinBox Gameweek. maximum and now ***
        self.spinBox.setMaximum(38)
        self.spinBox.setValue(38)
        # self.spinBox.setMaximum(self.seasons[234]['finalRound'])
        # self.spinBox.setValue(self.seasons[234]['lastRound'])

        # *** Button ***
        self.btnParser.clicked.connect(self.pushButton_Parser)

    def pushButton_Parser(self):
        gameweek = int(self.spinBox.value())

        if self.rbFootball.isChecked():
            kindOfSport = 'football'
        elif self.rbHockey.isChecked():
            kindOfSport = 'hockey'

        if self.comboBox.currentText() == 'EPL 18-19':
            season_id = 234
        elif self.comboBox.currentText() == 'NHL 18-19':
            season_id = 286

        ftStats.main(kindOfSport, season_id, gameweek)

    def rbSport_Clicked(self, button):
        if button.text() == 'Football':
            self.comboBox.clear()
            self.comboBox.addItem('EPL 18-19')
            self.spinBox.setMaximum(self.seasons[234]['finalRound'])
            self.spinBox.setValue(self.seasons[234]['lastRound'])
        elif button.text() == 'Hockey':
            self.comboBox.clear()
            self.comboBox.addItem('NHL 18-19')
            self.spinBox.setMaximum(self.seasons[286]['finalRound'])
            self.spinBox.setValue(self.seasons[286]['lastRound'])
        # print(button.text())


def get_season():
    url = f'{ftStats.API_URL}/match_collections?statuses[]=waiting&' + \
        f'tab=admin_created&type=fantasy&per_page=10&page=0'
    # seasons_data = ftStats.get_page_data(ftStats.get_html(url))
    authorization = {'Authorization': 'Bearer fanteam undefined'}
    platform = Parser(url, authorization)
    seasons_data = platform.parserResult()
    # print(seasons_data)

    seasons = {}
    for item in seasons_data['seasons']:
        year = item.get('season')
        league = item.get('league')['name']
        gameType = item.get('league')['gameType']
        season_id = item.get('id')
        finalRound = item.get('finalRound')
        lastRound = item.get('lastRound')
        seasons.update({season_id: {'year': year,
                                    'league': league,
                                    'gameType': gameType,
                                    'finalRound': finalRound,
                                    'lastRound': lastRound}})
    print(seasons)
    return seasons


def main():
    seasons = get_season()

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(seasons)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
