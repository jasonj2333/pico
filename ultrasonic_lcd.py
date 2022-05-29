from machine import Pin, I2C
import utime
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
led = machine.Pin(17, machine.Pin.OUT)
buzzer = machine.Pin(20, machine.Pin.OUT)

from pico_i2c_lcd import I2cLcd

i2c = I2C(id=0,scl=Pin(1),sda=Pin(0),freq=100000)
lcd = I2cLcd(i2c, 0x27, 4, 20) # LCD 16x2

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    lcd.clear()
    lcd.putstr("Dist: "+str(round(distance, 1))+" cm")
    if distance < 10:
        lcd.move_to(0,1)
        lcd.putstr("ALARM!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
while True:
   ultra()
   led.toggle()
   utime.sleep(1)