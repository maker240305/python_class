#for 반복문, continue 사용
#1부터 100까지의 합을 구하시오
#단, 3의 배수는 재외하시오.
sum = 0   #누적되는 값은 반드시 초기화 필수!
for i in range(1, 101):
    if (i % 3) == 0:
        continue
    sum += i
print(sum)