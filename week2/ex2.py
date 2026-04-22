#파이썬의 기본 데이터형
#정수형
a = 0xFF      #16진수
b = 0o77      #8진수
c = 0b1111    #2진수
print(a,b,c)

#실수형
a = 3.14
b = 3.14e5 #e는 십의 제곱 e5면 10의 5제곱
print(a,b)

#숫자 연산
# ';' - 2개의 명령문을 한 줄에 쓸 때 사용
a = 10; b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#'**' : 제곱승
a =9; b = 2
print(a**b)

#'//' : 나눈 몫
print(a//b)

#'%' : 나눈 나머지
print(a%b)

#bool형 데이터
a = True

a = (10 > 100)
print(a)

a = (100 == 100)
print(a)

#문자열
a = "파이썬"
print(type(a))

#파이썬의 문자열은 반드시 따옴표를 사용 => "",'' 둘다 가능
print("작은 따옴표는 ' 모양이다.")
print('큰 따옴표는 " 모양이다.')

#문자열을 여러 줄 출력하기
#a = ("파이썬
#     프로그래밍")
a = "파이썬 \n프로그래밍 \n언어" #줄바꾸는법 역슬레시 \ 사용
print(a)
a = """파이썬 
프로그래밍
언어"""                       #줄바꾸는법 """ 세번쓰기
print(a)

#문자열의 연산 : +, *
a = "파이썬"
print(a + a) #문자열의 + : 문자열 연결
print(a * 5) #문자열의 * : 문자열 반복

#문자열과 숫자는 + 연사자로 연결할  수 없다!!
a = "국어 점수는"
b = 90
#print(a + b) #오류임!!

# 숫자를 문자로 변환 => str()
print(a + str(b) + "점입니다.")

#문자열과 숫자의 상호 변환
#int() : 문자열을 정수로 변환
s1 = "100" #일공공 문자열임
print(int(s1) + 1)

#float() : 문자열을 실수로 변환
s2 = "100.123"
print(float(s2) + 10)

#복합대입 연산자 : 자기값의 +,-,* 하기
a = 10
a += 5; print(a)
a -= 5; print(a)
a *= 5; print(a)
a /= 5; print(a) #나누기는 실수로 나옴 '10.0'
a //= 5; print(a)
a %= 5; print(a)
a **= 5; print(a)

##관계 연산자 (비교 연산자)
a, b = 100, 200
print(a > b) #비교연산의 결과는 참 or 거짓
print(a == b)
print(a != b)

##논리 연산자
#and(논리곱) 둘 다 참이어야 함 a>100 and a<200
#or(논리합) 둘 중 하나만 참이어도 참 a==100 o r a==200
#not(논리부정)

##연산자 우선순위

##실습
print()
print(5 == 5)
print(8 != 5)
print(True == False)
print(True != False)
print(True == 1)
print(True == 0)
print(False == 0)

