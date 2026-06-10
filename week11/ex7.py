#다형성을 이용한 게임 캐릭터 만들기
#부모 클래스
class Character:
    def __init__(self,name,hp,power):
        self.name = name
        self.hp = hp
        self.power = power

    def status(self):
        print(f'이름:{self.name} | HP:{self.hp} | Power:{self.power}')

    def attack(self):
        print(f'{self.name} 공격! (공격력:{self.power})')

class Warrior(Character):
    def attack(self):
        print(f'{self.name} 검으로 베기! (공격력:{self.power})')

class Mage(Character):
    def attack(self):
        print(f'{self.name} 파이어볼 발사! (공격력:{self.power})')

class Angel(Character):
    def attack(self):
        print(f'{self.name} 하트 공격!! (공격력:{self.power})')

charList = [Warrior('김용사',150,45),
            Mage('마법사최',80,90),
            Angel('이천사',100,70),
            Character('일반인',50,10)]

print('=== 게임 시작 ===')
for char in charList:
    char.status()
    char.attack()
    print()
