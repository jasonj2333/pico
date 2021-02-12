from machine import *
import utime
import tm1637
from grove_lcd_i2c import Grove_LCD_I2C

mydisplay = tm1637.TM1637(clk=Pin(18), dio=Pin(19))

LCD_SDA = Pin(2)
LCD_SCL = Pin(3)
LCD_ADDR = 62 # 0x3E or 62
i2c = I2C(1, sda=LCD_SDA, scl=LCD_SCL)
#print(i2c.scan())
lcd = Grove_LCD_I2C(i2c, LCD_ADDR)


sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    mydisplay.temperature(int(temperature))
    #lcd.home()
    lcd.cursor_position(2,0)
    lcd.write("Temp:"+ str(temperature))
    print(temperature)
    utime.sleep(1)