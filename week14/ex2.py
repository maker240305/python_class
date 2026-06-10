#두 개의 그래프 그리기
#범례 표시
import matplotlib.pyplot as plt

#데이터
sqr = [10**2, 11**2, 12**2, 13**2]
myNumber = [90,105,130,180]

#그래프 그리기
plt.plot(sqr, linewidth=10)
plt.plot(myNumber, linewidth=5)
plt.title('10 to 13 Square Numbers')
plt.xlabel('Orders')
plt.ylabel('Square Numbers',fontsize=15)

#범례 표시
plt.legend(['SQR N','MyNumber'])

plt.show()