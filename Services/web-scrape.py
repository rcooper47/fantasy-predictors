import requests 
from bs4 import BeautifulSoup
import nfl_data_py as nfl

URL = "https://api.sportsdata.io/api/nfl/fantasy/json/Standings/2022REG"
page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")
#class_name = "k-grid k-widget k-display-block k-grid-lockedcolumns"

#results = soup.find("div", class_="k-grid k-widget k-display-block k-grid-lockedcolumns")

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get(URL)
#players = driver.find_elements_by_xpath('//td[@class="k-grid k-widget k-display-block k-grid-lockedcolumns"]')
#content = driver.find_element(By.CLASS_NAME, class_name)
stats = nfl.import_weekly_data([2022,2021])

print(stats)

