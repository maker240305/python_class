#생성자 메서드를 이용해서 필드값을 초기화
class Car:
    color = ''
    speed = 0

    #생성자 이용 => 객체 생성 시 자동으로 실행
    def __init__(self):
        self.color = 'red'
        self.speed = 50

#main code
#인스턴스 생성
mycar = Car()
print(f'mycar = {mycar.color}, {mycar.speed}')

yourcar = Car()
print(f'yourcar = {yourcar.color}, {yourcar.speed}')