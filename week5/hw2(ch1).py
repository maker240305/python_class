sale = []               #판매량 리스트

for i in range(5):      #판매량 5번 입력받기
    v = int(input('판매량 입력: '))
    sale.append(v)

total = sale[0] + sale[1] + sale[2] + sale[3] + sale[4]
ave = total / 5
new_list = []

def find_outliers(get_list):
    ret_list = []
    for j in get_list:
        if j >= (ave * 1.5):
            ret_list.append(j)
    return ret_list

new_list = find_outliers(sale)

print('이상치 판매량:',new_list)