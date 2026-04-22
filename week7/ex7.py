#동물명 영어사전 만들기
#         key  : value
dict = {'강아지':'dog','고양이':'cat','새':'bird','코끼리':'elephant','물고기':'fish','양':'lamb','호랑이':'tiger'}

while True:
    animal = input('동물이름(한글) : ')
    #종료조건 체크
    if animal == '끝':
        break
    result = dict.get(animal)
    if result:  #result의 값이 있으면 True
        print(f'{animal} = {result}')
    else:
        print(f'없음')