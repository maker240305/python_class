def circle_area(v1):
    a=v1 * v1 * 3.14
    return a

def circle_length(v1):
    a = (v1 * 2 )* 3.14
    return a


while True:
    r = int(input('원의 반지름:'))
    if r < 1:
        break
    print(f'반지름이 {r}인 원의 넓이는 {circle_area(r)}이고, 둘레의 길이는 {circle_length(r):.1f}입니다.')