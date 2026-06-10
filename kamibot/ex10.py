#카미봇 연결하기
from pyKamipi.pibot import *

#로봇 객체 생성, COM 포트번호 설정, 통신속도
kamibot = KamibotPi('COM5',57600)

for i in range(255,0,-5):
    kamibot.turn_led(i,0,0)
kamibot.delay(2)
for i in range(0,255,5):
    kamibot.turn_led(0,i,0)
kamibot.delay(2)
for i in range(255,0,-5):
    kamibot.turn_led(0,0,i)

#카미봇 연결 해제
kamibot.close()