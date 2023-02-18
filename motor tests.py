import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)

p1 = GPIO.PWM(12,1000)
p2 = GPIO.PWM(32,1000)
p3 = GPIO.PWM(33,1000)
p4 = GPIO.PWM(35,1000)

p1.start(89)
p2.start(89)
p3.start(89)
p4.start(89)

p1.ChangeFrequency(188)
p2.ChangeFrequency(188)
p3.ChangeFrequency(188)
p4.ChangeFrequency(188)

time.sleep(3)

for i in range(100,88,-1):
    p1.ChangeFrequency(i)
    p2.ChangeFrequency(i)
    p3.ChangeFrequency(i)
    p4.ChangeFrequency(i)
    print("frequincy : %i" %i)
    time.sleep(1)
p1.ChangeFrequency(188)
p2.ChangeFrequency(188)
p3.ChangeFrequency(188)
p4.ChangeFrequency(188)