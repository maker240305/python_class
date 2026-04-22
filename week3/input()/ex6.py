name = input('이름을 입력하세요 : ')
kor = int(input('국어 성적을 입력하세요 : '))
eng = int(input('영어 성적을 입력하세요 : '))
math = int(input('수학 성적을 입력하세요 : '))
sum1 = kor + eng + math
ave = sum1 / 3
print()
print('홍길동 님의 성적은')
print('총합', sum1,'점, 평균',ave,'점입니다.')