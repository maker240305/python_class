#뉴스 제목 수집하기
from bs4 import BeautifulSoup

with open('news.html',encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

    news_list = soup.find_all('li', class_='news')
    #print(news_list)
    for news in news_list:
        print(news.text)