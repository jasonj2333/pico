import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(17, machine.Pin.OUT)
buzzer = machine.Pin(19, machine.Pin.OUT)
kon = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

def alarm():
    for i in range(50):
            led.toggle()
            #buzzer.toggle()
            utime.sleep_ms(100)
            
def pir_check(pin):
    if pin.value():
        print("ALARM! Motion detected! PIR")
        alarm();
            
def kon_check(pin):
    if pin.value()==0:
        print("ALARM! Motion detected! KON")
        alarm();
    

while True:
    led.toggle()
    kon_check(kon)
    pir_check(sensor_pir)
    utime.sleep(1)