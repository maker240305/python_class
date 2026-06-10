import turtle as t   #turtle를 t로 부르겠다 선언
t.shape('turtle')
t.speed(2)

n = int(input("몇 각형을 그릴까요?: "))

for i in range(n):
    t.forward(100)
    t.left(360/n)

t.done()