#상속 + 오버라이딩(재정의) => 다형성 구현
import math

#부모 클래스
class Shape:
    def area(self):   #자식 클래스에서 반드시 재정의해서 사용!
        raise NotImplementedError('자식클래스에서 재정의하시오')

#자식 클래스
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    #메서드 재정의
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rect = Rectangle(5,3)
cir = Circle(4)

print(rect.area())
print(f'{cir.area():.1f}')