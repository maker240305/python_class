gugu = int(input('출력할 구구단 숫자를 입력하세요(2~9) : '))
print('=== 구구단',str(gugu)+'단 ===')

for i in range(1,10):
    print(gugu,'*',i,'=',(gugu*i))
