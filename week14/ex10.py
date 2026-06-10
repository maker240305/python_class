#도서 정보 분석하기
from bs4 import BeautifulSoup

with open('books.html',encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

    #가장 비싼 도서 찾기
    max_price = 0
    max_title = ''

    books = soup.find_all('div',class_='book')
    for book in books:
        title = book.find('h2',class_='title').text
        author = book.find('p',class_='author').text
        price = int(book.find('p',class_='price').text)

        print(f'{title} / {author} / {price:,}원')

        #가장 비싼 도서 비교
        if price > max_price:
            max_price = price
            max_title = title

    print()
    print(f'가장 비싼 도서 : {max_title} / {max_price:,}원')