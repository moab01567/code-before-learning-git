from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
import time
import re


class Start():
	def __init__(self):
		self.kjop = Start_up2()
		print("MT4")
		self.driver  = self.kjop.driver
		self.hoved()



	def hoved(self):
		elementer = self.driver.find_elements_by_xpath("//div[@class='page-table grid fixed odd trade-table toolbox-table']//td[@style='text-align: right;']//span[@class='content']")
		liste_text = []
		
		for i in elementer:
			i.text
			liste_text.append(i.text)

		print(liste_text)



							
class Start_up2():
	def __init__(self):
		self.options = Options()  
		#self.options.add_argument("--headless");
		self.options.add_argument("--window-size=1440,900");
		self.options.add_argument('disable-blink-features=AutomationControlled')
		self.options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')

		self.driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options=self.options)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get("https://trade.mql5.com/trade?servers=FusionMarkets-Demo")
		time.sleep(1)
		
		self.login()
		self.fiks_oppsett()

	def login(self):
		try:
			self.driver.find_element_by_xpath("//button[@id='details-button']").click()
			self.driver.find_element_by_xpath("//a[@id='proceed-link']").click()
		except:
			pass
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("34962")
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_xpath("//input[@id='password']").send_keys("Rehman5724")
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_xpath("//select[@id='server']").click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_xpath("//option[@value='FusionMarkets-Demo']").click()
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_xpath("//button[@style='position: absolute; bottom: 10px; width: 80px; left: 135px;']").click()
		time.sleep(10)


	def fiks_oppsett(self):
		self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[1].click()



sta = Start()








