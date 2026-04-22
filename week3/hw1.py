kor = int(input('국어 점수 입력 : '))
math = int(input('수학 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
listA = []
listA.append(kor)
listA.append(math)
listA.append(eng)
print(listA)
print('국어 :',str(kor)+'점, 수학 :',str(math)+'점, 영어 :',str(eng)+'점')
total = listA[0] + listA[1] + listA[2]
ave = total/3
print('총점 =',total)
print('평균 =',int(ave))
print(listA[0:2])