from machine import Pin
import time

led = Pin(17, Pin.OUT)
button = Pin(16, Pin.IN, Pin.PULL_UP)



while True:
    print(button.value() )
    if button.value():
        led.toggle()
    time.sleep(0.5)