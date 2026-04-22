#큐 자료구조 - 먼저 들어간 데이터가 먼저 나오는 구조 : first in first out(FIFO)
#리스트를 이용해서 큐 구조 구현
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
for i in range(len(parking)):
    outCar = parking.pop(0)
    print(outCar)

