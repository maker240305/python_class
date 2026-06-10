from pyKamipi.pibot import *
import time

kamibot = KamibotPi('COM5',57600)


def avoid_left():
    print('왼쪽 장애물!')
    kamibot.turn_led(255,255,0)
    kamibot.move_backward_unit(5,'-l',30) #후진
    time.sleep(0.5)
    kamibot.go_forward_speed(20,0)
    time.sleep(0.4)
    print("-> 왼쪽 장애물 회피 완료")

def avoid_right():
    print('오르쪽 장애물!')
    kamibot.turn_led(255,0,255)
    kamibot.move_backward_unit(5,'-l',30) #후진
    time.sleep(0.5)
    kamibot.go_forward_speed(0,20)
    time.sleep(0.4)
    print("-> 오른쪽 장애물 회피 완료")

print('===자율 회피 주행 시작===')
while True:
    left, right = kamibot.get_object_detect() #근접셉서 왼쪽,오른쪽 값 읽기
    print(f'센서:left={left}, right={right}')      #근접센서 값 출력하기
    if left > 100 or right > 100:
        break
    elif left > 20:
        avoid_left()
    elif right > 20:
        avoid_right()
    else:
        kamibot.go_forward_speed(30,30)
        kamibot.turn_led(0,255,0)
        print('전진')

kamibot.stop()
kamibot.close()