from machine import Pin, PWM, I2C, ADC
import utime
from pitches import tones
from ssd1306 import SSD1306_I2C
import framebuf
from buzzer_music import music
import _thread

red = Pin(11, Pin.OUT)
yellow = Pin(13, Pin.OUT)
green = Pin(14, Pin.OUT)

blue = Pin(17, Pin.OUT)
red2 = Pin(18, Pin.OUT)
buzzer = PWM(Pin(19))

#RGB LED
led_r = Pin(4, Pin.OUT) # GPIO pin 4 - red of pico board #
led_g = Pin(5, Pin.OUT) # GPIO pin 5 - green of pico board #
led_b = Pin(7, Pin.OUT) # GPIO pin 7 - blue of pico board #

#Oled Hello
WIDTH  = 128                                         
HEIGHT = 64

#photoresistor
photoPIN = 27

#potentiometer
potentiometer = ADC(26)
conversion_factor = 3.3 / (65535)

#buttons
button6 = Pin(6, Pin.IN, Pin.PULL_UP)
button9 = Pin(9, Pin.IN, Pin.PULL_UP)
button15 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button16 = Pin(16, Pin.IN, Pin.PULL_DOWN)

logo = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
song = '0 E3 1 0;2 E4 1 0;4 E3 1 0;6 E4 1 0;8 E3 1 0;10 E4 1 0;12 E3 1 0;14 E4 1 0;16 A3 1 0;18 A4 1 0;20 A3 1 0;22 A4 1 0;24 A3 1 0;26 A4 1 0;28 A3 1 0;30 A4 1 0;32 G#3 1 0;34 G#4 1 0;36 G#3 1 0;38 G#4 1 0;40 E3 1 0;42 E4 1 0;44 E3 1 0;46 E4 1 0;48 A3 1 0;50 A4 1 0;52 A3 1 0;54 A4 1 0;56 A3 1 0;58 B3 1 0;60 C4 1 0;62 D4 1 0;64 D3 1 0;66 D4 1 0;68 D3 1 0;70 D4 1 0;72 D3 1 0;74 D4 1 0;76 D3 1 0;78 D4 1 0;80 C3 1 0;82 C4 1 0;84 C3 1 0;86 C4 1 0;88 C3 1 0;90 C4 1 0;92 C3 1 0;94 C4 1 0;96 G2 1 0;98 G3 1 0;100 G2 1 0;102 G3 1 0;104 E3 1 0;106 E4 1 0;108 E3 1 0;110 E4 1 0;114 A4 1 0;112 A3 1 0;116 A3 1 0;118 A4 1 0;120 A3 1 0;122 A4 1 0;124 A3 1 0;0 E6 1 1;4 B5 1 1;6 C6 1 1;8 D6 1 1;10 E6 1 1;11 D6 1 1;12 C6 1 1;14 B5 1 1;0 E5 1 6;4 B4 1 6;6 C5 1 6;8 D5 1 6;10 E5 1 6;11 D5 1 6;12 C5 1 6;14 B4 1 6;16 A5 1 1;20 A5 1 1;22 C6 1 1;24 E6 1 1;28 D6 1 1;30 C6 1 1;32 B5 1 1;36 B5 1 1;36 B5 1 1;37 B5 1 1;38 C6 1 1;40 D6 1 1;44 E6 1 1;48 C6 1 1;52 A5 1 1;56 A5 1 1;20 A4 1 6;16 A4 1 6;22 C5 1 6;24 E5 1 6;28 D5 1 6;30 C5 1 6;32 B4 1 6;36 B4 1 6;37 B4 1 6;38 C5 1 6;40 D5 1 6;44 E5 1 6;48 C5 1 6;52 A4 1 6;56 A4 1 6;64 D5 1 6;64 D6 1 1;68 D6 1 1;70 F6 1 1;72 A6 1 1;76 G6 1 1;78 F6 1 1;80 E6 1 1;84 E6 1 1;86 C6 1 1;88 E6 1 1;92 D6 1 1;94 C6 1 1;96 B5 1 1;100 B5 1 1;101 B5 1 1;102 C6 1 1;104 D6 1 1;108 E6 1 1;112 C6 1 1;116 A5 1 1;120 A5 1 1;72 A5 1 6;80 E5 1 6;68 D5 1 7;70 F5 1 7;76 G5 1 7;84 E5 1 7;78 F5 1 7;86 C5 1 7;88 E5 1 6;96 B4 1 6;104 D5 1 6;112 C5 1 6;120 A4 1 6;92 D5 1 7;94 C5 1 7;100 B4 1 7;101 B4 1 7;102 C5 1 7;108 E5 1 7;116 A4 1 7'
mySong = music(song, pins=[Pin(19)])

buff = framebuf.FrameBuffer(logo, 32, 32, framebuf.MONO_HLSB)

i2c = I2C(0, scl = Pin(1), sda = Pin(0))
devices = i2c.scan()
display = False
if 60 in devices:
    display = True

if display: oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

def second_thread():
    while True:
        mySong.tick()
        utime.sleep(0.05)

def playtone(frequency):
        buzzer.duty_u16(1000)
        buzzer.freq(frequency)

def start():
    red.value(0)
    yellow.value(0)
    green.value(0)
    red2.value(0)
    blue.value(0)
    if display:
        oled.fill(0)
        oled.text('EduPico', 35,0)
        oled.text('v3 - 2022', 35,20)
        oled.text('Jerzy Jasonek', 8,40)

        oled.blit(buff, 0, 0)

        oled.show()

    utime.sleep(1)
    
    _thread.start_new_thread(second_thread, ())

