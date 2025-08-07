import RPi.GPIO as gpio


class  DCMotor():


    def __init__(self, in1, in2, en):

        self.motor = dict(
            in1=in1,
            in2=in2,
            en=en
        )

        #  define pins
        gpio.setmode(gpio.BCM)

        gpio.setup(self.motor['in1'], gpio.OUT)
        gpio.setup(self.motor['in2'], gpio.OUT)
        gpio.setup(self.motor['en'], gpio.OUT)

        #  configure PWM frequency
        self.pwm = gpio.PWM(self.motor['en'], 1000) # 1000 Hz frequency

        #  initialize motor parameters
        self.motor_effort=0
        self.motor_direction=(True, True)



    def set_motor_effort(self, effort:float):

        # effort correlates to speed as a function
        # of percent of total voltage supplied (0-1)

        if effort>=0 and effort<=100:
            self.motor_effort = abs(effort)

        else:
            self.motor_effort = 0
            print('invalid voltage command')
        


    def set_motor_direction(self, direction=True):

        # motor direction is defined as a boolean
        # where True is forward and False is backward

        self.motor_direction = (direction, not direction)



    #  parameterize motor
    def drive_motor(self):

        self.pwm.start(self.motor_effort)
        gpio.output(self.motor['in1'], self.motor_direction[0])
        gpio.output(self.motor['in2'], self.motor_direction[1])



    #  terminate the motor at the end of a run
    def stop_motor(self):
        gpio.cleanup()






if __name__=='__main__':

    motor_A = DCMotor(
        in1=23,
        in2=24,
        en=25
    )

    motor_B = DCMotor(
        in1=17,
        in2=27,
        en=22
    )


    motor_A.set_motor_effort(effort=75)
    motor_A.set_motor_direction(direction=False)

    motor_B.set_motor_effort(effort=75)
    motor_B.set_motor_direction(direction=False)


    x=0
    loop_count = 10000
    while x<loop_count:

        x+=.01
        motor_A.drive_motor()
        motor_B.drive_motor()

    motor_A.stop_motor()
    motor_B.stop_motor()