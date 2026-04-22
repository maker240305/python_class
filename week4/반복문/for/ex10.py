#반복문 - 횟수반봅(for), 조건반복(while)

#for 변수 in 리스트:
#    문장 1
#    문장 2
for i in [1,2,3,4,5]:
    print(i, 'hello~')

menu = ['americano', 'latte', 'moca', 'ccino']
for item in menu:
    print(item)

#반복문에 많이 사용하는 함수 : range()
for i in range(1, 11): #range(시작, 마지막, 증가값)
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 1, -2):
    print(i)

