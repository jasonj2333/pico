import machine
import utime
import _thread

p_led_red = machine.Pin(1, machine.Pin.OUT)
p_led_green = machine.Pin(0, machine.Pin.OUT)
led_red = machine.Pin(11, machine.Pin.OUT)
led_amber = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(14, machine.Pin.OUT)
button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(18, machine.Pin.OUT)

global base_sleep
base_sleep = 2

global button_pressed, button2_pressed
button_pressed = button2_pressed = False

def button_handler(pin):
    global button_pressed
    if not button_pressed:
        button_pressed = True
        
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

def button2_handler(pin):
    global button2_pressed
    if not button2_pressed:
        button2_pressed = True
        
button2.irq(trigger=machine.Pin.IRQ_RISING, handler=button2_handler)

while True:
    if button_pressed == True:
        base_sleep += 1
        button_pressed = False
    if button2_pressed == True:
        base_sleep = 2
        button2_pressed = False
    #print(base_sleep)
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
    utime.sleep(2)
    #green
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    utime.sleep(base_sleep)
    #amber
    led_green.value(0)
    led_amber.value(1)
    utime.sleep(base_sleep)
    led_amber.value(0)
