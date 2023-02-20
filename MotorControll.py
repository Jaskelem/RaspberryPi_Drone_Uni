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
import os     #importing os library so as to communicate with the system
os.system ("sudo pigpio-master/pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import time

motor1=23  #Connect the ESC in this GPIO pin
motor2=27  #Connect the ESC in this GPIO pin
motor3=22  #Connect the ESC in this GPIO pin
motor4=10  #Connect the ESC in this GPIO pin

#1st motor left black
#2st motor right black
#3st motor left white
#4st motor right white
#rearange this depending on how motors are wired
motors=[motor1,motor2,motor3,motor4]

pi = pigpio.pi();

max_value = 2500 #change this if your ESC's max value is different or leave it be
min_value = 1500  #change this if your ESC's min value is different or leave it be

def StartUp():
    for power in range(min_value,1515,1):
        for motor in motors:
            pi.set_servo_pulsewidth(motor, power)
        time.sleep(1)
    Stop()
    
def Stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    for motor in motors:
        pi.set_servo_pulsewidth(motor, min_value)
    pi.stop()
    
def Test():
    for power in range(1517,1550,1):
        for motor in motors:
            pi.set_servo_pulsewidth(motor, power)
        print(power)
        time.sleep(5)
    Stop()

def MotorSpeed(motor,power):
    pi.set_servo_pulsewidth(motor, power)


if __name__ == "__main__":
    StartUp()