from bs4 import BeautifulSoup
import requests

#보안뉴스 소스코드 가져오기
req = requests.get('https://www.boannews.com/Default.asp')
soup = BeautifulSoup(req.text, 'html.parser')

#id가 headline0인 태그의 자손 중 li 크롤링
title = soup.select('#headline0 li')

#title에서 text 부분만 뽑아서 print
for i in title:
	print(i.text)