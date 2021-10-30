from machine import Pin, PWM
from utime import sleep
from pitches import tones
buzzer = PWM(Pin(18))
buzzer1 = PWM(Pin(19))

song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)
    buzzer1.duty_u16(1000)
    buzzer1.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)
    buzzer.duty_u16(1)

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i].lower()])
        sleep(0.3)
    bequiet()
playsong(song)