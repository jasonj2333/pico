from machine import Pin
import time

led = Pin(17, Pin.OUT)
button = Pin(9, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)