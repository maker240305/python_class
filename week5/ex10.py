#함수의 반환값(리턴값)
#함수 선언
def func1():
    result = 100
    return result

def func2():
    print('반환값이 없는 함수 실행')

#메인 코드
res = func1()  #리턴값이 있는 함수는 변수로 받아줌
func2()        #리턴값이 없는 함수는 함수이름만 호출

#리턴값이 2개인 경우의 함수
#두 수의 합과 평균을 반환하는 함수
def func3(v1,v2):
    sum = v1+v2
    ave = sum/2
    return sum, ave

res1, res2 = func3(100, 200)
print(res1,res2)

#여러개의 반환값을 하나의 변수로 처리하기
#한 개의 변수에 값을 여러 개 저장할 수 있는 구조 => 리스트
def multi(a,b):
    ret = []
    res1 = a+b
    ret.append(res1)
    ret.append(a-b)
    ret.append(a*b)
    return ret

result = multi(10,20)
print(result)
print(result[0])

#함수의 매개변수
def para2(v1, v2):
    sum = v1+v2
    return sum

def para3(v1, v2, v3):
    return v1+v2+v3

res1 = para2(100, 200)
print('para2() = ', res1)
res2 = para3(100, 200,300)
print('para3() = ', res2)

#default 값 적용
def paraFunction(v1, v2, v3=0):
    return v1+v2+v3

res1 = paraFunction(100, 200)
print(res1)
res2 = paraFunction(100,200,300)
print(res2)