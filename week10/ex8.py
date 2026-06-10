#Pet 클래스를
class Pet:
    kind = ''
    legs = 0
    sound = ''

    def __init__(self, kind, legs):
        self.kind = kind
        self.legs = legs

    #울음소리 저장
    def setSound(self, sound):
        self.sound = sound

    def printPet(self):
        print(f'다리가 {self.legs}개인 {self.kind}가 {self.sound}~')

#main code
dog = Pet('강아지',4)
dog.setSound('멍멍')
dog.printPet()

cat = Pet('고양이',4)
cat.setSound('야옹')
cat.printPet()

bird = Pet('참새',2)
bird.setSound('짹짹')
bird.printPet()
