from machine import Pin
import time

led11 = Pin(11, Pin.OUT)
led13 = Pin(13, Pin.OUT)
led14 = Pin(14, Pin.OUT)
led17 = Pin(17, Pin.OUT)
button6 = Pin(6, Pin.IN, Pin.PULL_UP)
button9 = Pin(9, Pin.IN, Pin.PULL_UP)
button15 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button16 = Pin(16, Pin.IN, Pin.PULL_DOWN)



while True:
    if button6.value() == 0:
        led11.toggle()
        time.sleep(0.5)
    if button9.value() == 0:
        led13.toggle()
        time.sleep(0.5)
        
    if button15.value():
        led14.toggle()
        time.sleep(0.5)
    
    if button16.value():
        led17.toggle()
        time.sleep(0.5)