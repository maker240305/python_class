#메서드 재정의 실습 - 오버라이딩
#부모 클래스
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def getDesc(self):
        print(f'{self.model}, {self.color}')

class SportsCar(Car):
    def __init__(self, model, color, turbo):
        super().__init__(model, color)
        self.turbo = turbo

    #오버라이딩
    def getDesc(self):
        print(f'내 차 정보 : {self.model}, {self.color}, 터보자동차')

mycar = SportsCar('제네시스쿠페', 'red',True)
mycar.getDesc()