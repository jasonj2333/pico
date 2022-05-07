from machine import Pin, Timer
red = Pin(11, Pin.OUT)
yellow = Pin(13, Pin.OUT)
green = Pin(14, Pin.OUT)

red2 = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)
timer = Timer()

red.value(1)
yellow.value(0)
green.value(1)
red2.value(0)
blue.value(1)

def blink(timer):
    red.toggle()
    yellow.toggle()
    green.toggle()
    red2.toggle()
    blue.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)