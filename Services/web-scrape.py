import nfl_data_py as nfl
import pandas 
import river
import gymnasium as gym
import itertools

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
playerArray: ["ryan", "zhane", ..."name"...]
scoreArray: Weekly scores [100, 99, 120] need function to build
rewards: [0,0,0,1] possibly
}

1. get all 3 positions (names)
2. run thru function
3. eliminate all that don't meet criteria : exactly 1 qb, 2-3 rbs, 2-3 wrs, 1-2 te (if more than min num of 1 pos, other pos must be min)

"""
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
    all_possible_combos = itertools.combinations(player_names, 7)
    return list(all_possible_combos)

def main(df):
    df = get_skill_pos(df)
    df = fumble_combiner(df)
    df = reg_season_combiner(df)
    all_names = get_all_names(df)
    all_combos = build_all_combos(all_names)
    return len(all_combos)

#print(nfl.import_weekly_data([2022]).position.unique())
print(main(nfl.import_weekly_data([2022])))
#print(player_searcher(stats, "Tom Brady"))
### Write tests
