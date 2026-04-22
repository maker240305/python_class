#bmi 지수 구하기
weight = float(input('당신의 몸무게(kg)를 입력하세요 : '))
height = float(input('당신의 키(cm)를 입력하세요 : '))

#키의 단위 변환 : cm => m : 1m = 100cm
m_height = height / 100

bmi =  weight / (m_height ** 2)
print('당신의 BMI 지수는', round(bmi, 1))