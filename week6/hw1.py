ss = input('문자열을 입력하세요 : ')

sslen = len(ss)
space = 0
alpha = 0
number = 0
other = 0

for i in range(sslen):
    if ss[i] == ' ':
        space += 1
    elif ss[i].isalpha():
        alpha += 1
    elif ss[i].isdigit():
        number += 1
    else:
        other += 1

print('알파벳은 %d개, 숫자는 %d개, 스페이스는 %d개, 기타 %d개입니다.' % (alpha,number,space,other))
print(f'알파벳은 {alpha}개, 숫자는 {number}개, 스페이스는 {space}개, 기타 {other}개입니다.')