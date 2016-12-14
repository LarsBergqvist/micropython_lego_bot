"""
A bot with servos for an Adafruit Feather Huzzah
Requires the Adafruit PWM servo library:
https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library
Uses a FeatherWing servo board attached with i2C
"""
import machine
import servo
import utime

from wheels import Wheels
from hammer import Hammer
from claws import Claws

class Bot(object):
    """
    A robot car with two continuous servos as wheels
    and three standard servos as weapons (hammer and claws)
    """

    def __init__(self):
        # Setup pins to use for i2c and create the servos object
        i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
        servos = servo.Servos(i2c)

        # Create the the servo controlled parts of the bot
        # and assign the control pins to use
        self.wheels = Wheels(servos, 0, 1)
        self.hammer = Hammer(servos, 5)
        self.claws = Claws(servos, 7, 6)

        # A mapping between each command and the
        # corresponding method on the servo objects
        self.action_methods = {
            'F' : self.wheels.fw_step,
            'B' : self.wheels.back_step,
            'L' : self.wheels.turn_left,
            'R' : self.wheels.turn_right,
            'S' : self.wheels.stop,
            'U' : self.hammer.up,
            'D' : self.hammer.down,
            'O' : self.claws.open,
            'C' : self.claws.close
        }

    def _execute(self, action):
        """
        Executes an action according to the mapped methods.
        Input is a character that represents an action.
        """
        if action in self.action_methods:
            self.action_methods[action]()

    def run(self, sequence):
        """
        Input is a string where each character
        represents an action. Each action is executed according
        to the defined action method mapping
        """
        for action in sequence:
            self._execute(action)
