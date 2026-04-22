#list자료형
aa = [0,0,0,0]
print(aa)
print(type(aa))
print(aa[0])

aa[0] = int(input('1번째 숫자 : '))
print(aa[0])

#list의 다양한 모양
aa = [] #빈 리스트
bb = [10,20,30] #숫자
cc = ['홍길동', '이순신']
dd = [10, '파이썬', 3.14, True]
print(dd)

#list의 인덱스
#           0       1       2       순서는 0부터 시작
colors = ['red', 'green', 'blue']
#reverse    -3      -2      -1
print(colors[2])
print(colors[-1])