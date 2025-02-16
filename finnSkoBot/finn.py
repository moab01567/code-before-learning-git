from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
import time

class Start_up():
	def __init__(self):
		self.options = Options()  
		#self.options.add_argument("--headless");
		self.options.add_argument("--window-size=1440,900");
		self.options.add_argument('disable-blink-features=AutomationControlled')
		self.options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')

		self.driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options=self.options)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get("https://my.salita.no/nb/no/s/home")

		epost = self.driver.find_element_by_xpath("//input[@id='emailId']").send_keys("Fatmatolk@hotmail.com")
		passord	= self.driver.find_element_by_xpath("//input[@id='passwordId']").send_keys("2018Dagbladet2018")

		self.driver.find_element_by_xpath("//button[@class='sk-btn sk-btn--default']").click()
		self.hoved()
		time.sleep(3)

	def hoved(self):
		while True:
			alle = self.driver.find_elements_by_xpath("//section[@class='assignment is-progress-bar assignment__yellow-status']")

			for i in range(len(alle)):
				try:
					self.driver.find_elements_by_xpath("//section[@class='assignment is-progress-bar assignment__yellow-status']")[i].click()
				except:
					continue
				time.sleep(3)
				pris = self.driver.find_elements_by_xpath("//p[@class='invoice-info__line-amount'] | //p[@class='regular-apply__standard-price']")[-1].text
				print(pris)
				pris = pris.replace(" ","")
				pris = pris.replace("NOK","")
				if float(pris) > 600:
					self.bekreft()
					self.driver.back()
					time.sleep(3)
					break
					
				else:
					self.driver.back()
					time.sleep(3)

			self.driver.refresh()
			time.sleep(3)
			print("oppdater")
	
	def bekreft(self):
		self.driver.find_element_by_xpath("//button[@class='sk-btn sk-btn--default pt-apply__apply-btn'] | //button[@class='sk-btn sk-btn--default regular-apply__apply-btn']").click()
		check = self.driver.find_elements_by_xpath("//span[@class='sk-checkbox__imitation']")
		for i in check:
			i.click()
		
		self.driver.find_element_by_xpath("//button[@class='sk-btn sk-btn--default assign-apply__btn']").click()

hei = Start_up()

