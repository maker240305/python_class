class Animal:
    def __init__(self,name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def introduce(self):
        print(f'저는 동물입니다.')

    def sound(self):
        print(f'{self.name} : 소리')

    def info(self):
        print(f'이름 : {self.name} | 나이 : {self.age}살 | 서직지 : {self.habitat}')
#자식 클래스
class lion(Animal):
    #메서드 재정의
    def introduce(self):
        print(f'저는 사자 {self.name}입니다. 정글의 왕이에요. {self.age}살')

    def sound(self):
        print(f'{self.name} : 으르럼!!!')

class pen(Animal):
    def introduce(self):
        print(f'저는 펭귄 {self.name}입니다. 수영을 잘해요. {self.age}살')
    def sound(self):
        print(f'{self.name} : 꽥꽥')

class co(Animal):
    def introduce(self):
        print(f'저는 코끼리 {self.name}입니다. 코가 길어요. {self.age}살')
    def sound(self):
        print(f'{self.name} : 뿌~~')

lion1 = lion('심바',5,'사바나')
pen1 = pen('뽀로로', 3,'남극')
co1 = co('코코',12,'열대우림')
lion1.info()
lion1.introduce()
lion1.sound()
print()
pen1.info()
pen1.introduce()
pen1.sound()
print()
co1.info()
co1.introduce()
co1.sound()


