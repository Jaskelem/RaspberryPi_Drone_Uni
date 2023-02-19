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

Black forward
White Back
"""
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIOPWM1=12 # GPIO who has PWM
GPIOPWM2=32 # GPIO who has PWM
GPIOPWM3=33 # GPIO who has PWM
GPIOPWM4=35 # GPIO who has PWM

GPIO.setup(GPIOPWM1,GPIO.OUT)
GPIO.setup(GPIOPWM2,GPIO.OUT)
GPIO.setup(GPIOPWM3,GPIO.OUT)
GPIO.setup(GPIOPWM4,GPIO.OUT)
motor1=GPIO.PWM(GPIOPWM1,1000)
motor2=GPIO.PWM(GPIOPWM2,1000)
motor3=GPIO.PWM(GPIOPWM3,1000)
motor4=GPIO.PWM(GPIOPWM4,1000)

#1st motor left black
#2st motor right black
#3st motor left white
#4st motor right white
#rearange this depending on how motors are wired
motors=[motor1,motor2,motor3,motor4]
#Set up all the motors
def Set_UP():

    #Set Duty cycle to 89,I found this works for me
    motor1.start(89)
    motor2.start(89)
    motor3.start(89)
    motor4.start(89)
    #Set the Frequincy to stop it from moving and beeping
    motor1.ChangeFrequency(188)
    motor1.ChangeFrequency(188)
    motor1.ChangeFrequency(188)
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
    Stop()
    for motor in motors:
        for i in range(0,11,1):
            MotorSpeed(motor,i)
            print(i)
            time.sleep(1)
    Stop()