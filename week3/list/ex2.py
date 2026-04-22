#list의 슬라이싱(slicing) => 일부분을 잘라오기
numbers = [10,20,30,40,50,60,70,80,90]

#슬라이실 형식 : 리스트변수[start : stop]   ex: 2:7이면 2번부터 7번앞 6번까지
print(numbers[2:7]) #리스트를 짤라도 리스트임
print(numbers[0:3])
print(numbers[:3]) #start가 생략되면 처음부터
print(numbers[6:9])
print(numbers[6:]) #stop이 생략하면 끝까지
print(numbers[:])  #start,stop 둘다 생략이면 전체다

#슬라이싱 형식 : 리스트변수[start : stop : step]
#step : 증가값, 건너뛰는 개수
print(numbers[1::2])

listA=['mango','banana','apple','orange','kiwi']

print(listA[1])
print(listA[0])
print(listA[1:])
print(listA[:3])
print(listA[1:4:2])
print(listA[::-1])
print()
print(listA[2])
print(listA[:2])
print(listA[1:5:3])
print(listA[3:0:-1])
print(listA[-2:-5:-1])

#list에 데이터 추가하기 => append()
listA.append('melon')
print(listA)

listB = []
print(listB)
data1 = input('데이터 입력 : ')
listB.append(data1)
print(listB)

fruits = []
data1 = input('과일 입력 : ')
data2 = input('과일 입력 : ')
data3 = input('과일 입력 : ')
data4 = input('과일 입력 : ')
data5 = input('과일 입력 : ')
fruits.append(data1)
fruits.append(data2)
fruits.append(data3)
fruits.append(data4)
fruits.append(data5)
print(fruits)
print('첫번째 과일 : ', fruits[0])
print('마지막 과일 : ', fruits[4])