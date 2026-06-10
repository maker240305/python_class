#생성자의 매개변수로 속성(필드) 값을 초기화
class Car:
    color = ''
    speed = 0

    def __init__(self,value1,value2):
        self.color = value1
        self.speed = value2

#main code
#매개변수가 있는 생성자를 이용해서 인스턴스 객체 생성
mycar = Car('red', 150)
print(f'mycar = {mycar.color}, {mycar.speed}')

yourcar = Car('blue', 100)
print(f'yourcar = {yourcar.color}, {yourcar.speed}')