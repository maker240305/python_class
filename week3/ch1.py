prod1 = int(input('상품1 가격 = '))
prod2 = int(input('상품2 가격 = '))
prod3 = int(input('상품3 가격 = '))
list1 = []
list1.append(prod1)
list1.append(prod2)
list1.append(prod3)
print('가격 리스트 =',list1)
list2 = []
list2.append(int(prod1 * 110/100))
list2.append(int(prod2 * 110/100))
list2.append(int(prod3 * 110/100))
print('(가격+10%)리스트 =',list2)
list3 = []
list3.append(int(prod1 * 85/100))
list3.append(int(prod2 * 85/100))
list3.append(int(prod3 * 85/100))
print('(가격-15%)리스트 =',list3)
