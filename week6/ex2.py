#문자열의 인덱스
#문자열의 모든 글자를 하나씩 출력 => 인덱스 이용
ss = '파이썬 Python'

ssLen = len(ss)
for i in range(ssLen):    #0,1,2,3,.... => 인덱스로 사용 가능
    print(ss[i], end='')  #end => 밑으로 안내리고 계속 출력
print()
#문자열 인덱스 관련 함수
#               1         2         3
#     01234567890123456789012345678901234567890
ss = 'We are studing Python. Python is easy~^^'
print(ss.count('Python'))  #'Python'이 몇번 있느냐
print(ss.find('Python'))   #'Python'이 몇번 인덱스에 있는지 찾아줌
print(ss.find('Python', 20))
print(ss.find('C++'))      #없는것을 검색하면 -1 이라고 뜸
print(ss.startswith('We')) #'we'로 시작하냐?
print(ss.endswith('^^'))   #'^^'로 끝나냐?