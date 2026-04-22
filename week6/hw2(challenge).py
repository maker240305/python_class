ss = input('입력 : ')
ss2= ss.lower()
sslen = len(ss2)

moum = []

for i in range(sslen):
    if 'a' in ss2[i] or 'e' in ss2[i] or 'i' in ss2[i] or 'o' in ss2[i] or 'u' in ss2[i]:
        moum.append(ss2[i])

print(f'모음 개수:{len(moum)}개 {moum}')