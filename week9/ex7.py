import turtle as t   #turtle를 t로 부르겠다 선언
t.shape('turtle')
t.speed(10)
t.width(3)

for i in range(10):
    t.circle(100)
    t.forward(50)

t.done()