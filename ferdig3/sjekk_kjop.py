from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options  
import time
import epost_mot
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
		print("logger in demo2")
		self.demo2 = Start_up2()
		print("logget in demo2")
		print("logger in ekte")
		self.ekte = Start_up3()
		print("logget in ekte")
		print("logger in chart")
		self.chart = Start_up4()
		print("logget in chart")

		self.kjor = Start_program(self, self.driver, self.demo2, self.ekte, self.chart)

	def login(self):
		try:
			self.driver.find_element_by_xpath("//button[@id='details-button']").click()
			self.driver.find_element_by_xpath("//a[@id='proceed-link']").click()
		except:
			pass
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("18996")
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
	def __init__(self, set_up, driver, demo2, ekte, chart):
		self.set_up = set_up
		self.driver = driver
		self.demo2 = demo2
		self.ekte = ekte
		self.chart = chart
		self.lot_list = ["2","3","4","5","6"]
		self.demo1 = Kjop(self.driver)
		self.hoved()

	def hoved(self):
		##første loop
		fortsett = self.sjekker_antall_trades()
		
		##skriver type på fil
		fortsett = self.sjekk_type()
			
		##andre loop
		if fortsett:
			with open(f"valutaer/0_size.txt","r") as s:
				lot = s.read()
			trend = self.chart.sjekk_chart()
			if lot in self.lot_list:
				self.ekte.kjor.hoved(trend)
			else:
				self.demo2.kjor.hoved(trend)

			self.status_sjekk()
		else:
			pass
		##sjekker hvor mye penger hvor mye penger jeg har tjent
		
		#self.ekte.kjor.konto()
		
		##kjøp på nytt to trades
		self.demo1.hoved()

		self.hoved()

	def henter_antall_trades(self):
		while True:
			try:
				self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[0].click()
				element_text_liste = []
				print(element_text_liste)
				liste = self.driver.find_elements_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table') and not(contains(@style,'display: none;'))]//tr[@draggable='true' and not(@class)]//td[contains(@class,'iconed')]//span[@class='content']")
			
				for element_text in liste:
					element_text_liste.append(element_text.text)

				print(element_text_liste)
			except:
				print("meny feil "*20)
				self.driver.refresh()
				try:
					self.set_up.login()
				except:
					pass
				element_text_liste = self.henter_antall_trades()
				return element_text_liste

			return element_text_liste



	def sjekker_antall_trades(self):
		while True:
			info = self.henter_antall_trades()

			if len(info) == 1:
				return True
			elif len(info) == 0:
				return False
			else: 
				time.sleep(1)
				continue


	def sjekk_type(self):
		while True:
			el = self.driver.find_elements_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table') and not(contains(@style,'display: none;'))]//td[not(contains(@style,'text-align: right; display: none;')) and not(contains(@class,'profit')) and not(contains(@class,'iconed'))]//span[@class='content']")
			print(len(el))
			if len(el) <= 3:
				print("ingen aktiv trades")
				return False
			else:

				element_text = []
				for i in el:
					try:
						element_text.append(i.text)
					except:
						continue
				
				print(element_text)
				with open("0type.txt","w") as SB: 
					SB.write(element_text[1])
				return True


	def status_sjekk(self):
		while True:
			with open("status.txt","r") as st:
				status = st.read()
				print(status)
			if status == "aktiv":
				#fjerne alle trades
				try:
					el = self.driver.find_elements_by_xpath("//span[@class='close']//span")
					for i in el:
						i.click()
						time.sleep(1)
					break
				except:
					break 
			else:
				print("fortsatt ikke aktiv")
				time.sleep(1)
				continue

class Kjop():
	def __init__(self, driver):
		self.driver = driver

	def hoved(self):
		self.size()
		self.XAUUSD = self.finn_XAUUSD()
		self.dobbel_click(self.XAUUSD)
		self.sell()
		self.dobbel_click(self.XAUUSD)
		self.buy()

	def size(self):
		self.driver.find_elements_by_xpath("//div[@class='page-tabs bottom lower frame toolbox']//a[@class]")[0].click()

		s = self.driver.find_element_by_xpath("//input[@max='100']")
		for i in range(4):
			s.send_keys(Keys.BACKSPACE)
		
		s.send_keys("0.01")



	def finn_XAUUSD(self):
		valutaer = self.driver.find_elements_by_xpath("//td[@class='symbol']//span[@class='content']")
		print(len(valutaer))
		for i in valutaer:
			print(i.text)
			
			if i.text == " XAUUSD":
				return i
			else:
				continue

	def dobbel_click(self, XAUUSD):
		XAUUSD.click()
		actions = ActionChains(self.driver)
		actions.double_click(XAUUSD).perform()
		time.sleep(0.5)

	def ok_knapp(self):
		try:
			ok_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 324px; left: 330px; width: 396px;']")
			ok_button.click()
		except:
			print("feil på ok "*20)
			time.sleep(1)
			self.ok_knapp()

	def sell(self):
		"""fikser pips"""
		try:
			sellpips = self.driver.find_elements_by_xpath("//div[@class='page-text']//span[@style]")
			print(sellpips[0])
			print(sellpips[0].text)
			sellpips = sellpips[0].text
		except:
			print("Feilsell "*20)
			true=self.sell()
			return True
			#sellpips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#sellpips = sellpips[0].text
			#print("ERROR pips sell")

		pip = f"{sellpips}"
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

		"""kanpper"""
		sell_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; left: 330px; width: 187px;']")
		sell_button.click()
		time.sleep(0.5)

		self.ok_knapp()

	def buy(self):
		"""fikser pips"""
		try:
			buypips = self.driver.find_elements_by_xpath("//div[@class='page-text']//span[@style]")
			buypips = buypips[3].text
		except:
			print("buyFeil"*20)
			true = self.buy()
			return True
			#buypips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#buypips = buypips[2].text
			#print("ERROR pips buy")


		pip = f"{buypips}"
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

		"""knapper"""
		buy_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; right: 30px; width: 187px;']")
		buy_button.click()
		time.sleep(0.5)

		self.ok_knapp()


	def ordre(self):
		pass
	
