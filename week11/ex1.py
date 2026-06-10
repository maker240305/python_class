#책체지향 프로그래밍 - 상속과 다형성 구현
#상속 - 부모 클래스의 속성과 기능을 물려받아 사용하는 것
#부모 클래스 선언
class Vehicle:
    #속성값 - field
    make = ''
    model = ''
    color = ''
    price = 0

    #속성값 초기화 - 생성자 이용
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price

    #메서드
    def getDesc(self):
        print(f'차량 정보: {self.make}, {self.model}, {self.color}, {self.price}만원')

    def setMake(self,make):
        self.make = make

    def setModel(self,model):
        self.model = model

    def setPrice(self,price):
        self.price = price

#자식 클래스 선언
class Truck(Vehicle):
    payload = 0

    def __init__(self,make,model,color,price,payload):
        #부모클래스 필드는 부모생성자를 이용해서 초기화
        super().__init__(make,model,color,price)
        self.payload = payload

#main code
#자식 클래스로 인스턴스 객체 생성
tr1 = Truck('Tesla','cyber truck','white','15000',2000)
tr1.getDesc()
tr1.setMake('현대자동차')
tr1.setModel('포터')
tr1.setPrice(3000)
tr1.getDesc()