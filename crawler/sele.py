from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
#자원이 모두 로드될 때 까지 최대 3초까지 대기
driver.implicitly_wait(3)
driver.get('https://google.com')