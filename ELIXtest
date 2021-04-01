#this program scraps data from any site given (url)


from selenium import webdriver
from colorama import init, Fore, Style
import time
init(autoreset=True)
url = 'https://de.wikipedia.org/wiki/Wikipedia:Hauptseite'
#url = 'https://192.168.7.202/' #thats the ELIX I want to go to in the end


options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors') #ssl errors ignore
options.add_argument("--disable-dev-shm-usage") #dev options disable
options.add_argument("--disable-extensions") #extensions disable
options.add_argument("--disable-notifications") #notifications disable
options.add_argument('--log-level=3') #logging disable
#options.add_argument("--headless") #call website without openung the window

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

element = driver.find_element_by_id('n-help')

print (Fore.GREEN + "test123")
print (Fore.RED + "hier kommt der Wert rein (element) ist aber noch ein WebElement und kein str")

time.sleep(5)

driver.close()
