def bigger(v1, v2):
    if v1 > v2:
        big = v1
    else:
        big = v2
    return big

x = int(input('첫 번째 숫자: '))
y = int(input('두 번째 숫자: '))

res = bigger(x, y)
print('큰수: ', res)