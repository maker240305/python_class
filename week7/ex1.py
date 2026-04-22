#자료구조의 이해
#리스트 조작 함수
#리스트를 이용한 반복문
aa = [0] * 5 #5자리를 0으로 초기화
print(aa)
tot = 0 #누적시키는 값은 반드시 초기화

for i in range(len(aa)):    # 0, 1, 2, 3, 4
    aa[i] = int(input('%d번째 숫자 : ' % i))
    tot += aa[i]

print(aa)
print(tot)