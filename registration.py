from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
import time
import json
from faker import Faker
from helper.registerHelper import registration as regist

file = open("config.json",)
data = json.load(file)
fake = Faker()


#ancours = driver.find_elements_by_tag_name("a")
#for link in ancours:
    #print(link.text())
    #hrefAttribute = link.get_attribute("href")
    #if hrefAttribute == "https://parabank.parasoft.com/parabank/register.htm":
        #link.click()

for i in range(1,10):
    driver = webdriver.Chrome()
    driver.get(data["drivers_config"]["URL"])
    driver.fullscreen_window()
    driver.implicitly_wait(5)
    regist(driver,fake)
    driver.quit()

