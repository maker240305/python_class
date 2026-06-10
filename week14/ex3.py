#분포도(산정도) 그리기
#좌표값을 이용
import matplotlib.pyplot as plt
from random import *

#임의의 좌표값을 데이터로 준비
numX = []
numY = []

for i in range(100):
    numX.append(randint(-10,10))
    numY.append(randint(-10,10))

#산점도 그리기
plt.scatter(numX,numY, s=50, c='red', marker='^')   #s=점크기 c=색깔 marker=점 모양
plt.title('Scatter makes scatter graph')
plt.xlabel('X label')
plt.ylabel('Y label')

plt.show()