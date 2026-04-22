#문자열
#len() : 리스트나 문자열의 개수를 셀 때 사용. (파이썬 내장 함수)
ss = '파이썬abcd'
print(len(ss))

#문자열의 함수 => 문자열변수.함수명()
#upper() : 모두 대문자로
ss = 'Python is Easy. 그래서 programming이 재밌네요~^^'
print(ss.upper())
print(ss.lower())      #모두 소문자로
print(ss.swapcase())   #대문자=>소문자로, 소문자=>대문자로
print(ss.title())      #단어의 첫글자만 대문자

#문자열의 공백 제거하기 => strip() => 좌, 우 공백만 제거 (가운대 있는건 안지워짐)
ss = ' 파 이 썬 '
print(ss.strip())
print(ss.lstrip())
print(ss.rstrip())
ss = '----파--이--썬----'
print(ss.strip('-'))

ss = '<<파<<이>>썬>>'
print(ss.strip('<>'))

#문자열 변경하기
ss = ('지금 파이썬을 공부하고 있는 중~')
ss2 = ss.replace('파이썬','Python')
print(ss2)

#문자열 분리하기 => split()
ss = ('지금 파이썬을 공부하고 있는 중~')
print(ss.split())

ss = '하나:둘:셋'
print(ss.split(':'))

ss = '하나\n둘\n셋'
print(ss)
print(ss.splitlines())

#문자열 결합하기 => join()
ss1 = '%'
ss2 = '파이썬'
print(ss1.join(ss2))

#문자열 구성 파악하기
#숫자인지 확인 => isdigit()
ss = '1234'
print(ss.isdigit())

#알파벳 문자이니? => isalpha   한글도 문자
ss = 'abc'
print(ss.isalpha())
ss = '홍길동'
print(ss.isalpha())
ss = 'abc123cdf'
print(ss.isalnum())  #문자+숫자 이냐

ss = 'abc'
print(ss.isupper())  #모두 대문자?
print(ss.islower())  #모두 소문자?

ss = ' '
print(ss.isspace()) #모두 공백?

#실습문제
#문자열을 입력받아서
#영어나 한글이면 '글자입니다'
#숫자이면 '숫자입니다'
#섞여 있으면 '글자+숫자입니다'
#그렇지 않으면 '그 외 문자' 출력하기
#무한루프 이용 => 종료 조건 공백이 들어오면 종료
while True:
    ss = input('문자열 입력 : ')
    if ss.isspace():
        break
    if ss.isalpha():
        print('글자입니다')
    elif ss.isdigit():
        print('숫자입니다')
    elif ss.isalnum():
        print('글자+숫자입니다')
    else:
        print('그 외 문자열')
