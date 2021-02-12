import machine
import utime
import urandom
from pico_i2c_lcd import I2cLcd
from machine import I2C

i2c = I2C(id=1,scl=machine.Pin(3),sda=machine.Pin(2),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2

led = machine.Pin(17, machine.Pin.OUT)
left_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
right_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
fastest_button = None
timer_reaction = 0

lcd.clear()
lcd.putstr('Be ready!')

def button_handler(pin):
    left_button.irq(handler=None)
    right_button.irq(handler=None)
    global timer_reaction
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    global fastest_button
    fastest_button = pin

led.value(1)
utime.sleep(urandom.uniform(2, 5))
led.value(0)
timer_start = utime.ticks_ms()
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)
lcd.clear()
if fastest_button is left_button:
    lcd.putstr('Left wins')
elif fastest_button is right_button:
     lcd.putstr('Right wins')

lcd.move_to(0,1)
lcd.putstr("Time: " + str(timer_reaction) + " ms")