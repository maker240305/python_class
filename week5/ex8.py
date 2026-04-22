#전역변수와 지역변수의 차이
def func1():
    #지역변수를 전역변수로 지정 => global 키워드
    global a
    a = 10
    print('func1() a=', a)
def func2():
    print('func2() a=', a)

#메인 코드
a = 20 #전역변수-프로그램 모든 지역에서 사용 가능
func1()
func2()