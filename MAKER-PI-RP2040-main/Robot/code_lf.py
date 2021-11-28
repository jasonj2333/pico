#
# Maker Pi RP2040 Mobile Robot: Part 2 - Line Following
#
# Tutorial
# - https://tutorial.cytron.io/
#
# Raspberry Pi Pico
# - Maker Pi Pico https://my.cytron.io/p-maker-pi-pico?tracking=idris
# - LiPo 3.7V 1300mAH https://my.cytron.io/p-lipo-rechargeable-battery-3.7v-1300mah?tracking=idris
# - Maker Line https://my.cytron.io/p-maker-line-simplifying-line-sensor-for-beginner?tracking=idris
# - VL53L0X V2 Sensor https://my.cytron.io/p-vl53l0x-v2-laser-tof-distance-sensor-module?tracking=idris
# - micro:servo 360 (Continuous) https://my.cytron.io/p-micro-servo-360-degrees-digital-servo-for-micro-bit-42148?tracking=idris
# - Wheel for FS90R https://my.cytron.io/p-wheel-for-fs90r?tracking=idris
# - M3 PCB Stand (screw & nut)15mm https://my.cytron.io/p-m3-pcb-stand-screw-and-nut-15mm?tracking=idris
# - Bolt M3 x 6mm https://my.cytron.io/p-bolt-m3x6mm?tracking=idris
#
# Additional Libraries
# - simpleio.mpy
# - neopixel.mpy
# - adafruit_motor
# - adafruit_vl53l0x.mpy
#
# Download CircuitPython Libraries Bundle - https://circuitpython.org/libraries
#
# Update:
# 3 Aug 2021 - Tested with CircuitPython Pico 7.0.0
#

import board
import digitalio
import analogio
import neopixel
import simpleio
import time
import pwmio
import busio
from adafruit_motor import motor
import adafruit_vl53l0x

btn1 = digitalio.DigitalInOut(board.GP20)
btn1.direction = digitalio.Direction.INPUT

btn2 = digitalio.DigitalInOut(board.GP21)
btn2.direction = digitalio.Direction.INPUT

sen_an = analogio.AnalogIn(board.GP28)

sen_cal = digitalio.DigitalInOut(board.GP7)
sen_cal.direction = digitalio.Direction.OUTPUT
sen_cal.value = True

# create a PWMOut object on Pin GP12.
pwm1 = pwmio.PWMOut(board.GP12, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP13, duty_cycle=2 ** 15, frequency=50)

# Initialize DC motors
m1a = pwmio.PWMOut(board.GP8, frequency=50)
m1b = pwmio.PWMOut(board.GP9, frequency=50)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(board.GP10, frequency=50)
m2b = pwmio.PWMOut(board.GP11, frequency=50)
motor2 = motor.DCMotor(m2a, m2b)

motor1.throttle = 0
motor2.throttle = 0


piezo_pin = board.GP22
tempo = 0.6
tone_freq = [262, 294, 330, 392, 0, 330, 392]
tone_duration = [4, 4, 4, 4, 4, 4, 2]
def melody_start():
    for i in range(len(tone_freq)):
        simpleio.tone(piezo_pin, tone_freq[i], tempo/tone_duration[i])


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


def calibrate():
    print("Calibrating...")

    sen_cal.value = False
    simpleio.tone(piezo_pin, 262, 0.1)
    time.sleep(2)
    sen_cal.value = True

    motor1.throttle = -0.5
    motor2.throttle = -0.5
    time.sleep(0.5)
    motor1.throttle = 0
    motor2.throttle = 0
    time.sleep(0.5)
    motor1.throttle = 0.5
    motor2.throttle = 0.5
    time.sleep(1)
    motor1.throttle = 0
    motor2.throttle = 0
    time.sleep(0.5)
    motor1.throttle = -0.5
    motor2.throttle = -0.5
    time.sleep(0.5)
    motor1.throttle = 0
    motor2.throttle = 0

    sen_cal.value = False
    time.sleep(0.5)
    sen_cal.value = True


last_proportional = 0
kp = 0.9
kd = 5
def line_follow_pd(data, setpoint):
    global last_proportional
    global kp
    global kd
    speed_left = 1
    speed_right = -1

    proportional = data - setpoint
    derivative = proportional - last_proportional
    last_proportional = proportional

    power_different = (proportional * kp) + (derivative * kd)

    if power_different < -1:
        power_different = -1
    if power_different > 1:
        power_different = 1

    if power_different < 0:
        speed_left = speed_left + power_different
    else:
        speed_right = speed_right + power_different

    motor1.throttle = speed_left
    motor2.throttle = speed_right


follow_line = False

simpleio.tone(piezo_pin, 262, 0.1)
simpleio.tone(piezo_pin, 392, 0.1)

while True:
    if btn1.value == False:
        calibrate()

    if btn2.value == False:
        print("Move!")
        follow_line = not follow_line
        while btn2.value == False:
            pass
        if follow_line == True:
            melody_start()

    maker_line = get_voltage(sen_an)
    # print("Maker Line: {:.2f}V".format(maker_line))

    if follow_line == True:
        line_follow_pd(maker_line, 1.6)
    else:
        motor1.throttle = 0
        motor2.throttle = 0