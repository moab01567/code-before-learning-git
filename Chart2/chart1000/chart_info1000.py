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
		self.options = Options()  
		self.options.add_argument("--headless");
		self.options.add_argument("--window-size=1440,900");
		self.options.add_argument('disable-blink-features=AutomationControlled')
		self.options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')

		self.driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options=self.options)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get("https://www.tradingview.com/")
		self.login()
		time.sleep(10)
		#self.sjekk_chart()


	def login(self):
		self.driver.find_element_by_xpath("//button[@aria-haspopup='true']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//div[@data-name='header-user-menu-sign-in']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//span[@class='tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//input[@name='username']").send_keys("moh0802032@gmail.com")
		time.sleep(1)
		self.driver.find_element_by_xpath("//input[@name='password']").send_keys("Rehman5724")
		time.sleep(1)
		submit = self.driver.find_element_by_xpath("//button[@type='submit']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//a[@data-main-menu-root-track-id='chart']").click()
		time.sleep(5)

	def sjekk_chart(self): 
		antall = 0
		while True:
			if antall >= 100:
				self.ref()
				antall = 0
			else:
				pass
			
			signal = self.QQE_signal()
			#MACD_trend = self.MACD()

			if signal == "SHORT":
				with open("info1000.txt","w") as f:
					f.write("sell")
			else:
				with open("info1000.txt","w") as f:
					f.write("buy")
				pass
				
			
			antall = antall +1
	
	def QQE_signal(self):
		try:
			longe = self.driver.find_elements_by_xpath("//div[@style='color: rgb(76, 175, 80);']")
			if longe:
				signal = "LONG"
				print("QQE_signal: LONG")
				time.sleep(2)
			else:
				signal = "SHORT"
				print("QQE_signal: SHORT")
				time.sleep(2)

			return signal 
		except:
			self.ref()

	def MACD(self):
		tall = self.driver.find_element_by_xpath("//div[@style='color: rgb(103, 58, 183);'] | //div[@style='color: rgb(255, 235, 59);']").text
		print(f"MACD ligger på {tall}")
		
		try:
			float(tall)
		except:
			tall = "-" + tall[1::]

		if float(tall) <= float(-0.3):
			print("MACD: SHORT")
			MACD_trend = "SHORT"
		elif float(tall) >= float(0.3):
			print("MACD: LONG")
			MACD_trend = "LONG"
		else:
			print("MACD: ingen")
			MACD_trend = "ingen"

		return MACD_trend
	

	def ref(self):
		self.driver.refresh()
		print("re "*20)
		time.sleep(10)
			



startt = Start()
