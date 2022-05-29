# Tutaj pisz swój kod, młody padawanie ;-)
import board
from time import sleep
from digitalio import DigitalInOut, Direction
import pwmio

buzzer = pwmio.PWMOut(board.GP19, frequency=3700, duty_cycle=0, variable_frequency=True)
red = DigitalInOut(board.GP11)
red.direction = Direction.OUTPUT

yellow = DigitalInOut(board.GP13)
yellow.direction = Direction.OUTPUT
yellow.value = True
red.value = False

def toggle(pin):
    if pin.value:
        pin.value = False
    else:
        pin.value = True

while True:
    toggle(yellow)
    toggle(red)
    buzzer.duty_cycle = 2 ** 11
    sleep(0.3)
    buzzer.duty_cycle = 0
    toggle(red)
    toggle(yellow)
    buzzer.duty_cycle = 2 ** 12
    sleep(0.3)
    buzzer.duty_cycle = 0


