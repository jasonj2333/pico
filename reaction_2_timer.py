import machine
import utime
import urandom

led = machine.Pin(17, machine.Pin.OUT)
left_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
right_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
fastest_button = None
timer_reaction = 0

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
if fastest_button is left_button:
     print("Left Player wins!")
elif fastest_button is right_button:
     print("Right Player wins!")
print("Winner reaction time was " + str(timer_reaction) + " milliseconds!")