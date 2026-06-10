class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        a = self.width * self.height
        return a

    def isSquare(self):
        if self.width == self.height:
            return True
        else:
            return False

    def info(self):
        print(f'가로 : {self.width}, 세로 : {self.height}', end="")

rec1 = Rectangle(5,4)
if rec1.isSquare():
    rec1.info()
    print(f', 넓이 : {rec1.area()}, 정사각형')
else:
    rec1.info()
    print(f', 넓이 : {rec1.area()}, 정사각형이 아님')

rec2 = Rectangle(6,6)
if rec2.isSquare():
    rec2.info()
    print(f', 넓이 : {rec2.area()}, 정사각형')
else:
    rec2.info()
    print(f', 넓이 : {rec2.area()}, 정사각형이 아님')