free_big = 34000
free_small = 25000
night = 10000
time = int(input('현재 시간 입력(0~24)>>'))
age = int(input('나이 입력(세)>>'))
if time < 17:
    if (age>=3 and age<=12) or age>=65:
        print('요금은',str(free_small)+'입니다')
    else:
        print('요금은',str(free_big)+'입니다')
else:
    print('요금은',str(night)+'입니다')