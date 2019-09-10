# -*- coding: utf-8 -*-
import csv
import sys
import os.path
from modules.parser import Parser

API_URL = 'https://fanteam-game.api.scoutgg.net'

# for terminal and .exe in Windows
FILENAME = ['./data/ftStats.csv']
# for app in Mac OS
# FILENAME = ['/'.join(sys.argv[0].split('/')[:-4]), '/data/ftStats.csv']


def write_csv(data):
    """Write data in csv file"""
    if not os.path.exists(os.path.dirname(FILENAME[0])):
        os.makedirs(os.path.dirname(FILENAME[0]))
    with open(''.join(FILENAME), 'a', encoding='utf-8') as file:
        order = ['firstName',
                 'lastName',
                 'teamName',
                 'abbr',
                 'position',
                 'totalPoints',
                 'minutesPlayed',
                 'gw_points',
                 'seasonPrice',
                 'gw_price',
                 'selectedRatio',
                 'captainedRatio',
                 'fieldTeam',
                 'abbr_rival',
                 'gameweek', ]
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def run_once(f):
    def wrapper(*args, **kwargs):
        wrapper.has_run = os.path.isfile(''.join(FILENAME))
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@run_once
def print_headline():
    """Insert table header. The general part, plus additional fields
       for various sports"""
    data_headline = {'firstName': 'firstName',
                     'lastName': 'lastName',
                     'teamName': 'Team',
                     'abbr': 'Abbr',
                     'abbr_rival': 'Rival',
                     'position': 'Pos',
                     'fieldTeam': 'St',
                     'gw_points': 'Points',
                     'gw_price': 'Cost',
                     'gameweek': 'Gw',
                     'selectedRatio': 'Select',
                     'captainedRatio': 'Cap',
                     'seasonPrice': 'Season',
                     'totalPoints': 'Total',
                     'minutesPlayed': 'Min', }
    write_csv(data_headline)


def get_position(member):
    """Request and field position formatting"""
    try:
        position_name = member.get('position').split('_')
    except AttributeError:
        position = None
        return position

    try:
        position = position_name[1][0].upper() + position_name[0][0].upper()
    except IndexError:
        position = position_name[0][0].upper()
    # for football and hockey
    position = 'GK' if position == 'G' else position
    # for baseball
    position = 'OF' if position == 'O' else position
    position = '1B' if position == 'BF' else position
    position = '2B' if position == 'BS' else position
    position = '3B' if position == 'BT' else position
    return position


def get_player_name(player):
    """Getting full player name"""
    firstName = player.get('firstName')
    lastName = player.get('lastName')
    # if first_name is not None:
    #     full_player_name = f'{firstName} {lastName}'
    # else:
    #     full_player_name = f'{lastName}'
    # return full_player_name
    return firstName, lastName


def get_playerSeasons(players_data, player_id):
    """Getting general data about each player"""
    for member in players_data:
        if member.get('realPlayerId') == player_id:
            firstName, lastName = get_player_name(member['realPlayer'])
            position = get_position(member)
            try:
                seasonPrice = member.get('seasonPrice')['price']
            except TypeError:
                seasonPrice = ''
            totalPoints = member.get('totalPoints')
            break
    return firstName, lastName, position, seasonPrice, totalPoints


def get_realTeams(players_data, realTeamId, realTeamId_rival):
    """Getting team name and abbreviation by ID in database"""
    teamName, abbr, teamName_rival, abbr_rival = ['', '', '', '']
    for team in players_data:
        if team.get('id') == realTeamId:
            teamName = team.get('name')
            abbr = team.get('abbr')
        if team.get('id') == realTeamId_rival:
            teamName_rival = team.get('name')
            abbr_rival = team.get('abbr')
    # bug on the fanteam
    abbr = 'AVL' if abbr == 'AV' else abbr
    abbr_rival = 'AVL' if abbr_rival == 'AV' else abbr_rival
    abbr = 'SHU' if abbr == 'SUN' else abbr
    abbr_rival = 'SHU' if abbr_rival == 'SUN' else abbr_rival
    return teamName, abbr, teamName_rival, abbr_rival


def get_realMatches(matches_data, realMatchId, realTeamId):
    """Parsing real match data for a player"""
    for item in matches_data:
        if item.get('id') == realMatchId:
            if item.get('realTeamIds')[0] == realTeamId:
                fieldTeam = 'H'
                realTeamId_rival = item.get('realTeamIds')[1]
            else:
                fieldTeam = 'A'
                realTeamId_rival = item.get('realTeamIds')[0]
            break
        fieldTeam = ''
    return fieldTeam, realTeamId_rival


