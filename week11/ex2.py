#상속 실습
#부모 클래스 선언
class Animal:
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age

    def eat(self):
        print(f'동물이 먹고 있습니다.')

    def info(self):
        print(f'{self.kind} 이름은 {self.name}이고 {self.age}개월')

#자식 클래스 선언
class Dog(Animal):
    def __init__(self, kind, name, age, place):
        super().__init__(kind, name, age)
        self.place = place

    #추가로 필요한 메서드 선언
    def dogLife(self):
        print(f'{self.place} 동물')

    #메서드 재정의(오버라이딩, overriding)
    def eat(self):
        print('강아지가 먹고 있습니다.')

class Whale(Animal):
    def __init__(self, kind, name, age, place):
        super().__init__(kind, name, age)
        self.place = place

    def eat(self):                  #오버라이딩
        print('고래가 먹고 있습니다.')

    def whaleLife(self):
        print(f'{self.place} 동물')

dog = Dog('강아지','초코',6,'육지')
dolphin = Whale('고래','돌핀',11,'바다')

dog.info()
dog.dogLife()
dog.eat()

print()

dolphin.info()
dolphin.whaleLife()
dolphin.eat()