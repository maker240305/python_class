 #인스턴스 변수와 클래스 변수 비교하기
class Car:
    color = ''    #인스턴스 변수 - 각 객체마다 독립적인 값을 가짐
    speed = 0     #인스턴스 변수
    count = 0     #클래스 변수   - 모든 객체가 공유해서 사용하는 변수

    def __init__(self):
        self.color = 'red'
        self.speed = 50
        Car.count += 1

    def printInfo(self):
        print(f'{self.color} - {self.speed}')

#main code
car1 = Car()
car1.printInfo()
print(f'생성된 자동차는 {Car.count}대')

car2 = Car()
car2.printInfo()
print(f'생성된 자동차는 {Car.count}대')

car3 = Car()
car3.printInfo()
print(f'생성된 자동차는 {Car.count}대')