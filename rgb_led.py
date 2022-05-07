from machine import Pin
import utime

led_r = Pin(4, Pin.OUT) # GPIO pin 4 - red of pico board #
led_g = Pin(5, Pin.OUT) # GPIO pin 5 - green of pico board #
led_b = Pin(7, Pin.OUT) # GPIO pin 7 - blue of pico board #

while True:

    led_r.value(1) #To turn ON led #
    utime.sleep(1)
    led_r.value(0) #To turn OFF led #
    led_g.value(1)
    utime.sleep(1)
    led_g.value(0)
    led_b.value(1)
    utime.sleep(1)
    led_b.value(0)