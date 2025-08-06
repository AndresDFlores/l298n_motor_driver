import RPi.GPIO as gpio
import time


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
pwm_A.start(75)

pwm_B = gpio.PWM(motor_B['en'], 1000) # 1000 Hz frequency
pwm_B.start(75)

while True:
    gpio.output(motor_A['in1'], False)
    gpio.output(motor_A['in2'], True)

    gpio.output(motor_B['in1'], False)
    gpio.output(motor_B['in2'], True)