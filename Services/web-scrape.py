import requests 
from bs4 import BeautifulSoup
import nfl_data_py as nfl
import pandas 
URL = "https://api.sportsdata.io/api/nfl/fantasy/json/Standings/2022REG"
page = requests.get(URL)

stats = nfl.import_weekly_data([2022,2021])
# [id, name, week, f-score, stat1, stat2, avg-pts-agst,..., ]

head = stats.head(100)

#head.to_excel('output.xlsx', index=False)

### Combine fumbles lost columns
def fumble_combiner(df):
    df["fumbles_lost"] = df["sack_fumbles_lost"] + df["rushing_fumbles_lost"] + df["receiving_fumbles_lost"]
    return df

"""
^^^ SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead
"""

def reg_season_combiner(df):
    regseason = stats[stats['season_type']== "REG"]
    return regseason

def remove_kickers(df):
    no_kickers = stats[stats['position'] != "SPEC"]
    return no_kickers

def player_searcher(df, name):
    player_stats = stats[stats['player_display_name'] == name]
    return player_stats

def main(df):
    df = fumble_combiner(df)
    df = reg_season_combiner(df)
    df = remove_kickers(df)
    return df

print(player_searcher(stats, "Tom Brady"))
### Write tests
