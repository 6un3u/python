from selenium import webdriver
from bs4 import BeautifulSoup
c = 1
txt = input('검색어를 입력하세요 : ')

driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://map.naver.com/')
driver.find_element_by_id('search-input').send_keys(txt)
driver.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
shop = soup.select('.lst_site dt > a')

for i in shop:
	print(i.text)