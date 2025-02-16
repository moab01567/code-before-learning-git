from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
import time
import re

class Start_up():
	def __init__(self):
		self.options = Options()  
		self.options.add_argument("--headless");
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
		self.kjor = Start_program(self, self.driver)

	def login(self):
		try:
			self.driver.find_element_by_xpath("//button[@id='details-button']").click()
			self.driver.find_element_by_xpath("//a[@id='proceed-link']").click()
		except:	
			pass
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("19437")
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
		'''akseptere one click sell/buy'''
		try:
			self.driver.find_element_by_xpath("//div[@class='but']").click()
		except:
			self.driver.refresh()
			time.sleep(10)
			self.fiks_oppsett()
			return None
		
		time.sleep(1)
		self.driver.find_element_by_xpath("//input[@id='one-click-accept']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//button[@style='position: absolute; bottom: 10px; right: 96px; width: 80px;']").click()
		time.sleep(1)


		"""legger til alle valuta parene"""
		right_click = self.driver.find_element_by_xpath("//td[@class='symbol']//span[@class='content']")
		actionChains = ActionChains(self.driver)
		actionChains.context_click(right_click).perform()
		time.sleep(1)
		symbol_meny = self.driver.find_elements_by_xpath("//div[@class='page-menu context expanded']//div[@class='item iconed']")[3].click()
		time.sleep(1)
		
		fx_crosses = self.driver.find_elements_by_xpath("//div[@class='item first parent']//div[@class='item collapsed parent']")[4].click()
		time.sleep(1)
		show = self.driver.find_element_by_xpath("//button[@style='position: absolute; right: 8px; width: 84px; top: 8px;']").click()
		time.sleep(1)

		close = self.driver.find_element_by_xpath("//button[@style='position: absolute; right: 8px; width: 84px; bottom: 8px;']").click()
		time.sleep(1)
		

class Start_program():
	def __init__(self, start, driver):
		self.start = start
		self.driver = driver
		
		self.hoved()


	def hoved(self):
		self.status()
		self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[0].click()
		resultat = self.sjekk_trade()
		self.size(resultat)

		self.hoved()

	def status(self):
		while True:
			with open("status2.txt","r") as r:
				status = r.read()

				if status == "aktiv":
					print("status: aktiv")
					right_click = self.driver.find_element_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table') and not(contains(@style,'display: none;'))]//tr[@draggable='true']")
					actionChains = ActionChains(self.driver)
					actionChains.context_click(right_click).perform()
					time.sleep(1)

					self.driver.find_element_by_xpath("//div[@class='first item parent selected']//div[@class='item parent']").click()
					time.sleep(1)
					self.driver.find_elements_by_xpath("//div[@class='item parent selected']//div")[1].click()
					break
				else:
					print("status: ikke aktiv")
					time.sleep(5)
					continue

	def henter_info(self): 
		try:
			element_text_liste = []
			print(element_text_liste)
			liste = self.driver.find_elements_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table') and not(contains(@style,'display: none;'))]//td[@style='text-align: right;']")
			
			for element_text in liste:
				element_text_liste.append(element_text.text)

			print(element_text_liste)
		except:
			print("meny feil "*20)
			element_text_liste = self.henter_info()
			
			return element_text_liste

		return element_text_liste

	def sjekk_trade(self):
		while True:
			info = self.henter_info()
			if len(info) < 3:
				return resultat
			else:
				resultat = info[-1]
				print(f"resultatet er {resultat}")

			if float(info[-1]) >= float(100.00):
				try:
					self.driver.find_element_by_xpath("//span[@class='close']//span").click()
					return resultat
				except:
					return resultat
			else:
				print(info)
				time.sleep(1)
		
	def size(self, resultat):

		self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[0].click()
		
		if resultat[0] == "-":
			
			with open(f"valutaer/0_size.txt", "r") as SB:
				Glot_key = SB.read()

			Nlot_key = int(Glot_key) + 1 

			with open(f"valutaer/0_size.txt","w") as s:
				s.write(f"{Nlot_key}")
		
		else:
			with open(f"valutaer/0_size.txt","w") as s:
				s.write("1")

		
		with open("status.txt","w") as w:
			w.write("aktiv")
		with open("status2.txt","w") as w2:
			w2.write("ikke aktiv")



startssss = Start_up()















