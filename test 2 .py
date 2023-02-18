import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,100)

p.start(0)
print("starting 0")
time.sleep(3)
print("start")
time.sleep(2)
'''

i=7
while i<23:
    print(i)
    p.ChangeDutyCycle(i)
    for y in range(1,1000,100):
        p.ChangeFrequency(y)
        print("freq: %i" %y)
        time.sleep(1)
    time.sleep(0.5)
    i +=1
i=48
while i<64:
    print(i)
    p.ChangeDutyCycle(i)
    for y in range(1,1000,100):
        p.ChangeFrequency(y)
        print("freq: %i" %y)
        time.sleep(1)
    time.sleep(0.5)
    i +=1
'''
i=88
while i<101:
    print(i)
    p.ChangeDutyCycle(i)
    for y in range(1,1000,100):
        p.ChangeFrequency(y)
        print("freq: %i" %y)
        time.sleep(3)
    time.sleep(0.5)
    i +=1
p.ChangeDutyCycle(0)