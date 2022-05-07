from machine import Pin, ADC, PWM
import utime

potentiometer = ADC(26)
led = PWM(Pin(11))
led.freq(1000)

while True:
    led.duty_u16(potentiometer.read_u16())

