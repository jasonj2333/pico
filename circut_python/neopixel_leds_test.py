"""
NeoPixel example for Pico. Turns the NeoPixels red, green, and blue in sequence.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import time
import board
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 8

pixels = neopixel.NeoPixel(board.GP0, num_pixels, brightness=0.2, auto_write=False)
pixels.brightness = 0.2

while True:
    for i in range(8):
        if i < 4:
            pixels[i] = (0,0,255)
        else:
            pixels[i] = (255,0,0)
        if i == 3 or i==7:
            pixels.show()
            time.sleep(0.2)

            pixels.fill((0,0,0))
            pixels.show()


