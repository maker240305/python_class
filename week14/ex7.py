#html 페이지에서 필요한 데이터 가져오기
from bs4 import BeautifulSoup

with open('ht1.html',encoding='utf-8') as f:
    #f를 html.parser로 구분 분석
    soup = BeautifulSoup(f, 'html.parser')

    #필요한 부분 찾기
    result = soup.find_all('div', class_='ABC_class')
    print(result)
