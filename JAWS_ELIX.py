#this program scraps data from any site given (url)


from selenium import webdriver
from colorama import init, Fore, Style
import time
import datetime
init(autoreset=True)

url = 'https://192.168.7.202/'  #thats the ELIX adress


options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')       #ssl errors ignore
options.add_argument("--disable-dev-shm-usage")         #dev options disable
options.add_argument("--disable-extensions")            #extensions disable
options.add_argument("--disable-notifications")         #notifications disable
options.add_argument('--log-level=3')                   #logging disable
options.add_argument("--headless")                     #call website without openung the window

driver = webdriver.Chrome(chrome_options=options)          #use Chrome as Browser
driver.get(url)                                            #get the url


f = open('Test.txt', 'a')                                                       #open file with name and append / for new file use w
f.writelines("Datum\t" + "\tUhrzeit \ttanklevel in L")                        #write header in file                   

i = 0
while i < 2 :                                                                     #while loop to save data from webpage
    textroh = driver.find_element_by_id('tank-level-litre').text                    #textroh get from page
    textohneLeerzeichen = textroh.replace('\n', '')                                 #delete space in the string
    textohneL = textohneLeerzeichen.replace('L', '')                                #delete L in the sting
    now = datetime.datetime.now()                                                   #define now

    print (Fore.GREEN  + now.strftime("%Y-%m-%d \t%H:%M:%S\t")  + textohneL)      #print the data in the console
    f.writelines(now.strftime("\n%Y-%m-%d \t%H:%M:%S\t") + textohneL)              #write data to txt
    time.sleep(10)                                                                  #wait for 10s
    i +=1                                                                           #count i for next loop
    
f.close()                                                                           #close the file
driver.close()                                                                      #close chrome

#Einbauen: Abbrechen über konsole, IMMER f.close und driver.close!