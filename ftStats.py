# -*- coding: utf-8 -*-
import csv
import sys
from modules.parser import Parser

API_URL = 'https://fanteam-game.api.scoutgg.net'


def write_csv(data):
    """Write data in csv file"""
    # for terminal and .exe in Windows
    pathFile = ['FtStats.csv']

    # for app in Mac OS
    # pathFile = ['/'.join(sys.argv[0].split('/')[:-4]), '/FtStats.csv']
    with open(''.join(pathFile), 'a', encoding='utf-8') as file:
        order = ['firstName',
                 'lastName',
                 'team_name',
                 'abbr',
                 'position',
                 'gw_points',
                 'gw_price',
                 'homeTeam',
                 'gameweek', ]
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


def run_once(f):
    def wrapper(*args, **kwargs):
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
                     'team_name': 'Team',
                     'abbr': 'Abbr',
                     'position': 'Pos',
                     'homeTeam': 'St',
                     'gw_points': 'Points',
                     'gw_price': 'Cost',
                     'gameweek': 'Gw'}
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
            break
    return firstName, lastName, position


def get_realTeams(players_data, realTeamId):
    """Getting team name and abbreviation by ID in database"""
    for team in players_data:
        if team.get('id') == realTeamId:
            team_name = team.get('name')
            abbr = team.get('abbr')
            break
        team_name, abbr = ['', '']
    return team_name, abbr


def get_realMatches(matches_data, realMatchId, realTeamId):
    """Parsing real match data for a player"""
    for item in matches_data:
        if item.get('id') == realMatchId:
            if item.get('realTeamIds')[0] == realTeamId:
                homeTeam = 'H'
            else:
                homeTeam = 'A'
            break
        homeTeam = ''
    return homeTeam


def format_data(kindOfSport, gw_points):
    """Formatting game data"""
    # Formatting by type of sport
    if kindOfSport == 'football':
        try:
            gw_points = '{:.0f}'.format(float(gw_points) / 100)
        except ValueError:
            gw_points = gw_points

    elif kindOfSport == 'hockey':
        try:
            gw_points = '{:.1f}'.format(float(gw_points) / 10)
        except ValueError:
            gw_points = gw_points

    elif kindOfSport == 'basket':
        try:
            gw_points = '{:.2f}'.format(float(gw_points) / 4)
        except ValueError:
            gw_points = gw_points

    elif kindOfSport == 'baseball':
        try:
            gw_points = '{:.1f}'.format(float(gw_points) / 20)
        except ValueError:
            gw_points = gw_points

    return gw_points


def get_realPlayers(real_players_data, kindOfSport, gameweek):
    """The main module for performing all operations of a request
       and writing to a file"""
    print_headline()
    for player in real_players_data['playerRounds']:
        # ***** Main query *****
        realPlayerId = player.get('realPlayerId')
        realTeamId = player.get('matchPrice')['realTeamId']
        realMatchId = player.get('matchPrice')['realMatchId']
        gw_points = player.get('points')
        minutesPlayed = player.get('minutesPlayed')
        gw_price = player.get('matchPrice')['price']

        # skipping non-playing players
        if minutesPlayed == 0:
            continue

        firstName, lastName, position = get_playerSeasons(
            real_players_data['playerSeasons'], realPlayerId)
        team_name, abbr = get_realTeams(
            real_players_data['realTeams'], realTeamId)
        homeTeam = get_realMatches(
            real_players_data['realMatches'], realMatchId, realTeamId)

        gw_points = format_data(kindOfSport, gw_points)

        # print(full_player_name)

        # Gameweek data dictionary. Data generation and writing to file
        data_gameweek = {'firstName': firstName,
                         'lastName': lastName,
                         'team_name': team_name,
                         'abbr': abbr,
                         'position': position,
                         'gw_points': gw_points,
                         'gameweek': gameweek,
                         'gw_price': gw_price,
                         'homeTeam': homeTeam}
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


def main(kindOfSport='football', season_id=234, gameweek=38):
    """Request information about the players. General request"""
    url = f'{API_URL}/seasons/{season_id}/players?season_id={season_id}&' + \
        f'white_label=fanteam&round={gameweek}'
    # get_realPlayers(get_page_data(get_html(url)), kindOfSport, gameweek)
    authorization = {'Authorization': 'Bearer fanteam undefined'}
    platform = Parser(url, authorization)
    get_realPlayers(platform.parserResult(), kindOfSport, gameweek)

if __name__ == '__main__':
    main()
