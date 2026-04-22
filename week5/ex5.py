#매개변수와 반환값이 있는 함수
#함수 선언
#두 개의 숫자를 받아서 합을 반호나하는 함수
def plus(num1, num2):
    result = num1 + num2
    return result    #반환값

#메인 코드
#반환값이 있는 함수가 호출된 경우
#반드시 대입연산자 왼쪽에 변수를 지정해야 함
res = plus(100,200)
print(res)
