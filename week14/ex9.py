#상품 정보 추출하기
from bs4 import BeautifulSoup

with open('products.html',encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

    products = soup.find_all('div', class_='product')
    for product in products:
        name = product.find('span', class_='name').text
        price = product.find('span', class_='price').text
        print(f'{name} : {int(price):,} 원')