def format_data(kindOfSport, gw_points, selectedRatio, captainedRatio, totalPoints):
    """Formatting game data"""
    # Formatting by type of sport
    if kindOfSport == 'football' or 'hockey' or 'american_football':
        try:
            totalPoints = '{:.1f}'.format(float(totalPoints) / 100)
            gw_points = '{:.1f}'.format(float(gw_points) / 100)
        except ValueError:
            gw_points = gw_points
            totalPoints = totalPoints

    elif kindOfSport == 'basket':
        try:
            gw_points = '{:.2f}'.format(float(gw_points) / 4)
        except ValueError:
            gw_points = gw_points

    elif kindOfSport == 'baseball':
        try:
            gw_points = '{:.2f}'.format(float(gw_points) / 20)
        except ValueError:
            gw_points = gw_points

    # elif kindOfSport == 'tennis':
    #     try:
    #         gw_points = '{:.2f}'.format(float(gw_points) / 4)
    #     except ValueError:
    #         gw_points = gw_points

    try:
        if float(selectedRatio) != 0:
            selectedRatio = '{:.2f}'.format(float(selectedRatio) * 100)
        else:
            selectedRatio = ''
    except ValueError:
        selectedRatio = selectedRatio

    try:
        if float(captainedRatio) != 0:
            captainedRatio = '{:.2f}'.format(float(captainedRatio) * 100)
        else:
            captainedRatio = ''
    except ValueError:
        captainedRatio = captainedRatio

    return gw_points, selectedRatio, captainedRatio, totalPoints


def get_ownership(realPlayerId, numTourn, gameweek, season_id):
    url = f'{API_URL}/real_players/{realPlayerId}?season_id={season_id}&' + \
        f'round={gameweek}&tournament_id={numTourn}'
    authorization = {'Authorization': 'Bearer fanteam undefined'}
    plarform_player = Parser(url, authorization)
    data_player = plarform_player.parserResult()

    try:
        selectedRatio = data_player[
            'tournamentPlayerStats'].get('selectedRatio')
        captainedRatio = data_player[
            'tournamentPlayerStats'].get('captainedRatio')
    except AttributeError:
        selectedRatio, captainedRatio = ['', '']
    return selectedRatio, captainedRatio


def get_realPlayers(real_players_data, kindOfSport, season_id,
                    gameweek, skipNonPlaying, numTourn, enableNumTourn):
    """The main module for performing all operations of a request
       and writing to a file"""
    print_headline()
    for player in real_players_data['playerRounds']:
        # ***** Main query *****
        realPlayerId = player.get('realPlayerId')
        realMatchId = player.get('realMatchId')
        gw_points = player.get('points')
        minutesPlayed = player.get('minutesPlayed')

        realTeamId = player.get('matchPrice')['realTeamId']
        gw_price = player.get('matchPrice')['price']

        # skipping non-playing players
        if minutesPlayed == 0:
            if skipNonPlaying:
                continue
            else:
                minutesPlayed = ''
                gw_points = ''

        firstName, lastName, position, seasonPrice, totalPoints = get_playerSeasons(
            real_players_data['playerSeasons'], realPlayerId)
        fieldTeam, realTeamId_rival = get_realMatches(
            real_players_data['realMatches'], realMatchId, realTeamId)
        teamName, abbr, teamName_rival, abbr_rival = get_realTeams(
            real_players_data['realTeams'], realTeamId, realTeamId_rival)

        if enableNumTourn:
            selectedRatio, captainedRatio = get_ownership(
                realPlayerId, numTourn, gameweek, season_id)
            print(lastName)
        else:
            selectedRatio, captainedRatio = ['', '']

        gw_points, selectedRatio, captainedRatio, totalPoints = format_data(
            kindOfSport, gw_points, selectedRatio, captainedRatio, totalPoints)

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {'firstName': firstName,
                         'lastName': lastName,
                         'teamName': teamName,
                         'abbr': abbr,
                        #  'teamName_rival': teamName_rival,
                         'abbr_rival': abbr_rival,
                         'position': position,
                         'gw_points': gw_points,
                         'gameweek': gameweek,
                         'gw_price': gw_price,
                         'fieldTeam': fieldTeam,
                         'selectedRatio': selectedRatio,
                         'captainedRatio': captainedRatio,
                         'seasonPrice': seasonPrice,
                         'totalPoints': totalPoints,
                         'minutesPlayed': minutesPlayed, }
        write_csv(data_gameweek)


def get_season():
    url = f'{API_URL}/match_collections?statuses[]=waiting&' + \
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
    return seasons


def main(kindOfSport='football', season_id=387, gameweek=4,
         skipNonPlaying=True, numTourn=176601, enableNumTourn=False):
    """Request information about the players. General request"""
    url = f'{API_URL}/seasons/{season_id}/players?season_id={season_id}&' + \
        f'white_label=fanteam&round={gameweek}'
    # get_realPlayers(get_page_data(get_html(url)), kindOfSport, gameweek)
    authorization = {'Authorization': 'Bearer fanteam undefined'}
    platform = Parser(url, authorization)
    get_realPlayers(platform.parserResult(), kindOfSport, season_id,
                    gameweek, skipNonPlaying, numTourn, enableNumTourn)

if __name__ == '__main__':
    main()
