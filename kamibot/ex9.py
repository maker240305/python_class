#카미봇 연결하기
from pyKamipi.pibot import *

#로봇 객체 생성, COM 포트번호 설정, 통신속도
kamibot = KamibotPi('COM5',57600)

#LED 색상을 빨간색으로 켜기
kamibot.turn_led(255,0,0)
kamibot.delay(2)

#카미봇 연결 해제
kamibot.close()