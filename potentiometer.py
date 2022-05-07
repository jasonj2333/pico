from machine import Pin, PWM, ADC

pwm = PWM(Pin(11))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
    duty = adc.read_u16()
    print(duty)
    pwm.duty_u16(duty)