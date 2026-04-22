#새로운 프로그램 실행 => ctrl+shift+F10
#커피 자판기 프로그램
#함수 선언
def coffee_machine(coffee):
    print('#1.뜨거운 물 준비')
    print('#2.컵 준비')
    if coffee == 1:
        print('#3.보통커피 준비')
    elif coffee == 2:
        print('#3.설탕커피 준비')
    elif coffee == 3:
        print('#3.블랙커피 준비')
    else:
        print('#3.아무거나 준비')

    print('#4.물을 붓는다')
    print('#5.손님~ 커피 나왔습니다.')

#실제 실행되는 메인 코드
#첫 번재 손님
menu = int(input('메뉴 선택(1.보통커피 2.설탕커피 3.블랙커피): '))
coffee_machine(menu)   #함수 호출

#두 번재 손님
menu = int(input('메뉴 선택(1.보통커피 2.설탕커피 3.블랙커피): '))
coffee_machine(menu)   #함수 호출
