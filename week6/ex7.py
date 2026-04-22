# 스포츠 기사 만들기
winner = input('승리팀 : ')
loser = input('패배팀 : ')
score = input('score : ')
kind = input('경기유형(1.불꽃튀는 2.단조로운 3.일방적인): ')
place = input('경기장소: ')
mvp = input('MVP : ')

if kind == '1':
    kind = '불꽃튀는'
elif kind == '2':
    kind = '단조로운'
elif kind == '3':
    kind = '일방적인'

print('[ 스포츠 기사 ]')
print(f'오늘 {place}에서 {winner}팀과 {loser}팀의 경기가 있었습니다.\n '
      f'경기는 {winner}팀의 {score}승리로 끝이 났습니다.\n'
      f'오늘 승부는 {kind} 경기가 펼쳐졌습니다.\n'
      f'MVP는 {mvp} 선수였습니다.')