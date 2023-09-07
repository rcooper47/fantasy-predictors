import nfl_data_py as nfl
import pandas 
import river
import gymnasium as gym
import itertools
import regex as re

# [id, name, week, f-score, stat1, stat2, avg-pts-agst,..., ]

#head = stats.head(100)




#head.to_excel('output.xlsx', index=False)
# maybe to enforce position limits only plug same positions with their limits into the alg
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
    regseason = df[df['season_type']== "REG"]
    return regseason

def remove_kickers(df):
    no_kickers = df[df['position'] != "SPEC"]
    return no_kickers

def player_searcher(df, name):
    player_stats = df[df['player_display_name'] == name]
    return player_stats
# {"QB","RB","RB","WR","TE","FLX"}
# {"QB","RB","WR","WR","TE","FLX"} Positional Pattern
"""
Build dictionary of team combos

{
teamId: 1
playerArray: ["ryan", "zhane", ..."name"...] players to play that week
scoreArray: Weekly scores [100, 99, 120] players' summed scores for each week
rewards: [0,0,0,1] possibly
}


1. get all 3 positions (names)
2. run thru function
3. eliminate all that don't meet criteria : exactly 1 qb, 2-3 rbs, 2-3 wrs, 1-2 te (if more than min num of 1 pos, other pos must be min)

Player Object:
Will have to search using our shit to get pos & pointArray

[
  [  
    {
        name: ryan
        position: qb
        pointArray: [1]
    }
    ,
        {
        name: ryan
        position: qb
        pointArray: [1]
    }
,
]
,
]
 "if valid return 1 else 0"
    "qbrbrbwrwrwrte"
    "qbrbrbwrwrrbte"
    "qbrbrbwrwrtete"
"    3. eliminate all that don't meet criteria : exactly 1 qb, 2-3 rbs, 2-3 wrs, 1-2 te (if more than min num of 1 pos, other pos must be min)"

"""

def validation_tester():
    return bool(re.search("qb{1}","qb"))

def remove_invalid_combos(all_combos):
    # if is flex modifier then can be flex or their pos
    valid_lineups = []
    for tup in all_combos:
        validation_str = ""
        for player in tup:
            validation_str += player["position"]
        if validation_tester(validation_str) == 1:
            valid_lineups.append(tup)
    return valid_lineups

def get_skill_pos(df):
    qbs = df[df['position'] == 'QB']
    wrs = df[df['position'] == 'WR']
    rbs = df[df['position'] == 'RB']
    tes = df[df['position'] == 'TE']
    return qbs._append([wrs, rbs, tes])

def get_all_names(df):
    player_names = df.player_display_name.unique()
    return player_names

def build_all_combos(player_names):
    """make all combos"""
    all_possible_combos = itertools.combinations(player_names, 7)
    return list(all_possible_combos)



def choose_best_team(input):
    return 

def main(df):
    df = get_skill_pos(df)
    df = fumble_combiner(df)
    df = reg_season_combiner(df)
    all_names = get_all_names(df)
    all_combos = build_all_combos(all_names)
    return len(all_combos)
# Option 1: Allow for all players
# Option 2: Allow for only 1 roster worth of players -> 
#print(nfl.import_weekly_data([2022]).position.unique())
#print(main(nfl.import_weekly_data([2022])))
#print(player_searcher(stats, "Tom Brady"))
### Write tests
print(validation_tester())