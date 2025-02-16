from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
#import ordre_endring
		#2102345019 #2102345186
		#7zfltui	#b7bkriv
		#2102357931 #fvaf1rc
		#2102365268 #fad1vow		
		#2102374935 #d1ciuyu

class Start_up():
	def __init__(self, ids):
		options = Options()  
		options.add_argument("--headless");
		options.add_argument("--window-size=1440,900");
		options.add_argument('disable-blink-features=AutomationControlled')
		options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36');

		self.driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options=options)
		self.login()
		self.fiks_oppsett()
		trade = Start_trading(self.driver, ids)


	def login(self):
		'''logger inn'''
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.driver.get("https://trade.mql5.com/trade?servers=FusionMarkets-Demo")
		time.sleep(1)
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("19847")
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

		fx_crosses = self.driver.find_elements_by_xpath("//div[@class='item first parent']//div[@class='item collapsed parent']")[0].click()
		time.sleep(1)
		show = self.driver.find_element_by_xpath("//button[@style='position: absolute; right: 8px; width: 84px; top: 8px;']").click()
		time.sleep(1)

		close = self.driver.find_element_by_xpath("//button[@style='position: absolute; right: 8px; width: 84px; bottom: 8px;']").click()
		time.sleep(1)

		"""setter på gebyr"""
		self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[1].click()
		time.sleep(1)
		right_click = self.driver.find_element_by_xpath("//tr[@class='total']")
		actionChains = ActionChains(self.driver)
		actionChains.context_click(right_click).perform()
		time.sleep(1)

		self.driver.find_element_by_xpath("//div[@class='first item parent selected']//div[@class='item parent']").click()
		time.sleep(1)
		self.driver.find_elements_by_xpath("//div[@class='item parent selected']//span[@class='box']//div[@class='item']")[0].click()
		time.sleep(5)
		self.driver.find_element_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[(@class)]").click()
		time.sleep(1)

