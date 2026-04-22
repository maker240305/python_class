#튜플(tuple) 자료구조
# #리스트와 거의 비슷하지만 데이터를 변경할 수 없다!
tt = (10, 20, 30)
print(tt)
print(type(tt))

tt = (10,) # , 를 사용해야 튜플로 인식
print(tt)
print(type(tt))

tt = (10, 20, 30)
print(tt[0])
print(tt[:2])
print(tt + tt)
print(tt * 3)
print(len(tt))
#tt[0] = 100
#tt.append(100)

#튜플 실습
ss = 'ABCDEF'
#문자열을 튜플로 전환 => tuple()
tt = tuple(ss)
print(tt)

for i in tt:
    print(i, end='')

