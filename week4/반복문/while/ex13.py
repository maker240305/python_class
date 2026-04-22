#조건반복문 - while
i = 1
while i <10:
    print(i)
    i += 1

#무한루프 만들기 : while True:
#두 수를 입력받아서 합을 출력해 주는 계산기 만들기
while True:
    num1 = int(input('숫자 1 입력 : '))
    #숫자 1에 0이 입력되면 반복문을 종료해자
    if num1 == 0:
        break
    num2 = int(input('숫자 2 입력 : '))
    sum = num1 + num2
    print(num1,'+',num2,'=',sum)

print('프로그램 종료')

#반복문의 제어 - break
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print('break 종료')

#continue - 반복문의 처음으로 돌아가게 하는 제어문
for i in range(1, 11):
    if i == 5:
        continue    #값을 건너뛰는 효과
    print(i)


