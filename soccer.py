import numpy
import pandas
import sqlite3
import math

path = "C://Users//nicob//OneDrive//Dokumenter//Skole greier//Maskinlæring//"
database = path + 'database.sqlite'

conn = sqlite3.connect(database)

def get_match():
    match = pandas.read_sql("""SELECT * FROM Match WHERE id = 14722;""", conn)
    return match

def get_home_and_away_team_overall_player_rating_sum(match, all_players):
    match_date = match['date'][0]
    home_player_ids = numpy.array(match[['home_player_1',
                                         'home_player_2',
                                         'home_player_3',
                                         'home_player_4',
                                         'home_player_5',
                                         'home_player_6',
                                         'home_player_7',
                                         'home_player_8',
                                         'home_player_9',
                                         'home_player_10',
                                         'home_player_11']])
    away_player_ids = numpy.array(match[['away_player_1',
                                         'away_player_2',
                                         'away_player_3',
                                         'away_player_4',
                                         'away_player_5',
                                         'away_player_6',
                                         'away_player_7',
                                         'away_player_8',
                                         'away_player_9',
                                         'away_player_10',
                                         'away_player_11']])
    all_players = pandas.read_sql("""SELECT * FROM Player_Attributes;""", conn)
    sum_home_rating = 0
    sum_away_rating = 0

    for home_player_id in home_player_ids[0]:
        home_player = all_players[(all_players['player_api_id'] == home_player_id)]
        try:
            home_player_last_match = home_player[home_player.date <= match_date].sort_values(by='date', ascending=False).iloc[0]
            sum_home_rating += home_player_last_match['overall_rating']
        except:
            index = home_player.shape[0] - 1
            bad_index = True
            while bad_index:
                if math.isnan(home_player['overall_rating'].iloc[index]):
                    index = index-1
                else:
                    bad_index = False
            sum_home_rating += home_player['overall_rating'].iloc[index]

    for away_player_id in away_player_ids[0]:
        away_player = all_players[(all_players['player_api_id'] == away_player_id)]
        try:
            away_player_last_match = away_player[away_player.date <= match_date].sort_values(by='date', ascending=False).iloc[0]
            sum_away_rating += away_player_last_match['overall_rating']
        except:
            index = away_player.shape[0] - 1
            bad_index = True
            while bad_index:
                if math.isnan(away_player['overall_rating'].iloc[index]):
                    index = index - 1
                else:
                    bad_index = False
            sum_away_rating += away_player['overall_rating'].iloc[index]

    return [sum_home_rating, sum_away_rating]


match = get_match()
sum_ratings = get_home_and_away_team_overall_player_rating_sum(match=match)
print(sum_ratings)


