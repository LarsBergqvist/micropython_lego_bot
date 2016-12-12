"""
A bot with servos
Requires the Adafruit PWM servo library:
https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library
"""
import machine
import servo
import utime


from wheels import Wheels
from axe import Axe
from claws import Claws

class Bot(object):
    """
    A robot car with two continuous servos as wheels
    and three standard servos as weapons (axe and claws)
    """
    i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
    servos = servo.Servos(i2c)
    wheels = Wheels(servos, 0, 1)
    axe = Axe(servos, 5)
    claws = Claws(servos, 7, 6)

    ACTION_METHODS = {
        'F' : wheels.fw_step,
        'B' : wheels.back_step,
        'L' : wheels.turn_left,
        'R' : wheels.turn_right,
        'S' : wheels.stop,
        'U' : axe.axe_up,
        'D' : axe.axe_down,
        'O' : claws.open_claws,
        'C' : claws.close_claws
    }

    def __init__(self):
        pass

    def execute(self, action):
        """
        Executes an action.
        Input is a character that represents an action.
        """

        if action in self.ACTION_METHODS:
            self.ACTION_METHODS[action]()

    def run(self, sequence):
        """
        Input is a string where each character
        represents an action. Each action is executed according
        to the defined action method mapping
        """
        for action in sequence:
            self.execute(action)
