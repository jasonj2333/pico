from machine import Pin, PWM
import utime

led_r = PWM(Pin(4)) # GPIO pin 4 - red of pico board #
led_g = PWM(Pin(5)) # GPIO pin 5 - green of pico board #
led_b = PWM(Pin(7)) # GPIO pin 7 - blue of pico board #

for i in range(65535):
    led_b.duty_u16(i)
    utime.sleep(0.0001)
    
for i in range(65535, 0, -1):
    led_b.duty_u16(i)
    utime.sleep(0.0001)
    