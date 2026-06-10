from pyKamipi.pibot import *
kamibot = KamibotPi('COM5',57600)
kamibot.turn_led(0,0,255)

kamibot.draw_arc(5,360,1)


for i in range(5):
    kamibot.move_forward_unit(5,'-l',100)
    kamibot.delay(1)
    kamibot.turn_right_speed(144,150)
    kamibot.delay(1)

kamibot.close()