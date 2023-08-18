import requests 
from bs4 import BeautifulSoup
import nfl_data_py as nfl
import pandas 
URL = "https://api.sportsdata.io/api/nfl/fantasy/json/Standings/2022REG"
page = requests.get(URL)

stats = nfl.import_weekly_data([2022,2021])
# [id, name, week, f-score, stat1, stat2, avg-pts-agst,..., ]

head = stats.head(100)

head.to_excel('output.xlsx', index=False)

### Combine fumbles lost columns
def fumble_combiner(df):
    df["fumbles_lost"] = df["sack_fumbles_lost"] + df["rushing_fumbles_lost"] +df["receiving_fumbles_lost"]
    return df
### Write tests
