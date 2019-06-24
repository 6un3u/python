from urllib import parse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait(driver, selector, name):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((selector, name))
        )        
    except TimeoutException:
        print('Time Out')
        
def search_engine(url) :
    shop = []
    driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
    driver.get(url)
    wait(driver, By.CSS_SELECTOR, '.section-listbox')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sh = soup.select('h3.section-result-title > span')
    driver.quit()

    for i in sh:
        shop.append(i.text)
    
    return shop

s = input('검색어를 입력하세요 : ')
# 구글은 url 파라미터로 검색어를 넘기는 방식
# 입력값에 url인코딩을 적용해서 url 값으로 입력
url = 'https://www.google.co.kr/maps/search/' + parse.quote(s)
shop = search_engine(url)   

for i in shop:
    print(i)