#led test
def led():
    if display:
        oled.fill(0)
        oled.text('Led - test', 5,10)
        oled.show()

    red.value(1)
    yellow.value(0)
    green.value(1)
    red2.value(0)
    blue.value(1)

    for i in range(5):
        red.toggle()
        utime.sleep(0.2)
        yellow.toggle()
        utime.sleep(0.2)
        green.toggle()
        utime.sleep(0.2)
        blue.toggle()
        utime.sleep(0.2)
        red2.toggle()
        utime.sleep(0.2)
        
    red.value(0)
    yellow.value(0)
    green.value(0)
    red2.value(0)
    blue.value(0)

### Police test
def police():
    if display:
        oled.fill(0)
        oled.text('Police - test', 5,10)
        oled.show()

    red2.value(0)
    blue.value(1)

    for i in range(8):
        blue.toggle()
        red2.toggle()
        playtone(3500)
        utime.sleep(0.2)
        red2.toggle()
        blue.toggle()
        playtone(4300)
        utime.sleep(0.2)
        
    red2.value(0)
    blue.value(0)

    buzzer.duty_u16(0)

### Play Song
def music():
    song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
    def bequiet():
        buzzer.duty_u16(0)

    def playsong(mysong):
        for i in range(len(mysong)):
            if (mysong[i] == "P"):
                bequiet()
            else:
                playtone(tones[mysong[i].lower()])
            utime.sleep(0.3)
        bequiet()
    if display:
        oled.fill(0)
        oled.text('Play song', 5,10)
        oled.text('- test', 5,20)
        oled.show()
    playsong(song)

### RGB LED Test
def rgb_led():
    if display:
        oled.fill(0)
        oled.text('RGB LED', 5,10)
        oled.text('- test', 5,20)
        oled.show()
    
    #RGB
    led_r.value(1) #To turn ON led #
    utime.sleep(1)
    led_r.value(0) #To turn OFF led #
    led_g.value(1)
    utime.sleep(1)
    led_g.value(0)
    led_b.value(1)
    utime.sleep(1)
    led_b.value(0)
    
    #Mix
    led_r.value(1) #To turn ON led #
    led_g.value(1)
    utime.sleep(1)
    led_g.value(0)
    led_b.value(1)
    utime.sleep(1)
    led_r.value(0)
    led_g.value(1)
    utime.sleep(1)
    led_g.value(0)
    led_b.value(0)

    led_r_PWM = PWM(Pin(4)) # GPIO pin 4 - red of pico board #
    led_g_PWM = PWM(Pin(5)) # GPIO pin 5 - green of pico board #
    led_b_PWM = PWM(Pin(7)) # GPIO pin 7 - blue of pico board #

    for i in range(65535):
        led_r_PWM.duty_u16(i)
        utime.sleep(0.0001)
        
    for i in range(65535, 0, -1):
        led_r_PWM.duty_u16(i)
        utime.sleep(0.0001)
        
    for i in range(65535):
        led_g_PWM.duty_u16(i)
        utime.sleep(0.0001)
        
    for i in range(65535, 0, -1):
        led_g_PWM.duty_u16(i)
        utime.sleep(0.0001)
        
    for i in range(65535):
        led_b_PWM.duty_u16(i)
        utime.sleep(0.0001)
        
    for i in range(65535, 0, -1):
        led_b_PWM.duty_u16(i)
        utime.sleep(0.0001)

def photoresistor():
    light = 100
    led = PWM(Pin(17))
    led.freq(1000)
    
    def readLight(photoGP):
        photoRes = ADC(Pin(photoPIN))
        light = photoRes.read_u16()
        led.duty_u16(light)
        light = round(light/65535*100,2)
        return light

    while light > 15:
        light = readLight(photoPIN)
        #print("light: " + str(light) +"%")
        if display:
            oled.fill(0)
            oled.text('Photores - test', 5,10)
            oled.text("light: " + str(light) +"%", 5,20)
            oled.text("light<= 15", 5, 40)
            oled.text("- stop test", 5, 50)
            oled.show()
        utime.sleep(0.5) # set a delay between readings
        
    led.duty_u16(0)

### potentiometer - test
def potentiometer_test():
    voltage = 1
    led = PWM(Pin(17))
    while button16.value() != 1:
        voltage = potentiometer.read_u16() * conversion_factor
        #print(voltage)
        if voltage <= 0.01:
            led.duty_u16(0)
        elif voltage >= 3.1:
            led.duty_u16(63000)
        else:
            led.duty_u16(potentiometer.read_u16())
        if display:
            oled.fill(0)
            oled.text('Potentiometer', 5,10)
            oled.text("voltage: " + str(round(voltage, 2)), 5,20)
            oled.text("Push GP16", 5, 40)
            oled.text("- stop test", 5, 50)
            oled.show()
        utime.sleep(0.3)
        
    if display: oled.fill(0)
    led.duty_u16(0)
    utime.sleep(0.5)
    
### buttons - test
def buttons_test():
    red.value(0)
    yellow.value(0)
    green.value(0)
    red2.value(0)
    if display:
        oled.fill(0)
        oled.text('Buttons test', 5,10)
        oled.text("push buttons: ", 5,20)
        oled.text("Reset buttons", 5, 40)
        oled.text("- reload demo", 5, 50)
        oled.show()
    while True:
        if button6.value() == 0:
            red.toggle()
            utime.sleep(0.5)
        if button9.value() == 0:
            yellow.toggle()
            utime.sleep(0.5)
            
        if button15.value():
            green.toggle()
            utime.sleep(0.5)
        
        if button16.value():
            red2.toggle()
            utime.sleep(0.5)
            
    

#demo 
start()
led()
police()
#music()
rgb_led()
photoresistor()
potentiometer_test()
buttons_test()
start()
    
    
