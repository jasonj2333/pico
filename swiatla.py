from machine import Pin, Timer
red = Pin(10, Pin.OUT)
yellow = Pin(11, Pin.OUT)
green = Pin(12, Pin.OUT)
timer = Timer()

def blink(timer):
    red.toggle()
    yellow.toggle()
    green.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)