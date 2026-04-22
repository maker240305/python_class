#함수
def coffee_machine(coffee):
    print('#1.뜨거운 물 준비')
    print('#2.컵 준비')
    if coffee == 1:
        print('#3.아메리카노 준비')
    elif coffee == 2:
        print('#3.라떼 준비')
    elif coffee == 3:
        print('#3.모카 준비')
    elif coffee == 4:
        print('#3.카푸치노 준비')
    else:
        print('#3.아무거나 준비')

    print('#4.물을 붓는다')
    print('#5.손님~ 커피 나왔습니다.')

#메인 코드
customer = ['홍길동', '이순신', '김철수','이영희']
for i in customer:
    menu = int(input(i +'님, menu 선택(1.아메리카노 2.라떼 3.모카 4.카푸치노): '))
    coffee_machine(menu)