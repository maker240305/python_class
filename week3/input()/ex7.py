#문자열을 정수로 변화 => int()
#문자열을 실수로 변환 => float()
#온도 변환기
F_temp = float(input('화씨온도를 입력하세요 : '))
C_temp = (F_temp- 32) * (5/9)

#반올림 함수 => round()
print('화씨',F_temp,'도는 섭씨', round(C_temp, 2),'도입니다.')