from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')

driver.implicitly_wait(3)

driver.get('http://www.megabox.co.kr/?menuId=theater')
driver.find_element_by_css_selector('.menu01').click()

soup = BeautifulSoup(driver.page_source, 'html.parser')
theater = soup.select('ul#region_10 a')

for i in theater:
	print(i.text)