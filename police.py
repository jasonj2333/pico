from machine import Pin, Timer, PWM
import time

red2 = Pin(17, Pin.OUT)
blue = Pin(18, Pin.OUT)
buzzer = PWM(Pin(19))

red2.value(0)
blue.value(1)

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

while True:
    blue.toggle()
    red2.toggle()
    playtone(3500)
    time.sleep(0.3)
    red2.toggle()
    blue.toggle()
    playtone(4300)
    time.sleep(0.3)
