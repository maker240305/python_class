#중첩 조건문 - 점수별 학점 출력 프로그램
score = int(input('점수 입력 : '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')