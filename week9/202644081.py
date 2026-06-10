import turtle
import turtle as t
t.shape("turtle")
t.speed(5)

t.fillcolor('red')
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.penup()
t.goto(0,100)
t.pendown()

t.fillcolor('black')
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

t.penup()
t.goto(10,0)
t.left(120)
t.pendown()

t.fillcolor('brown')
t.begin_fill()
for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()



t.done()
