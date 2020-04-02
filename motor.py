from gpiozero import LED, Button, PWMOutputDevice, OutputDevice
from time import sleep

motor1=OutputDevice(17)
pwm1=(18)
motor2=(6)
pwm2=(12)
sensor1=5
sensor2=26
boton1=Button(27)
boton2=Button(22)
boton3=Button(23)
boton4=Button(24)

def  motor1_contorl(dire,fer=200):
    pwm1.frequency(fer)
    if (dire is True):
        motor1.on()
    else:
        motor1.off()
    pwm1.on()
    sleep(0.01)

def  motor2_contorl(dire,fer=200):
    pwm2.frequency(fer)
    if (dire is True):
        motor2.on()
    else:
        motor2.off()
    pwm2.on()
    sleep(0.01)

