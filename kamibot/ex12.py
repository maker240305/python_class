from pyKamipi.pibot import *
kamibot = KamibotPi('COM5',57600)
kamibot.turn_led(0,0,255)

for i in range(5):
    kamibot.draw_arc(3,360,1)
    kamibot.delay(1)
    kamibot.move_forward_unit(5, '-l', 100)
    kamibot.delay(1)

kamibot.close()