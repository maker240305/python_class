#도형자판기
import turtle as t
t.shape("turtle")
t.speed(5)

n = int(input('만들고 싶은 도형은? '))
count = int(input('도형을 몇 개 만들까요? '))
length = int(input('각 변의 길이는? '))
width = int(input('선의 굵기는? '))
color = input('채우기 색상은? ')
backcolor = input('배경색은? ')

t.bgcolor(backcolor)
t.width(width)

for i in range(count):
    t.clear()

    t.begin_fill()
    t.fillcolor(color)
    #도형 그리기
    for j in range(n):
        t.forward(length)
        t.left(360/n)
    t.end_fill()

t.done()