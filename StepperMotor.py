from machine import Pin 
import time


dirPin=Pin(32,Pin.OUT)
stepPin=Pin(14,Pin.OUT)

def turn(n,d):
    dirPin(d)
    for i in range(n):
        stepPin(1)
        time.sleep(0.001)
        stepPin(0)
        time.sleep(0.001)


def keepturn(direction):
    dirPin(direction)
    while True:
        stepPin(1)
        time.sleep(0.001)
        stepPin(0)
        time.sleep(0.001)
