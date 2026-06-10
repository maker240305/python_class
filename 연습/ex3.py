class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def status(self):
        print(f'이름: {self.name} / HP: {self.hp} / 공격력: {self.power}')

    def attack(self):
        print(f'{self.name}이(가) 기본 공격을 합니다. 공격력: {self.power}')

class Warrior(Character):
    def attack(self):
        print(f'{self.name}이(가) 검으로 공격합니다. 공격력: {self.power}')

class Mage(Character):
    def __init__(self, name, hp, power,mana):
        super().__init__(name,hp,power)
        self.mana = mana

    def status(self):
        print(f'이름: {self.name} / HP: {self.hp} / 공격력: {self.power} / 마나: {self.mana}')

    def attack(self):
        print(f'{self.name}이(가) 마법 공격을 합니다. 공격력: {self.power}')


char1 = Character('일반캐릭터',100,20)
warrior1 = Warrior('전사',150,40)
mage1 = Mage('마법사',80,70,100)

charList = [char1,warrior1,mage1]
for char in charList:
    char.status()
    char.attack()


