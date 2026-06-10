import turtle as t   #turtle를 t로 부르겠다 선언
t.shape('turtle')
t.speed(1)
t.width(3) #굵기

for i in range(3):
    t.forward(200)
    t.left(120)

t.done()