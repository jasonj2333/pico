import array, time
from machine import Pin
import rp2
from rp2 import PIO, StateMachine, asm_pio

# Configure the number of WS2812 LEDs.
NUM_LEDS = 30

@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT,
autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    label("bitloop")
    out(x, 1) .side(0) [T3 - 1]
    jmp(not_x, "do_zero") .side(1) [T1 - 1]
    jmp("bitloop") .side(1) [T2 - 1]
    label("do_zero")
    nop() .side(0) [T2 - 1]

# Create the StateMachine with the ws2812 program, outputting on Pin(0).
sm = StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(0))
# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
pixel_array = array.array("I", [0 for _ in range(NUM_LEDS)])


############################################
# Functions for RGB Coloring
############################################

def updatePixel(brightness=0.2): # dimming colors and updating state machine (state_mach)
    dimmer_array = array.array("I", [0 for _ in range(NUM_LEDS)])
    for ii,cc in enumerate(pixel_array):
        r = int(((cc >> 8) & 0xFF) * brightness) 
        g = int(((cc >> 16) & 0xFF) * brightness) 
        b = int((cc & 0xFF) * brightness) 
        dimmer_array[ii] = (g<<16) + (r<<8) + b 
    sm.put(dimmer_array, 8) # update the state machine with new colors
    
def set_led_color(color):
    for ii in range(len(pixel_array)):
        pixel_array[ii] = (color[1]<<16) + (color[0]<<8) + color[2]

#Color based on RGB (R,G,B)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
off = (0,0,0)

set_led_color(red)
updatePixel(1)
time.sleep(1)
set_led_color(green)
updatePixel(1)
time.sleep(1)
set_led_color(blue)
updatePixel(1)
time.sleep(1)
set_led_color(white)
updatePixel(1)
time.sleep(1)
set_led_color(off)
updatePixel(1)
time.sleep(1)



    