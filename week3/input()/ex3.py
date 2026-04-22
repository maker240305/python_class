print('두 점수를 입력하세요.')
num1 = input('첫 번째 정수?')
num2 = input('두 번째 정수?')

#input() 함수로 입력된 값 => 문자열(str)
#문자열을 정수로 변환 => int()

result = int(num1) + int(num2)
print('두 정수의 합은 %s입니다' % result )

#문자열의 연결 => '+'
print('두 정수의 합은 ' + str(result) + '입니다')