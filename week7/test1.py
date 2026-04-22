slist = []
for i in range(5):
    a = int(input('판매량입력:'))
    slist.append(a)
ave = ( slist[0] + slist[1] + slist[2] + slist[3] + slist[4] ) / 5

def ideal(r):
    nlsit = []
    for i in r:
        if i > (ave*1.5):
            nlsit.append(i)
    return nlsit

print(f'이상치 판매량은: {ideal(slist)}')