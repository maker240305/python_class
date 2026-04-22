#주석(comment) - 코드에 대한 설명, 프로그램 실행과는 무관
#변수 지정
# '=' : 오른쪽 값을 왼쪽 변수에 대입 (등호연산자)
intVar = 0
floatVar = 3.14
strVar = "홍길동"
bloorVar = True
print(intVar, floatVar, strVar, bloorVar)
#type() : 변수가 저장하고 있는 데이터 타입을 확인
print(type(intVar))
print(type(floatVar))
print(type(strVar))
print(type(bloorVar))


#파이썬 키워드
import keyword
print(keyword.kwlist)
#변수명 조건 = 대소문자 구분, 한글변수가능, 숫자시작 안됨, 특수문자안됨, _가능, 등록된 키워드는 사용불가

#변수의 사용
intVar = 200
floatVar = 100.123
strVar = "파이썬"
boolVar = False
print(intVar, floatVar, strVar, boolVar)

var1 = 100
var2 = var1 + 100
print(var2)

var1 = 100 + 200
print(var1)

var4 = 300
var3 = var4
var2 = var3
var1 = var2
print(var1)

var1 = var2 = var3 = var4 = 500
print(var1)
