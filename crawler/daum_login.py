from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\smddu\Documents\chromedriver\chromedriver.exe')
#모든 자원이 로드될 때 까지 기다리는 시간을 직접 설정
driver.implicitly_wait(3)

driver.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F')

driver.find_element_by_name('id').send_keys('user_id')
driver.find_element_by_name('pw').send_keys('user_pw')

driver.find_element_by_id('loginBtn').click()
