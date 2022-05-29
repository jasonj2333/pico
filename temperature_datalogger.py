from machine import Pin, I2C
import utime
from ssd1306 import SSD1306_I2C

WIDTH  = 128                                         
HEIGHT = 32
i2c = I2C(1, scl = Pin(3), sda = Pin(2), freq=400000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
file = open('temperature.txt', 'w')
file.write('Pomiar temperatury\n')

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round((27 - (reading - 0.706)/0.001721), 2)
    #print(temperature)
    get_time = utime.localtime()
    hours_time = str(get_time[3]) + ':' + str(get_time[4]) + ':' + str(get_time[5])
    full_time = str(get_time[0]) + '-' + str(get_time[1]) + '-' + str(get_time[2]) + ' ' + hours_time
    #print(get_time)
    oled.fill(0)
    oled.text(hours_time + '-' + str(temperature), 0,1)
    oled.show()
    file.write(full_time + ' - ' + str(temperature) + '\n')
    file.flush()
    utime.sleep(5)