num1 = int(input('첫 번째 정수를 입력하세요 >> '))
num2 = int(input('두 번째 정수를 입력하세요 >> '))

def multi_func(n1,n2):
    result = n1 * n2
    return result

res = multi_func(num1,num2)
print(num1,'*',num2,'=',str(res))
