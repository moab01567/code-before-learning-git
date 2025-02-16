from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


#Gjør den headless
chrome_options = Options()
chrome_options.add_argument("--window-size=1440,900"); 
#chrome_options.add_argument("--headless");


#chrome_options.add_argument("--headless");
print("Headless")
driver = webdriver.Chrome("/Users/mo/Desktop/chromedriver",options=chrome_options)

driver.implicitly_wait(10)
#åpner siden
def start():
	driver.implicitly_wait(10)
	driver.maximize_window()
	driver.get("https://www.nike.com/no/en/launch/t/offline-stone-mauve")
	time.sleep(4)
	print("åpner side")
	sko()

#velger sko
def sko():
	størrelse = driver.find_elements_by_css_selector("button.size-grid-dropdown.size-grid-button")
	for i in størrelse:
		print(i.text)
		fot = i.text
		if fot == "EU 42.5":
			i.location_once_scrolled_into_view
			i.click()
			print("Sko valgt")
			break

	driver.implicitly_wait(10)

	element = driver.find_element_by_css_selector("button.ncss-btn-primary-dark.btn-lg")
	driver.execute_script("arguments[0].scrollIntoView();", element)
	time.sleep(10)
	driver.element = driver.find_element_by_css_selector("button.ncss-btn-primary-dark.btn-lg").click()
    #her trykker den ikke på knappen til checkout
	time.sleep(1)
	while True:
		try:
			driver.find_element_by_xpath("//button[@class='ncss-btn-primary-dark']").click()
		except:
			print("checkout")
			break
	
	time.sleep(20)
	driver.save_screenshot('/Users/mo/Desktop/finn/bilde.png')
	
	driver.close()


		

start()
