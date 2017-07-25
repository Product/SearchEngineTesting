from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
testURL = "http://www.naver.com"
searchKeyword = "keyword"

## explicit wait
driver.get(testURL)
inputElem = driver.find_element_by_id('query')
inputElem.send_keys(searchKeyword)
inputElem.send_keys(Keys.RETURN)

submitStartTime = time.time()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, nextIDList[i])))
renderEndTime = time.time()

responseTime = renderEndTime - submitStartTime

## javascript computation

## Browswermob

from browsermobproxy import Server

server = Server("browsermob-proxy")
server.start()
proxy = server.create_proxy()

from selenium import webdriver

profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har("naver")
driver.get("http://www.naver.com")
proxy.har # returns a HAR JSON blob

proxy.stop()
driver.quit()