#Car 클래스를 이용한 자동차 주행 프로그램
class Car:
    company = ''
    model = ''
    fuel = 0

    #생성자
    def __init__(self,company,model):
        self.company = company
        self.model = model

    #연료 체크
    def fuelCheck(self):
        if self.fuel > 0:
            return True
        else:
            return False

    #자동차 주행 메서드
    def run(self):
        self.fuel -= 10
        print(f'{self.model}가 달립니다(남은연료={self.fuel})')

#main code
mycar = Car('현대자동차','각그랜저')
mycar.fuel = 50
print('출발합니다~!')

while True:
    if mycar.fuelCheck():
        mycar.run()
    else:
        #연료가 다 소진되면 다시 연료를 입력
        #print('연료를 넣으세요.')
        inFuel = int(input('연료를 넣으세요 >> '))

        #입력된 값이 0이면 프로그램 종료
        if inFuel == 0:
            break

        mycar.fuel = inFuel

print(f'{mycar.model}가 멈춥니다.')