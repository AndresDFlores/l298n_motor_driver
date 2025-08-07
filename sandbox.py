import RPi.GPIO as gpio
import time
import math


motor_A = dict(
    in1=23,
    in2=24,
    en=25
)


motor_B = dict(
    in1=17,
    in2=27,
    en=22
)


def init():
    gpio.setmode(gpio.BCM)

    gpio.setup(motor_A['in1'], gpio.OUT)
    gpio.setup(motor_A['in2'], gpio.OUT)
    gpio.setup(motor_A['en'], gpio.OUT)

    gpio.setup(motor_B['in1'], gpio.OUT)
    gpio.setup(motor_B['in2'], gpio.OUT)
    gpio.setup(motor_B['en'], gpio.OUT)



def forward(tf):
    init()

    pwm_A = gpio.PWM(motor_A['en'], 1000) # 1000 Hz frequency
    pwm_A.start(75)

    gpio.output(motor_A['in1'], False)
    gpio.output(motor_A['in2'], True)

    pwm_B = gpio.PWM(motor_B['en'], 1000) # 1000 Hz frequency
    pwm_B.start(75)

    gpio.output(motor_B['in1'], False)
    gpio.output(motor_B['in2'], True)


    time.sleep(tf)
    gpio.cleanup()


def reverse(tf):
    init()

    pwm_A = gpio.PWM(motor_A['en'], 1000) # 1000 Hz frequency
    pwm_A.start(100)

    gpio.output(motor_A['in1'], True)
    gpio.output(motor_A['in2'], False)

    pwm_B = gpio.PWM(motor_B['en'], 1000) # 1000 Hz frequency
    pwm_B.start(100)

    gpio.output(motor_B['in1'], True)
    gpio.output(motor_B['in2'], False)

    time.sleep(tf)
    gpio.cleanup()


# print('FORWARD')
# forward(5)
# print('BACKWARD')
# reverse(5)




init()

pwm_A = gpio.PWM(motor_A['en'], 1000) # 1000 Hz frequency
pwm_B = gpio.PWM(motor_B['en'], 1000) # 1000 Hz frequency



x=0
loop_count = 10000
while x<loop_count:

    x+=.01

    #  change speed
    effort = abs(math.sin(0.001*x))*100
    if effort>100:
        effort = 100
    elif effort<40:
        effort=40


    #  change direction
    dir = (False, True)
    if x>loop_count/2:
        dir = (True, False)


    pwm_A.start(effort)
    gpio.output(motor_A['in1'], dir[0])
    gpio.output(motor_A['in2'], dir[-1])


    pwm_B.start(effort)
    gpio.output(motor_B['in1'], dir[0])
    gpio.output(motor_B['in2'], dir[-1])


gpio.cleanup()