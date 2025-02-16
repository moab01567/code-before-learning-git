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
		#self.chart = Start_up4()
		print("chart")
		self.kjop = Start_up2()
		print("MT4")
		self.hoved()

	def hoved(self):
		while True:
			with open("/Users/mo/Desktop/Chart/info.txt","r") as t:
				forhold = t.read()
			print(forhold)
			try:
				if float(forhold) >= 0.10:
					print("stigende trend")
					trend = "buy"
					trend = False

				elif float(forhold) <= -0.10: 
					print("synkende trend")
					trend = "sell"
					trend = False
				else:
					print("ingen trend")
					trend = True
			except:
				pass

			

			
			
			if not trend:
				time.sleep(0.5)
				print("1")
	
			else:
				sjekk = self.kjop.kjor.sjekk()
				
				if sjekk:
					continue
				else:
					self.kjop.kjor.hoved()
			
	
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
		self.driver.find_element_by_xpath("//input[@name='username']").send_keys("moh0802033@gmail.com")
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
		print(f"EMA200: {to}")

		forhold = float(en) - float(to)
		print(forhold)
		

		if float(forhold) >= 0.4:
			print("stigende trend")
			return "buy"
		elif float(forhold) <= -0.4: 
			print("synkende trend")
			return "sell"
		else:
			print("ingen trades")
			return False
	
	def ref(self):
		self.driver.refresh()
		print("re "*20)
					
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

class kjop2():
	def __init__(self, driver):
		self.driver = driver
	
	def sjekk(self):
		info = self.driver.find_elements_by_xpath("//div[contains(@class,'page-table grid fixed odd trade-table toolbox-table')and not(contains(@style,'display: none;'))]//td[contains(@class,'iconed') and not(contains(@colspan,'10'))]")
		
		if info:
			return True
		else:
			return False
	
	def hoved(self):
		self.s_size()
		self.XAUUSD = self.finn_XAUUSD()
		
		type_ = "buy"
		if type_ == "buy":
			self.dobbel_click(self.XAUUSD)
			self.sell()
			self.dobbel_click(self.XAUUSD)
			self.buy()
		else:
			self.dobbel_click(self.XAUUSD)
			self.buy()
			self.dobbel_click(self.XAUUSD)
			self.sell()

		self.ordre()

	def close(self):
		try:
			print("sjekker om det er noen åpne trades.")
			self.driver.find_element_by_xpath("//span[@class='close']//span").click()
		except:
			print("ingen trades som må lukkes")
			pass

	def s_size(self):
		text = self.driver.find_element_by_xpath("(//td[@class='iconed']//span[@class='content'])[last()]").text
		print(text)
		text_liste = text.split(" ")
		try:
			print(text_liste[1])
		except:
			print("feil på balanse "*10)
			self.s_size()
		
		with open("konto.txt","r") as k:
			g_konto = k.read() 

		with open("0type.txt","r") as t:
			lot = t.read()

		if float(g_konto) > float(f"{text_liste[1]}{text_liste[2]}"):
			with open("0type.txt","w") as t:
				t.write(f"{int(lot) + int(1)}")

		else:
			with open("0type.txt","w") as t:
				t.write("1")

		with open("konto.txt","w") as k:
			k.write(f"{text_liste[1]}{text_liste[2]}")
		
		with open("0type.txt","r") as t:
			lot = t.read()

		size = {"1":"0.01", "2":"0.09", "3":"0.70"}
		s = self.driver.find_element_by_xpath("//input[@max='100']")
		
		for i in range(4):
			s.send_keys(Keys.BACKSPACE)
		

		s.send_keys(size[lot])

	
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
		sp = int(pip_uten) + 300
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
		tp = int(pip_uten) - 400
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
		sp = int(pip_uten) - 300
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
		tp = int(pip_uten) + 400
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

sta = Start()



