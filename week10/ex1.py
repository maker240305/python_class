#객체지향 프로그래밍
#클래스 - 객체를 만들기 위한 설계도와 같다.
#자동차 객체를 만들기 위한 Car 클래스 작성
class Car:
    #자동차 객체의 속성 => 필드(field)
    color = ''
    speed = 0

    #자동차 객체의 기능(동작, 행동) => 메서드(method)
    def upSpeed(self, value):
        #최대 속도를 체크
        self.speed += value
        if self.speed > 250:
            self.speed = 250

    def downSpeed(self, value):
        self.speed -= value
        #최저 속도가 0 미만이 되지 않도록 체크
        if self.speed < 0:
            self.speed = 0

#main code
#클래스를 이용해서 객체 인스턴스 생성
car1 = Car()
car1.color = 'red'
car1.speed = 50
car1.upSpeed(350)
print(f'car1 = {car1.color}, {car1.speed}')

car2 = Car()
car2.color = 'blue'
car2.speed = 100
car2.downSpeed(150)
print(f'car2 = {car2.color}, {car2.speed}')

#car3 만들기 연습 => green, 150
car3 = Car()
car3.color = 'green'
car3.speed = 150
print(f'car3 = {car3.color}, {car3.speed}')
