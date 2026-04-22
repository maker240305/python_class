#리스트 조작 함수
aa = [30, 10, 20]
print(f'현재 리스트 = {aa}')

#리스트에 데이터 추가 => append() : 항상 맨 뒤에 추가
aa.append(40)
print(f'append(40)한 후 리스트 = {aa}')

#특정 위치에 데이터 추가 => insert()
aa.insert(0, 100)
print(f'insert(0,100) 후 리스트 = {aa}')

#데이터 삭제 => remove()
aa.remove(100)
print(f'remove(100) 후 리스트 = {aa}')

#데이터 추출 => pop() : 제일 마지막 값이 나옴
result = aa.pop()
print(f'pop()으로 추출한 값 = {result}')
print(f'pop() 후 리스트 = {aa}')

#데이터 정렬 => sort() : 오름차순 정렬
aa.sort()
print(f'sort() 후 리스트 = {aa}')

#내림차순 정렬 => reverse()
aa.reverse()
print(f'reverse() 후 리스트 = {aa}')

#특정 데이터의 위치 => index()
print(f'10 값의 위치 = {aa.index(10)}')
#print(f'40 값의 위치 = {aa.index(40)}')  없는 값 찾기 불가. 오류 뜸

#특정 값의 개수 => count()
print(f'30 값의 개수 = {aa.count(30)}')
print(f'40 값의 개수 = {aa.count(40)}')

#전체 리스트의 모든 데이터의 개수 => len()
print(f'리스트의 모든 데이터 개수 = {len(aa)}')