import turtle as t   #turtle를 t로 부르겠다 선언
t.shape('turtle')
t.speed(1)

for i in range(4):
    t.forward(200)
    t.left(90)

t.done()