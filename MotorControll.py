"""
XXD A2212 1000 kV Brushless Outrunner Motor Controll Code
These motors are not well suited for programing and require extra
management to make them work.

They beep constantly and i have not found a way to stop the beeping
the solution i use is to make them spin so slowly they never make a rotation
but twich a bit.

Duty cycle  -   Frequincy   -   Explanation
89          -   188         -   No Beep No Rotation
89          -   100-89      -   From Slowest To Fastest
"""
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIOPWM1=12 # GPIO who has PWM

GPIO.setup(GPIOPWM1,GPIO.OUT)
motor1=GPIO.PWM(GPIOPWM1,1000)

#Set up all the motors
def Set_UP():


    #Set Duty cycle to 89,I found this works for me
    motor1.start(89)
    #Set the Frequincy to stop it from moving and beeping
    motor1.ChangeFrequency(188)

def Speed(numb):
    speeds=list(range(100,89,-1))
    print(speeds)
    return speeds[numb]

def MotorSpeed(motor,speed):
    motor.ChangeFrequency(Speed(speed))

def Stop():
    motor1.ChangeFrequency(188)

if __name__ == "__main__":

    Set_UP()
    Speed(0)
    Stop()
    """
    for i in range(0,11,1):
       MotorSpeed(motor1,i)
       print(i)
       time.sleep(5)
    Stop()
"""