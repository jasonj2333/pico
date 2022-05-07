import machine
import utime

p_led_red = machine.Pin(1, machine.Pin.OUT)
p_led_green = machine.Pin(0, machine.Pin.OUT)
led_red = machine.Pin(11, machine.Pin.OUT)
led_amber = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(14, machine.Pin.OUT)
button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)

global base_sleep
base_sleep = 2

def button_handler(pin):
    global base_sleep
    if pin is button:
        base_sleep += 1
    elif pin is button2:
        base_sleep = 2
    print(base_sleep)
        
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)       
button2.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while True:
    print(base_sleep)
    #red
    led_red.value(1)
    utime.sleep(1)
    p_led_red.value(0)
    p_led_green.value(1)
    utime.sleep(base_sleep)
    p_led_red.value(1)
    p_led_green.value(0)
    utime.sleep(1)
    #red-amber
    led_amber.value(1)
    utime.sleep(1)
    #green
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(base_sleep)
    #amber
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(1)
    led_amber.value(0)
