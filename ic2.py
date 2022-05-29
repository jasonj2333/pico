from machine import *
from utime import sleep
from grove_lcd_i2c import Grove_LCD_I2C

sleep(1)
print("MicroPython on Raspberry Pi Pico")
print()

LCD_SDA = Pin(2)
LCD_SCL = Pin(3)
LCD_ADDR = 39 # 0x3E or 62
i2c = I2C(1, sda=LCD_SDA, scl=LCD_SCL)
print(i2c.scan())
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.write("  Raspberry Pi  \n      Pico")
sleep(1)
lcd.clear()
lcd.home()
lcd.write(" Witaj na kanale  \n   ScratchSPWZ")
