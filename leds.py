from gpiozero import LEDBoard, Button
"""
pin_motor1=17
pwm_motor1=18
pin_motor2=6
pwm_motor2=12
sensores1=5
sensores2=26
botones=[27,22,23,24]
"""
led=LEDBoard(led1=17,led2=18,led3=6)

boton1=Button(27)
boton2=Button(22)
boton3=Button(23)
boton4=Button(24)
boton5=Button(5)
boton6=Button(26)

while True:
    try:
        boton1.when_pressed = led.led1.on()
        boton2.when_pressed = led.led2.on()
        boton3.when_pressed = led.led3.on()
        boton4.when_pressed = led.off()
        boton5.when_pressed = led.off()
        boton6.when_pressed = led.off()
    except KeyboardInterrupt:
        Button.close()
        LEDBoard.close()
