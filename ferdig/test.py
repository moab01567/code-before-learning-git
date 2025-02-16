from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
import time
import epost_mot
import re

options1 = Options()  
#options1.add_argument("--headless");
options1.add_argument("--window-size=1440,900");
options1.add_argument('disable-blink-features=AutomationControlled')
options1.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')
options1.add_argument("--no-sandbox");

driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options= options1)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.tradingview.com/")
time.sleep(1)
##login
driver.find_element_by_xpath("//a[@class='tv-header__link tv-header__link--signin js-header__signin']").click()
time.sleep(1)
driver.find_element_by_xpath("//span[@class='tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@name='username']").send_keys("moh0802@hotmail.com")
time.sleep(1)
driver.find_element_by_xpath("//input[@name='password']").send_keys("Rehman5724")
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@data-type='chart']").click()
time.sleep(2)

##info henter


en = driver.find_element_by_xpath("//div[@style='color: rgb(255, 235, 59);']").text
print(en)
to = driver.find_element_by_xpath("//div[@style='color: rgb(33, 150, 243);']").text
print(to)
