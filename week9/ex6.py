#선으로 연결되지 않은 사각형, 삼각형 그리기
import turtle as t   #turtle를 t로 부르겠다 선언
t.shape('turtle')
t.speed(2)

#사각형 그리기
for i in range(4):
    t.forward(150)
    t.left(90)

#선 없이 이동
t.penup()
t.goto(200,0)
t.pendown()

#삼각형 그리기
for i in range(3):
    t.forward(150)
    t.left(120)

t.done()