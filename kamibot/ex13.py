from pyKamipi.pibot import *
kamibot = KamibotPi('COM5',57600)
while True:
    left, right = kamibot.get_object_detect() #근접셉서 왼쪽,오른쪽 값 읽기
    print(f'left={left}, right={right}')      #근접센서 값 출력하기
    if left > 100 or right > 100:
        break
    elif left > 20 or right > 20:
        kamibot.stop()
    else:
        kamibot.go_forward_speed(10,10) #(lspeed, rspeed)

kamibot.close()