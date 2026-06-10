#웹 페이지에 요청을 보내면 응답을 받아 확인하기
from urllib.request import urlopen
from bs4 import BeautifulSoup

a = urlopen('http://www.naver.com')
soup = BeautifulSoup(a.read(), 'html.parser')

print(soup)