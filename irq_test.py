import machine
import utime
import urandom

led = machine.Pin(17, machine.Pin.OUT)
button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)

def button_handler(pin):
    button.irq(handler=None)
    print(pin)

led.value(1)
utime.sleep(urandom.uniform(2, 4))
led.value(0)

#button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_handler) #if PULL_UP