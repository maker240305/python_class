#다형성 구현 실습
#부모 클래스
class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        return '알 수 없음'

class Dog(Animal):
    def sound(self):
        return'멍멍!'
class Cat(Animal):
    def sound(self):
        return'야용~!'
    def sound(self):
        return'야옹'
class Brid(Animal):
    def sound(self):
        return'캐사'

animalList = [Dog('dog'),Cat('cat'),Brid('brid')]
for animal in animalList:
    print(f'{animal.name}: {animal.sound()}')