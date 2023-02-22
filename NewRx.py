#!/usr/bin/env python

import time
import pigpio
import piVirtualWire.piVirtualWire as vw

RX=17

BPS=20000

pi=pigpio.pi() #connect to pi

rx = vw.rx(pi,RX,BPS) # specify pi, gpio, boud

msg=0

start = time.time()

while (time.time()-start) < 300:
    while rx.ready():
        print("".join(chr (c) for c in rx.get()))
    time.sleep(0.2)
rx.cancel()
pi.stop()