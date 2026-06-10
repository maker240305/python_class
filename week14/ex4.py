#막대 그래프
import matplotlib.pyplot as plt

y = [100,120,130,110,80,150]
x = range(1,len(y)+1)

plt.barh(x,y, height=0.5, color='red')
plt.title('Bar')

plt.show()
