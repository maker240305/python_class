#데이터 시각화
#나의  성장 데이터 그래프 보기
import matplotlib.pyplot as plt

#데이터 준비
myGrowth = [130,140,150,165,174,175]
ages = [10,13,16,19,21,24]

#한글 깨짐 방지 코드
plt.rcParams['font.family'] = 'Malgun Gothic'

#그래프 그리기
plt.plot(ages,myGrowth)
plt.title('나의 성장 그래프')
plt.xlabel('age')
plt.ylabel('height(cm)')


plt.show()
