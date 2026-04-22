#문자열 서식 지정
# % 서식
print('I eat %d apples.' % 3)   # %d = 숫자(정수)
print('I eat %s apples.' % 'five') # %s = 문자

name = '홍길동'
score = 90
#홍길동의 점수는 90점 입니다.
print('%s의 점수는 %d점 입니다.' % (name, score))

height  = 170.5
print('키는 %.1fcm 입니다.' % height)

# format() 함수 => 문자열 함수
name = '홍길동'
score = 90
print('{}의 점수는 {}입니다.'.format(name, score))

#f-string
print(f'{name}의 점수는 {score}접 입니다.')

count = 3
price = 1200
print(f'총 금액은 {count*price}원 입니다.')