class Start_trading():
	def __init__(self, driver, ids):
		self.driver = driver
		self.ids = ids
		self.hoved()


	def hoved(self,):
		info = self.hent_info()
		valuta_elementer = self.driver.find_elements_by_xpath("//td[@class='symbol']//span[@class='content']")
		
		for valuta in valuta_elementer:

			if valuta.text in info:
				self.size("0.01")
				self.sell(valuta)
				self.buy(valuta)
				self.ordre()
			else: continue

		self.driver.close()


	def size(self, s):
		size = self.driver.find_element_by_xpath("//input[@max='100']")
		for i in range(4):
			size.send_keys(Keys.BACKSPACE)
		size.send_keys(s)

		time.sleep(2)
		

	def ordre(self):
		try:
			self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[0].click()
			ordre_nummer = self.driver.find_elements_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table') and not(contains(@style,'display: none;'))]//tr[@draggable='true' and not(@class)]//td[contains(@class,'iconed')]//span[@class='content']")
			ordre_nummer = ordre_nummer[-2::]
			ordre_fil = open(f"{self.ids}.txt", "w")
			ordre_fil.write(f"{ordre_nummer[0].text}{ordre_nummer[1].text}")
			ordre_fil.close()
		except:
			print("ordre_skriving_feil "*20)
			self.ordre()
			return None

	def pipbuy(self):
		"""fikser pips"""
		try:
			buypips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			buypips = buypips[2].text
		except:
			print("buyFeil"*20)
			true = self.pipbuy()
			return True
			#buypips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#buypips = buypips[2].text
			#print("ERROR pips buy")
		
		try:
			buypip = self.driver.find_elements_by_xpath("//span[@style='font-size:20px;letter-spacing:1px;']")
			buypip = buypip[1].text
		except:
			print("buyFeil"*20)
			true=self.pipbuy()
			return True
			#buypip = self.driver.find_elements_by_xpath("//span[@style='font-size:20px;letter-spacing:1px;']")
			#buypip = buypip[1].text
			#print("ERROR pip buy")


		pip = f"{buypips}{buypip}"
		print(pip)
		legg_til_null = ""
		if pip[0] == "0":
			legg_til_null = "0"

		antall_pip = len(pip)
		pip_uten = ""
		for posisjon in range(antall_pip):
			if pip[posisjon] == ".":
				punktum_pos = posisjon
				print(f"punktum posisjon: {posisjon}")
				continue
			else:
				pip_uten = f"{pip_uten}{pip[posisjon]}"

		print(pip_uten)

		
		"""regn ut sl"""
		sp = int(pip_uten) - 150
		sp = f"{legg_til_null}{sp}"
		print(sp)

		antall_pip_uten = len(sp)
		ny_pip_sp = ""
		for posisjon in range(antall_pip_uten):
			if posisjon == punktum_pos:
				ny_pip_sp = f"{ny_pip_sp}.{sp[posisjon]}"
				continue
			else:
				ny_pip_sp = f"{ny_pip_sp}{sp[posisjon]}"
		print(ny_pip_sp)


		"""regn ut tp"""
		tp = int(pip_uten) + 270
		tp =  f"{legg_til_null}{tp}"
		print(tp)

		antall_pip_uten = len(tp)
		ny_pip_tp = ""
		for posisjon in range(antall_pip_uten):
			if posisjon == punktum_pos:
				ny_pip_tp = f"{ny_pip_tp}.{tp[posisjon]}"
				continue
			else:
				ny_pip_tp = f"{ny_pip_tp}{tp[posisjon]}"


		"""utfører pip skriving"""
		time.sleep(0.5)
		sp_input = self.driver.find_element_by_xpath("//div[@style='position: absolute; left: 410px; width: 100px; top: 82px;']//input[@min='0']")
		tp_input = self.driver.find_element_by_xpath("//div[@style='position: absolute; width: 100px; top: 82px; right: 23px;']//input[@min='0']")
		print("----------")
		print(pip_uten)
		print(ny_pip_sp)
		print(ny_pip_tp)
		print("----------")
		for i in range(7):
			sp_input.send_keys(Keys.BACKSPACE)
		
		sp_input.send_keys(ny_pip_sp)

		for i in range(7):
			tp_input.send_keys(Keys.BACKSPACE)
		
		tp_input.send_keys(ny_pip_tp)

		return True

	def buy(self,valuta):
		"""kjøper valutaen"""
		actions = ActionChains(self.driver)
		actions.double_click(valuta).perform()
		time.sleep(0.5)

		true = self.pipbuy()

		buy_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; right: 30px; width: 187px;']")
		buy_button.click()
		time.sleep(0.5)

		ok_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 324px; left: 330px; width: 396px;']")
		ok_button.click()

	def pipsell(self):
		"""fikser pips"""
		try:
			sellpips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			print(sellpips[0])
			print(sellpips[0].text)
			sellpips = sellpips[0].text
		except:
			print("Feilsell "*20)
			true=self.pipsell()
			return True
			#sellpips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#sellpips = sellpips[0].text
			#print("ERROR pips sell")

		try:
			sellpip = self.driver.find_elements_by_xpath("//span[@style='font-size:20px;letter-spacing:1px;']")
			sellpip = sellpip[0].text
		except:
			print("Feilsell "*20)
			true=self.pipsell()
			return True
			#sellpip = self.driver.find_elements_by_xpath("//span[@style='font-size:20px;letter-spacing:1px;']")
			#sellpip = sellpip[0].text
			#print("ERROR pip sell")

		pip = f"{sellpips}{sellpip}"
		print(pip)
		legg_til_null = ""
		
		if pip[0] == "0":
			legg_til_null = "0"

		antall_pip = len(pip)
		pip_uten = ""
		for posisjon in range(antall_pip):
			if pip[posisjon] == ".":
				punktum_pos = posisjon
				print(f"punktum posisjon: {posisjon}")
				continue
			else:
				pip_uten = f"{pip_uten}{pip[posisjon]}"

		print(pip_uten)

		"""regn ut sl"""
		sp = int(pip_uten) + 150
		sp = f"{legg_til_null}{sp}"
		print(sp)

		antall_pip_uten = len(sp)
		ny_pip_sp = ""
		for posisjon in range(antall_pip_uten):
			if posisjon == punktum_pos:
				ny_pip_sp = f"{ny_pip_sp}.{sp[posisjon]}"
				continue
			else:
				ny_pip_sp = f"{ny_pip_sp}{sp[posisjon]}"
		print(ny_pip_sp)
		
		"""regn ut tp"""
		tp = int(pip_uten) - 270
		tp =  f"{legg_til_null}{tp}"

		antall_pip_uten = len(tp)
		ny_pip_tp = ""
		for posisjon in range(antall_pip_uten):
			if posisjon == punktum_pos:
				ny_pip_tp = f"{ny_pip_tp}.{tp[posisjon]}"
				continue
			else:
				ny_pip_tp = f"{ny_pip_tp}{tp[posisjon]}"


		"""utfører pip skriving"""
		time.sleep(0.5)
		sp_input = self.driver.find_element_by_xpath("//div[@style='position: absolute; left: 410px; width: 100px; top: 82px;']//input[@min='0']")
		tp_input = self.driver.find_element_by_xpath("//div[@style='position: absolute; width: 100px; top: 82px; right: 23px;']//input[@min='0']")
		
		print("----------")
		print(pip_uten)
		print(ny_pip_sp)
		print(ny_pip_tp)
		print("----------")
		for i in range(7):
			sp_input.send_keys(Keys.BACKSPACE)
		
		sp_input.send_keys(ny_pip_sp)

		for i in range(7):
			tp_input.send_keys(Keys.BACKSPACE)
		
		tp_input.send_keys(ny_pip_tp)

		return True



	def sell(self, valuta):
		"""seller valutaen"""
		actions = ActionChains(self.driver)
		actions.double_click(valuta).perform()
		time.sleep(0.5)
		
		true = self.pipsell()

		sell_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; left: 330px; width: 187px;']")
		sell_button.click()
		time.sleep(0.5)

		ok_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 324px; left: 330px; width: 396px;']")
		ok_button.click()



	def utfør(self, info):
		"""sjekker om spread'en er verdt å trade med"""
		trade_valuta = []
		for valuta, bid, ask, spread in info:
			if int(spread) <= 1000:
				trade_valuta.append(valuta)
			else:
				continue

		print('trade med disse valutaene')
		print(trade_valuta)
		print()

		return trade_valuta


	

	def hent_info(self):	
		time.sleep(5)
		info = self.driver.find_elements_by_xpath("//td[@class='symbol']//span[@class='content']")
		print(len(info))
		#valuta = [' AUDUSD',' EURUSD',' GBPUSD',' NZDUSD', ' USDCAD',' USDCHF',' USDJPY',' AUDCAD', ' AUDJPY',' CADJPY', ' CHFJPY', ' EURCHF', ' EURGBP', ' EURJPY', ' NZDCAD', ' NZDCHF', ' NZDJPY']
		info_list = [" GBPUSD"]	
	

		print()
		print('hent_info')
		print(info_list)
		print()
		return info_list



















