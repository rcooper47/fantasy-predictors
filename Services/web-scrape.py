import nfl_data_py as nfl
import pandas 
import river
import gymnasium as gym
import itertools
import regex as re
import random

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

def validation_tester(input_str):
    # pass al tests return true, else return false
    qbs = re.findall("qb", input_str)
    rbs = re.findall("rb", input_str)
    wrs = re.findall("wr", input_str)
    tes = re.findall("te", input_str)
    if len(qbs) == 1:
        pass
    else:
        return False
    
    if len(rbs) >= 2 and len(rbs) <= 4:
        pass
    else:
        return False
    if len(wrs) >= 2 and len(wrs) <= 4:
        pass
    else:
        return False
    if len(tes) >= 1 and len(tes) <= 3:
        pass
    else:
        return False
    
    return True
    
# print(validation_tester("qb"*1+"wr"*3+"rb"*2+"te"))  
    #return bool(re.search("^(?!.*\bqb\b.*\bqb\b).*\bqb\b.*$","qbqb"))
## build output dict & give lineups id
## retrieve scores from dataframe & put into output dict
def remove_invalid_combos(all_combos, df):
    # if is flex modifier then can be flex or their pos
    valid_lineups = []
    for tup in all_combos:
        validation_str = ""
        for player in tup:
            position = df.loc[df['player_display_name'] == player]['position'].iloc[0]
            validation_str += position
        print(validation_str)
        if validation_tester(validation_str) == True:
            valid_lineups.append(tup)
    return valid_lineups
def create_output_dict(valid_lineups, df):
    """Build dictionary of team combos

{
teamId: 1
playerArray: ["ryan", "zhane", ..."name"...] players to play that week
scoreArray: Weekly scores [100, 99, 120] players' summed scores for each week
rewards: [0,0,0,1] possibly
}"""
    output_dict = {idNum: lineup for idNum, lineup in enumerate(valid_lineups)}
    #scores_dict = {idNum: player['fantasy_points'] for idNum, lineup in enumerate(valid_lineups) for player in lineup}
    return output_dict

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
    all_possible_combos = itertools.combinations(player_names, 8)
    return list(all_possible_combos)



def choose_best_team(input):
    return 

def main(df):
    df = get_skill_pos(df)
    df = fumble_combiner(df)
    df = reg_season_combiner(df)
    all_names = get_all_names(df)
    name_list = random.choices(list(all_names), k=30)
    all_combos = build_all_combos(name_list)
    print(all_combos[:30])
    valid_lineups = remove_invalid_combos(all_combos[:11], df)
    print(valid_lineups)
    return create_output_dict(valid_lineups, df)
df = nfl.import_weekly_data([2020])

print(main(df))
# Option 1: Allow for all players
# Option 2: Allow for only 1 roster worth of players -> 
#print(nfl.import_weekly_data([2022]).position.unique())
#print(main(nfl.import_weekly_data([2022])))
#print(player_searcher(stats, "Tom Brady"))
### Write tests
