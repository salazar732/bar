from gpiozero import LEDBoard, Button
from signal import pause

led=LEDBoard(led1=17,led2=18,led3=6,led4=12)

boton1=Button(27,hold_time=0.001)
boton2=Button(22,hold_time=0.001)
boton3=Button(23,hold_time=0.001)
boton4=Button(24,hold_time=0.001)
#boton5=Button(5)
#boton6=Button(26)

led.led1.source=boton1
led.led2.source=boton3
led.led3.source=boton2
led.led3.source=boton2

#led.on()
boton4.when_held = led.off
    
