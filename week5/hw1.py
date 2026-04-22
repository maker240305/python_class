def circle_area(v1):
    res = (v1**2) * 3.14
    return res

def circle_length(v1):
    res = 2*v1*3.14
    return res

while True:
    r = float(input('원의 반지름을 입력하세요 >> '))
    if r < 1:
        print('프로그램 종료')
        break
    else:
        s = circle_area(r)
        length = circle_length(r)
        print('반지름이', r ,'인 원의 넓이는', round(s,1) ,'이고, 둘레의 길이는', round(length,1), '입니다.')