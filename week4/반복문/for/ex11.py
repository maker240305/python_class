#for 반복문을 이용하여 별표 출력하기
num = int(input('숫자 입력 : '))
for i in range(num):  # 0 ~ (num-1) 까지 생성
    print('★' * (i+1))
