#in 키워드를 이용해서 데이터 확인
dict = {'강아지':'dog','고양이':'cat','새':'bird','코끼리':'elephant','물고기':'fish','양':'lamb','호랑이':'tiger'}

while True:
    animal = input('동물이름(한글) : ')
    if animal == '끝':
        print('프로그램 종료')
        break
    if animal in dict:
        print(f'{animal} - {dict[animal]}')
    else:
        print(f'없음')