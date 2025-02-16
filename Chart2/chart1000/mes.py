from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
import time
import re

class start():
	def __init__(self):
		self.options = Options()  
		self.options.add_argument("--headless");
		self.options.add_argument("--window-size=1440,900");
		self.options.add_argument('disable-blink-features=AutomationControlled')
		self.options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')

		self.driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options=self.options)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get("https://www.messenger.com/")
		print("funnet nettleser")
		print("-"*10)
		print("logger inn....")
		self.login()
		print("innlogging utført :)")
		print("-"*10)
		print("sender test")
		self.test("test")
		print("test utført")
		self.hoved()

	def hoved(self):
		while True:
	
			with open("info1000.txt","r") as f:
				aktiv_trend = f.read()
			print(f"aktiv trend: {aktiv_trend}")
			
			with open("0type.txt","r") as f:
				Gammel_trend = f.read()
			print(f"gammel trend: {Gammel_trend}")


			seconds = time.time()
			local_time = time.ctime(seconds)
			print(local_time)
			time.sleep(0.5)
			
			if aktiv_trend != Gammel_trend:
				print("sender msg"*10)
				try:
					self.test(aktiv_trend)
				except:
					print("vi må refresh'e"*10)
					self.ref()
					continue
				
				with open("0type.txt","w") as w:
					w.write(aktiv_trend)
			
			else:
				continue




	def login(self):
		time.sleep(2)
		self.driver.find_element_by_xpath("//button[@data-cookiebanner='accept_button']").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//input[@type='text']").send_keys("mohemmed.ar2003@gmail.com")
		time.sleep(2)
		self.driver.find_element_by_xpath("//input[@type='password']").send_keys("Rehman5724")
		time.sleep(2)
		self.driver.find_element_by_xpath("//div[@id='close']").click()
		time.sleep(2)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()
		time.sleep(10)

	def test(self, msg):
		self.driver.find_element_by_xpath("//p[@class='kvgmc6g5 oygrvhab']").send_keys(msg)
		time.sleep(1)
		print(f"sender {msg}")
		self.driver.find_element_by_xpath("//div[@aria-label='Trykk på Enter for å sende']").click()
		
	def ref(self):
		self.driver.refresh()
		print("re "*20)
		time.sleep(2)



sta = start()