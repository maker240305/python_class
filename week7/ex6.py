#딕셔너리 자료구조 => {key:value, ...}
# 딕셔너리 키는 중복되면 안된다!
st_info =  {'2026001':'홍길동', '2026002':'이순신', '2026003':'김철수'}
print(st_info)
print(type(st_info))

#학생정보를 딕셔너리로 저장
st = {'학번':'2026001',
      '이름':'홍길동',
      '학과':'컴퓨터공학과'}
print(st)
#key를 이용해서 value를 가져옴
print(st['학번'])
print(st['이름'])
print(st['학과'])

#새로운 데이터 추가하기
st['연락처'] = '010-2052-5858'
print(st)

#기존의 데이터를 수정하기
st['학과'] = '컴퓨터정보공학과'
print(st)

#데이터 삭제하기
del(st['연락처'])
print(st)

#key를 이용해서 value를 가져오기
print(st['학번'])  #방법1
#print(st['연락처'])  오류!!
#get() 함수를 이용해서 value 가져오기
print(st.get('학번')) #방법2
print(st.get('연락처')) #없는 값이어도 오류 안남! => None

#in 키워드 => 딕셔너리에 키가 포함되어 있는지 확인
print('연락처' in st)

#key 값들만 가져오기 => keys()
print(st.keys())
#value 값들만 가져오기 => values()
print(st.values())
#key+value 값들을 쌍으로 묶어서 반환 => items()
print(st.items())

#딕셔너리를 이용한 반복문 처리
for key in st.keys():
    print(f'{key} - {st[key]}')

for k, v in st.items():
    print(f'{k} - {v}')