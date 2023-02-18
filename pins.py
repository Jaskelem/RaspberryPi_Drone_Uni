import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,100)

p.start(0)
print("starting 0")
time.sleep(1)
print("start")
time.sleep(2)


i=1

while i<100:
    print(i)
    p.ChangeDutyCycle(i)

    time.sleep(0.5)
    i +=1
    

while i>0:
    print(i)
    p.ChangeDutyCycle(i)
    time.sleep(.05)
    i -=.5
p.ChangeDutyCycle(0)