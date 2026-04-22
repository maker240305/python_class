birth = int(input("출생년도 : "))
age = 2026 - birth + 1
print('당신의 나이는',str(age)+'세입니다.')
if age >= 20:
    print('성인입니다.')
else:
    print('미성년자입니다.')
