import utime
import servo

class Axe(object):
    """
    Handles the movements of an axe that is attached to
    a standard servo
    """
    def __init__(self, servos, servopin):
        self.servos = servos
        self.servopin = servopin
        self.action_wait = 1.0

    def up(self):
        """Rotates the axe servo so that the axe is put in its upper position"""
        self.servos.position(self.servopin, degrees=50)
        utime.sleep(self.action_wait)

    def down(self):
        """Rotates the axe servo so that the axe is put in its lower position"""
        self.servos.position(self.servopin, degrees=130)
        utime.sleep(self.action_wait)