class Start_up2():
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
		
		self.kjor = kjop2(self.driver)

	def login(self):
		try:
			self.driver.find_element_by_xpath("//button[@id='details-button']").click()
			self.driver.find_element_by_xpath("//a[@id='proceed-link']").click()
		except:
			pass
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("18997")
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

class kjop2():
	def __init__(self, driver):
		self.driver = driver
	
	def hoved(self, trend):
		self.s_size()
		self.XAUUSD = self.finn_XAUUSD()
		
		with open(f"0type.txt","r") as SB:
			type_ = SB.read()
		

		if type_ == trend:
			print("ikke samme trend")
			return "ingen trade"
		else:
			if "sell" == type_:
				self.dobbel_click(self.XAUUSD)
				self.sell()
			else:
				self.dobbel_click(self.XAUUSD)
				self.buy()
		
		self.ordre()

	def s_size(self):
		s = self.driver.find_element_by_xpath("//input[@max='100']")
		
		for i in range(4):
			s.send_keys(Keys.BACKSPACE)
		
		s.send_keys("0.01")

	
	def finn_XAUUSD(self):
		valutaer = self.driver.find_elements_by_xpath("//td[@class='symbol']//span[@class='content']")
		print(len(valutaer))
		for i in valutaer:
			print(i.text)
			
			if i.text == " XAUUSD":
				return i
			else:
				continue

	def dobbel_click(self, XAUUSD):
		XAUUSD.click()
		actions = ActionChains(self.driver)
		actions.double_click(XAUUSD).perform()
		time.sleep(0.5)

	def ok_knapp(self):
		try:
			ok_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 324px; left: 330px; width: 396px;']")
			ok_button.click()
		except:
			print("feil på ok "*20)
			time.sleep(1)
			self.ok_knapp()

	def sell(self):
		"""fikser pips"""
		try:
			sellpips = self.driver.find_elements_by_xpath("//div[@class='page-text']//span[@style]")
			print(sellpips[0])
			print(sellpips[0].text)
			sellpips = sellpips[0].text
		except:
			print("Feilsell "*20)
			true=self.sell()
			return True
			#sellpips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#sellpips = sellpips[0].text
			#print("ERROR pips sell")

		pip = f"{sellpips}"
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
		sp = int(pip_uten) + 100
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
		tp = int(pip_uten) - 200
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

		"""kanpper"""
		sell_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; left: 330px; width: 187px;']")
		sell_button.click()
		time.sleep(0.5)

		self.ok_knapp()

	def buy(self):
		"""fikser pips"""
		try:
			buypips = self.driver.find_elements_by_xpath("//div[@class='page-text']//span[@style]")
			buypips = buypips[3].text
		except:
			print("buyFeil"*20)
			true = self.buy()
			return True
			#buypips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#buypips = buypips[2].text
			#print("ERROR pips buy")


		pip = f"{buypips}"
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
		sp = int(pip_uten) - 100
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
		tp = int(pip_uten) + 200
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

		"""knapper"""
		buy_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; right: 30px; width: 187px;']")
		buy_button.click()
		time.sleep(0.5)

		self.ok_knapp()


	def ordre(self):
		with open("status2.txt","w") as w:
			w.write("aktiv")
		with open("status.txt","w") as w2:
			w2.write("ikke aktiv")
		
class Start_up3():
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
		
		self.kjor = kjop3(self.driver)

	def login(self):
		try:
			self.driver.find_element_by_xpath("//button[@id='details-button']").click()
			self.driver.find_element_by_xpath("//a[@id='proceed-link']").click()
		except:
			pass
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("18998")
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

