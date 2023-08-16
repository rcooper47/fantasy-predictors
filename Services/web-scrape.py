import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "https://fantasydata.com/nfl/fantasy-football-leaders?position=1&season=2022&seasontype=1&scope=2&subscope=1&startweek=1&endweek=1&aggregatescope=1&range=1"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)


