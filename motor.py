from gpiozero import LED, Button, PWMOutputDevice, OutputDevice
from time import sleep
from signal import pause


motor1=OutputDevice(17)
pwm1=PWMOutputDevice(18,frequency=200)
motor2=OutputDevice(6)
pwm2=PWMOutputDevice(12,frequency=200)
sensor1=5
sensor2=26
boton1=Button(27,hold_time=0.001)
boton2=Button(22,hold_time=0.001)
boton3=Button(23,hold_time=0.001)
boton4=Button(24,hold_time=0.001)

def  motor1_contorl(dire):
    if (dire is True):
        motor1.on()
    else:
        motor1.off()
    pwm1.on()
    sleep(0.01)

def  motor2_contorl(dire):
    if (dire is True):
        motor2.on()
    else:
        motor2.off()
    pwm2.on()
    sleep(0.01)

def derecha():
    motor1_contorl(True)

def izquierda():
    motor1_contorl(False)
    
def arriba():
    motor2_contorl(True)
    
def stop():
    motor1.off()
    motor2.off()
    pwm1.on()
    pwm2.on()

boton1.when_held = derecha()
boton2.when_held = arriba()
boton3.when_held = izquierda()
boton4.when_held = stop()
pause()
