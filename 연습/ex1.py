class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def printInfo(self):
        print(f'책 제목: {self.title} / 저자: {self.author} / 가격: {self.price}원')

    def discount(self,rate):
        self.price = self.price*(1-(rate/100))

class EBook(Book):
    def __init__(self,title,author,price,file_size):
        super().__init__(title,author,price)
        self.file_size = file_size

    def printInfo(self):
        print(f'전자책 제목: {self.title} / 저자: {self.author} / 가격: {self.price}원 / 파일크기: {self.file_size}MB')

book1 = Book('파이썬 입문', '김철수',20000)
ebook1 = EBook('데이터 분석','이영희',15000,5)

book1.printInfo()
ebook1.printInfo()