import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
global led
led = machine.Pin(17, machine.Pin.OUT)
led.value(0)
buzzer = machine.Pin(19, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

global button_pressed
button_pressed = False

from pico_i2c_lcd import I2cLcd

i2c = machine.I2C(id=0,scl=machine.Pin(1),sda=machine.Pin(0),freq=100000)
lcd = I2cLcd(i2c, 0x27, 4, 20) # LCD 16x2

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value() and button_pressed:
        lcd.clear()
        lcd.putstr("ALARM!              Motion detected!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
        lcd.clear()
        lcd.putstr("ALARM ON! ")
    
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
       
def button_handler(pin):
    global button_pressed
    global led
    if not button_pressed:
        button_pressed = True
        lcd.clear()
        lcd.putstr("ALARM ON! ")
    else:
        button_pressed = False
        led.value(0)
        lcd.clear()
        lcd.putstr("ALARM OFF!")
        
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

lcd.putstr("ALARM OFF!")

while True:
    
    if button_pressed:
        led.toggle()    
    #print(button_pressed)
    utime.sleep(1)`