class kjop3():
	def __init__(self, driver):
		self.driver = driver
	
	def hoved(self, trend):
		self.s_size()
		self.XAUUSD = self.finn_XAUUSD()
		
		with open(f"0type.txt","r") as SB:
			type_ = SB.read()
		

		if type_ == trend:
			print("ikke samme trend")
			return "ingen trade"
		else:
			if "sell" == type_:
				self.dobbel_click(self.XAUUSD)
				self.sell()
			else:
				self.dobbel_click(self.XAUUSD)
				self.buy()
		
		self.ordre()
		

	def s_size(self):
		size = {'2': '0.01', '3': '0.02','4': '0.04', '5': '0.09', '6': '0.01', '7': '0.01', '8': '0.01', '9': '0.01', "10":"0.01", "11": '0.01',"12":"0.01", "12": '0.01',"13":"0.01", '14': '0.01',"15":"0.01", "17": "0.01","18":"0.01", "19": "0.01","20":"0.01"}
		with open(f"valutaer/0_size.txt","r") as r:
			sz = r.read()

		s = self.driver.find_element_by_xpath("//input[@max='100']")
		
		for i in range(4):
			s.send_keys(Keys.BACKSPACE)
		
		s.send_keys(size[sz])

	
	def finn_XAUUSD(self):
		valutaer = self.driver.find_elements_by_xpath("//td[@class='symbol']//span[@class='content']")
		print(len(valutaer))
		for i in valutaer:
			print(i.text)
			
			if i.text == " XAUUSD":
				return i
			else:
				continue

	def dobbel_click(self, XAUUSD):
		XAUUSD.click()
		actions = ActionChains(self.driver)
		actions.double_click(XAUUSD).perform()
		time.sleep(0.5)

	def ok_knapp(self):
		try:
			ok_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 324px; left: 330px; width: 396px;']")
			ok_button.click()
		except:
			print("feil på ok "*20)
			time.sleep(1)
			self.ok_knapp()

	def sell(self):
		"""fikser pips"""
		try:
			sellpips = self.driver.find_elements_by_xpath("//div[@class='page-text']//span[@style]")
			print(sellpips[0])
			print(sellpips[0].text)
			sellpips = sellpips[0].text
		except:
			print("Feilsell "*20)
			true=self.sell()
			return True
			#sellpips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#sellpips = sellpips[0].text
			#print("ERROR pips sell")

		pip = f"{sellpips}"
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
		sp = int(pip_uten) + 100
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
		tp = int(pip_uten) - 200
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

		"""kanpper"""
		sell_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; left: 330px; width: 187px;']")
		sell_button.click()
		time.sleep(0.5)

		self.ok_knapp()

	def buy(self):
		"""fikser pips"""
		try:
			buypips = self.driver.find_elements_by_xpath("//div[@class='page-text']//span[@style]")
			buypips = buypips[3].text
		except:
			print("buyFeil"*20)
			true = self.buy()
			return True
			#buypips = self.driver.find_elements_by_xpath("//span[@style='font-size:24px;letter-spacing:1px;']")
			#buypips = buypips[2].text
			#print("ERROR pips buy")


		pip = f"{buypips}"
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
		sp = int(pip_uten) - 100
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
		tp = int(pip_uten) + 200
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

		"""knapper"""
		buy_button = self.driver.find_element_by_xpath("//button[@style='position: absolute; top: 244px; right: 30px; width: 187px;']")
		buy_button.click()
		time.sleep(0.5)

		self.ok_knapp()


	def ordre(self):
		with open("status3.txt","w") as w:
			w.write("aktiv")
		with open("status.txt","w") as w2:
			w2.write("ikke aktiv")

	def konto(self):
		with open("konto.txt","r") as k:
			org_konto = k.read()
		
		#balance
		element = self.driver.find_element_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table')and not(contains(@style,'display: none;'))]//tbody//td[contains(@class,'iconed')]//span[contains(@class,'content')]").text
		element_list = element.split(" ")
		print(element_list)
		overskudd = float(element_list[1]) - float(org_konto)

		if overskudd > 2000.00:
			self.driver.close()
			quit()
		else:pass

class Start_up4():
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
		time.sleep(10)
		self.login()

	def login(self):
		self.driver.find_element_by_xpath("//a[@class='tv-header__link tv-header__link--signin js-header__signin']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//span[@class='tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//input[@name='username']").send_keys("moh0802032@gmail.com")
		time.sleep(1)
		self.driver.find_element_by_xpath("//input[@name='password']").send_keys("Rehman5724")
		time.sleep(1)
		self.driver.find_element_by_xpath("//button[@type='submit']").click()
		time.sleep(1)
		self.driver.find_element_by_xpath("//a[@data-type='chart']").click()
		time.sleep(2)

	def sjekk_chart(self):
		en = self.driver.find_element_by_xpath("//div[@style='color: rgb(255, 235, 59);']").text
		print(f"EMA9: {en}")
		to = self.driver.find_element_by_xpath("//div[@style='color: rgb(33, 150, 243);']").text
		print(f"EMA: {to}")

		if float(en) > float(to):
			print("stigende trend")
			return "buy"
		elif float(en) == float(to): 
			return "ingen trade"
		else:
			print("synkende trend")
			return "sell"
		
start = Start_up()


