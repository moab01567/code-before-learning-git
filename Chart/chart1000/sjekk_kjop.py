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
		print("chart")
		self.kjop = Start_up2()
		print("MT4")
		self.hoved()

	def hoved(self):
		while True:
			with open("/Users/mo/Desktop/Chart/chart1000/info1000.txt","r") as t:
				LS = t.read()
			print(LS)
			seconds = time.time()
			local_time = time.ctime(seconds)
			print(local_time)
			
			with open("0type.txt","r") as t:
				type_ = t.read()

			try:
				if LS != type_:
					print("ny trend")
					trend_type = LS
					trend = True
				else:
					print("samme trend")
					trend = False
			except:
				pass

			
			if not trend:
				time.sleep(5)
				print("seep 5 sek")
	
			else:
				with open("0type.txt","w") as t:
					t.write(trend_type)
				
				self.kjop.kjor.hoved(trend_type)
			
			
							
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
		
		self.kjor = kjop2(self.driver)

	def login(self):
		try:
			self.driver.find_element_by_xpath("//button[@id='details-button']").click()
			self.driver.find_element_by_xpath("//a[@id='proceed-link']").click()
		except:
			pass
		self.driver.find_element_by_xpath("//input[@id='login']").send_keys("34958")
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
	
	def hoved(self, type_):
		self.sjekk()
		#self.pip = self.s_size()
		self.XAUUSD = self.finn_XAUUSD()
		
		if type_ == "buy":
			self.dobbel_click(self.XAUUSD)
			self.buy()
		else:
			self.dobbel_click(self.XAUUSD)
			self.sell()
	


	def sjekk(self):
		info = self.driver.find_elements_by_xpath("//span[@class='close']//span")
		
		if info:
			info[0].click() 
			print("lukker trade")
			time.sleep(5)
			self.sjekk()
		else:
			print("fant ingen åpne trades")
			pass
	
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

		n_konto = text_liste[1]

		#stopper program etter et tap. 
		#with open("start_konto.txt","r") as sk:
		#	start_k = sk.read()

		#print(f"start konto: {start_k}")
		#print(f"noverende konto: {n_konto}")
		#tap = f"{float(n_konto) - float(start_k)}"
		#if float(tap) < float(-13):
		#	quit()
		#else: 
		#	pass




		with open("konto.txt","r") as k:
			g_konto = k.read()

		print(f"g_konto: {g_konto}")
		print(f"n_konto: {n_konto}")

		omsetninger = f"{float(n_konto) - float(g_konto)}"
		print(f"omsetininger: {omsetninger}")

		if float(omsetninger) < 0:
			omsetninger1 = omsetninger[1:]
		else: 
			omsetninger1 = omsetninger
			pass


		if float(omsetninger) > 0:
			with open("konto.txt","w") as k:
				k.write(f"{n_konto}")
			pip = "200"
		
		else:
			pip = f"{(float(omsetninger1)*100) + 200}" 

		print(pip)

		return pip 

	
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
		try:
			XAUUSD.click()
			actions = ActionChains(self.driver)
			actions.double_click(XAUUSD).perform()
			time.sleep(0.5)
		except:
			self.driver.refresh()
			time.sleep(5)
			XAUUSD = self.finn_XAUUSD()
			self.double_click(XAUUSD)

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
			self.sell()
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
		sp = int(pip_uten) + 500
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
		tp = int(pip_uten) - 500
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
		tp_input = self.driver.find_element_by_xpath("//div[@style='position: absolute; width: 100px; top: 82px; right: 23px;']//input[@min='0']")
		sp_input = self.driver.find_element_by_xpath("//div[@style='position: absolute; left: 410px; width: 100px; top: 82px;']//input[@min='0']")
		
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
			self.buy()
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
		sp = int(pip_uten) - 500
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
		tp = int(pip_uten) + 500
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


sta = Start()



