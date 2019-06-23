import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
response = requests.get(url)
source = response.content

parser = BeautifulSoup(source, "html.parser")
navigator = parser.find_all("a",{"class":"title"})

for a in navigator:
	print(a.text)
