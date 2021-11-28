# *************************************************
# Out-of-the-box Demo for Cytron Maker Pi RP2040
# 
# This demo code is written in CircuitPython and it serves
# as an easy quality check when you first receive the board.
#
# It plays a melody upon power up (slide power switch to ON)
# and shows running lights (blue LEDs) at the same time.
# Then the two RGB LEDs will animate the colors, while the 
# program checking push buttons' state, repeatedly.
# 
# Press GP20 button to play a short melody, lights up all 
# blue LEDs, move servo motors to 0 degree and run DC motors
# at 50% and -50% speeds.
# Press GP21 button to play another melody, turn off all blue 
# LEDs, move servo motors to 180 degree & brake DC motors.
# 
# Maker Pi RP2040 also has four DC motors quick test buttons 
# built-in. You may press the onboard M1A, M1B, M2A or M2B 
# push buttons to run your motors without writing any code.
#
# More info: 
# http://www.cytron.io/p-maker-pi-rp2040
# https://circuitpython.org/board/raspberry_pi_pico
#
# Email: support@cytron.io
# *************************************************
import board
import digitalio
import neopixel
import simpleio
import busio
import time
import pwmio
from adafruit_motor import servo, motor
import adafruit_vl53l0x
from random import randint


# Initialize buttons
btn1 = digitalio.DigitalInOut(board.GP20)
btn2 = digitalio.DigitalInOut(board.GP21)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP

# Initialize DC motors
m1a = pwmio.PWMOut(board.GP8, frequency=50)
m1b = pwmio.PWMOut(board.GP9, frequency=50)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(board.GP10, frequency=50)
m2b = pwmio.PWMOut(board.GP11, frequency=50)
motor2 = motor.DCMotor(m2a, m2b)
# Initialize I2C bus and sensor.
i2cl = busio.I2C(board.GP5, board.GP4)
i2cp = busio.I2C(board.GP3, board.GP2)
vl53l = adafruit_vl53l0x.VL53L0X(i2cl)
vl53p = adafruit_vl53l0x.VL53L0X(i2cp)
piezo = board.GP22

# -------------------------------------------------
# FOREVER LOOP: Check buttons & animate RGB LEDs
# -------------------------------------------------
start = False

while True:
    
    
    # Check button 1 (GP20)
    if not btn1.value:  # button 1 pressed
        start = True
    # Check button 2 (GP21)
    elif not btn2.value:  # button 2 pressed
        start = False
    
    if start:
        # Move motors at 50% speed
        motor1.throttle = 0.8  # motor1.throttle = 1 or -1 for full speed
        motor2.throttle = 0.8  
        distancel = vl53l.range
        distancep = vl53p.range
        #print("Rangel: {0}mm".format(distancel))
        #print("Rangep: {0}mm".format(distancep))
        if distancel < 150 or distancep < 150:
            simpleio.tone(piezo, 450, 0.1)
            
            # Move motors at 50% speed
            motor1.throttle = -0.5  # motor1.throttle = 1 or -1 for full speed
            motor2.throttle = -0.5   
            time.sleep(0.5)
        
            # Move motors at 50% speed
            if distancel <= distancep:
                motor1.throttle = 0.5  # motor1.throttle = 1 or -1 for full speed
                motor2.throttle = -0.5
            else:
                motor1.throttle = -0.5  # motor1.throttle = 1 or -1 for full speed
                motor2.throttle = 0.5              
            turn_time = randint(2,4)/10
            time.sleep(turn_time)
        
       
    
    


        
    
            
        
