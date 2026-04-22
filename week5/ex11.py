def ave_func(v1,v2,v3):
    return (v1+v2+v3)/3

num1 = int(input('숫자1: '))
num2 = int(input('숫자2: '))
num3 = int(input('숫자3: '))

res = ave_func(num1,num2,num3)
print('평균:',round(res,1))