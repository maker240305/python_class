#매개변수가 있는 생성자를 이용
class Dog:
    name = ''
    age = 0
    color = ''

    #매개변수가 있는 생성자
    def __init__(self,name,age,color): #name이 같아 보여도 필드의 name은 self를 붙여야 되므로 구분가능
        self.name = name
        self.age = age
        self.color = color
    #객체의 공통된 기능도 메서드로 등록
    def printInfo(self):
        print(f'우리집 강아지는 {self.age}개월 된 {self.name}입니다.')
        print(f'색상은 {self.color}입니다.')


#main code
puddle = Dog('푸들',8,'brown')
maltese = Dog('보리',12,'while')

puddle.printInfo()
maltese.printInfo()