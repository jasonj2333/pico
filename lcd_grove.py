#
# Generate random number and display it to the LCD
# using Raspberry Pi Pico
#
# Raspberry Pi Pico
# - [Bare Board] https://my.cytron.io/p-raspberry-pi-pico?tracking=idris
# - [Pre-soldered Headers] https://my.cytron.io/p-raspberry-pi-pico-pre-soldered-headers?tracking=idris
# - [Maker Pi Pico] https://my.cytron.io/p-maker-pi-pico?tracking=idris
# Grove 16x2 I2C LCD (White on Blue)
# - https://my.cytron.io/p-grove-16-x-2-lcd-white-on-blue?tracking=idris
#
# Update:
# 26 Jan 2021 - Tested with MicroPython Pico V1.13-290-g556ae7914
# 

from machine import *
from utime import sleep
from pitches import tones
import urandom
from grove_lcd_i2c import Grove_LCD_I2C

sleep(1)
print("MicroPython on Raspberry Pi Pico")
print()

led = Pin(17, Pin.OUT)
button1 = Pin(9, Pin.IN, Pin.PULL_UP)
button2 = Pin(6, Pin.IN, Pin.PULL_UP)

LCD_SDA = Pin(2)
LCD_SCL = Pin(3)
LCD_ADDR = 62 # 0x3E or 62
i2c = I2C(1, sda=LCD_SDA, scl=LCD_SCL)
#print(i2c.scan())
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.write("  Raspberry Pi  \n      Pico")

tempo = 0.8

melody1 = ('c4','g4')
rhythm1 = [8,8]

melody2 = ('c4','f4','a4','c5','','a4','c5')
rhythm2 = [8,8,8,8,4,8,2]

def bequiet():
    buzzer.duty_u16(0)

def play_melody(melody, rhythm):
    for tone, length in zip(melody, rhythm):
        beeper = PWM(Pin(20))
        if tones[tone] != 0:
            beeper.duty_u16(32768)
            beeper.freq(tones[tone])
        sleep((tempo/length)*1.3)
        beeper.deinit()

play_melody(melody1, rhythm1)

sleep(1)

lcd.clear()
lcd.write(" *Lucky Winner*")

button_pressed = False
counter = 0

while True:
    led.toggle()
    sleep(0.1)
    
    if button1.value() == 0:
        button_pressed = True
        counter = 0
    
    if button_pressed == True:
        counter += 1
        if counter == 20:
            button_pressed = False
            sleep(1)
            print("Congratulation!")
            play_melody(melody2, rhythm2)
            while button2.value() == 1:
                pass
        sleep(counter*0.025)
        
    random_number = urandom.uniform(1, 38)
    lcd.cursor_position(7, 1)
    lcd.write("{:2.0f}".format(random_number))