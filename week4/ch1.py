while True:
    gugu = int(input('출력할 구구단 숫자를 입력하세요(2~9) : '))
    if gugu == 0:
        break
    elif gugu >=2 and gugu <=9:
        print('=== 구구단',str(gugu)+'단 ===')
        for i in range(1,10):
            print(gugu,'*',i,'=',(gugu*i))
    else:
        print('입력된 숫자를 확인하고 다시 입력하세요')
        continue