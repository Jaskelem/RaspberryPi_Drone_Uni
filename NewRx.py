#!/usr/bin/env python

import time
import os     #importing os library so as to communicate with the system
os.system ("sudo pigpio-master/pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error

import pigpio
import piVirtualWire_master.piVirtualWire as vw

RX_PIN = 17
BAUD_RATE = 2000

pi = pigpio.pi()
rx = vw.rx(pi, RX_PIN, BAUD_RATE)

def RadioSignal():
    while rx.ready():
        message_bytes = rx.get()
        message=int.from_bytes(message_bytes[:2], byteorder='little')
        return message

while True:
    print(RadioSignal())
    time.sleep(0.1)
