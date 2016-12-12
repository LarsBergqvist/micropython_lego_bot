import servo
import utime

class Claws(object):
    """
    Handles the movements of two claws that are attached to
    standard servos
    """
    def __init__(self, servos, servopin_left, servopin_right):
        self.servos = servos
        self.left_claw = servopin_left
        self.right_claw = servopin_right
        self.action_wait = 1.0

    def close(self):
        """Rotates the side claws inwards"""
        self.servos.position(self.left_claw, degrees=150)
        self.servos.position(self.right_claw, degrees=80)
        utime.sleep(self.action_wait)

    def open(self):
        """Rotates the side claws outwards"""
        self.servos.position(self.left_claw, degrees=80)
        self.servos.position(self.right_claw, degrees=150)
        utime.sleep(self.action_wait)
