#사칙연산을 처리하는 계산기 프로그램
#필요한 데이터 - 연산자(+,-,*,/), 숫자1, 숫자2
def calc(v1,v2,op):
    result = 0
    if op == '+':
        result = v1+v2
    elif op == '-':
        result = v1-v2
    elif op == '*':
        result = v1*v2
    elif op == '/':
        result = v1/v2
    else:
        print('op error')
    return result

#메인코드
#무한루프를 이용한 반복 프로그램으로 확장하기
#종료조건 : 'q'를 입력하면 프로그램 종료
while True:
    oper = input('연산자 기호(+,-,*,/)(종료:q) : ')
    #종료조건 체크
    if oper == 'q':
        break
    num1 = int(input('숫자 1 : '))
    num2 = int(input('숫자 2 : '))
    res = calc(num1,num2,oper)
    print(num1, oper, num2, '=', res)