import RPi.GPIO as gpio


class  DCMotor():


    @classmethod
    def set_running(cls, running:bool):
        cls.running=running



    @classmethod
    def set_motor_effort(cls, effort:float):

        # effort correlates to speed as a function
        # of percent of total voltage supplied (0-1)

        if effort>=0 and effort<=100:
            cls.motor_effort = abs(effort)

        else:
            cls.motor_effort = 0
            print('invalid voltage command')



    @classmethod
    def set_motor_direction(cls, direction=True):

        # motor direction is defined as a boolean
        # where True is forward and False is backward

        cls.motor_direction = (direction, not direction)



    def __init__(self, in1, in2, en):

        self.motor = dict(
            in1=in1,
            in2=in2,
            en=en
        )

        gpio.setmode(gpio.BCM)


        gpio.setup(self.motor['in1'], gpio.OUT)
        gpio.setup(self.motor['in2'], gpio.OUT)
        gpio.setup(self.motor['en'], gpio.OUT)


        self.set_running(running=False)
        self.set_motor_effort(effort=0)
        self.set_motor_direction(direction=True)


    #  parameterize motor
    def drive_motor(self):

        pwm = gpio.PWM(self.motor['en'], 1000) # 1000 Hz frequency
        pwm.start(self.motor_effort)

        gpio.output(self.motor['in1'], self.motor_direction[0])
        gpio.output(self.motor['in2'], self.motor_direction[1])


    #  terminate the motor at the end of a run
    def stop_motor(self):
        gpio.cleanup()