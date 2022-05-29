from machine import ADC, Pin
from time import sleep

photoPIN = 27

def readLight(photoGP):
    photoRes = ADC(Pin(photoPIN))
    light = photoRes.read_u16()
    light = round(light/65535*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(1) # set a delay between readings