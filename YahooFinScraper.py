import pandas as pd
from selenium import webdriver
import time

Companies = pd.read_csv('Tickers Not FOund.csv')


tickers = Companies['ticker'].tolist()

#print(tickers)


URL = "https://finance.yahoo.com/"
driver = webdriver.Chrome(executable_path = r"/home/sanket8898/Desktop/WebDriver/chromedriver")

driver.get(URL)
time.sleep(10)
ct = 1
for instrument in tickers:
	if(ct<13):
		ct = ct+1
		continue
	print(instrument)
	driver.find_element_by_xpath("//input[@placeholder = 'Search for news, symbols or companies']").send_keys(instrument)
	time.sleep(10)
	driver.find_element_by_xpath("//button[@id= 'header-desktop-search-button']").click()
	time.sleep(20)
	driver.find_element_by_xpath("//span[text() = 'Historical Data']").click()
	time.sleep(20)
	driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/div[1]/div/div/div").click()
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='dropdown-menu']/div/ul[2]/li[4]/button").click()
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[1]/div[1]/button").click()
	time.sleep(20)
	for i in range(0,25):
	 	driver.execute_script("window.scrollBy(0,5000)")
	 	time.sleep(2)





	webpage = driver.page_source

	from bs4 import BeautifulSoup

	HTMLPage = BeautifulSoup(driver.page_source, 'html.parser')

	Table = HTMLPage.find('table', class_='W(100%) M(0)')


	Rows = Table.find_all('tr', class_='BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')

	extracted_data = []
	
	for i in range(0, len(Rows)):
	 try:
	  
	  RowDict = {}
	  
	  Values = Rows[i].find_all('td')
	  
	 
	  if len(Values) == 7:
	   RowDict["Date"] = Values[0].find('span').text.replace(',', '')
	   RowDict["Open"] = Values[1].find('span').text.replace(',', '')
	   RowDict["High"] = Values[2].find('span').text.replace(',', '')
	   RowDict["Low"] = Values[3].find('span').text.replace(',', '')
	   RowDict["Close"] = Values[4].find('span').text.replace(',', '')
	   RowDict["Adj Close"] = Values[5].find('span').text.replace(',', '')
	   RowDict["Volume"] = Values[6].find('span').text.replace(',', '')
	
	   extracted_data.append(RowDict)
	 except:
	  
	  print("Row Number: " + str(i))
	 finally:
	  
	  i = i + 1

	extracted_data = pd.DataFrame(extracted_data)
	print(extracted_data)
	symb = instrument+".csv"
	extracted_data.to_csv(symb)







