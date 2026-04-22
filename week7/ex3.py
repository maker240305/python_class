#스택 자료구조 - 가장 먼저 들어간 데이터가 가장 나중에 나오는 구조
# = 가장 나중에 들어간 데이터가 가장 먼저 나오는 구조
# 리스트를 이용해서 스택 구조를 구현
parking = []
top =0    #가장 마지막 데이터의 바로 다음 인덱스 값

parking.append('자동차A')
top += 1
parking.append('자동차B')
top += 1
parking.append('자동차C')
top += 1
print(parking)
print(f'top = {top}')

outCar = parking.pop()
top -= 1
print(outCar)
outCar = parking.pop()
top -= 1
print(outCar)
outCar = parking.pop()
top -= 1
print(outCar)

#스택 활용 : 문자열을 거꾸로 출력할 때
word = input('문자열 : ')
#문자열을 리스트로 변환 => list()
wlist = list(word)
print(wlist)

result = []
for i in range(len(wlist)):
    result.append(wlist.pop())

print(result)
print(f'word 문자열을 거꾸로 출력 = {word[::-1]}')

