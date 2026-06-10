#원(파이) 그래프
import matplotlib.pyplot as plt

#한글 깨짐 방지
plt.rc('font', family='Malgun Gothic')

#데이터
ratio = [30.2,27.8,20.7,21.2]

#원 그래프
plt.pie(ratio)
plt.title('2019년 인구주택총조사 결과')
plt.legend(['1인가구','2인가구','3인가구','4인가구이상'])

plt.show()