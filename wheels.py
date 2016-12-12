import servo
import utime

class Wheels(object):
    """
    Handles the movements of two wheels that are attached
    to two continuous rotation servos
    """
    def __init__(self, servos, servopin_left, servopin_right):
        self.servos = servos
        self.left_wheel = servopin_left
        self.right_wheel = servopin_right
        self.wheel_speed = 10
        self.drift = -0.5
        self.turn_length = 0.5
        self.straight_length = 0.05

    def stop(self):
        """Stops the wheels"""
        self.servos.position(self.left_wheel, degrees=90)
        self.servos.position(self.right_wheel, degrees=90)

    def fw_step(self):
        """Moves the bot forward one step"""
        self.servos.position(self.left_wheel, degrees=90 + self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 - self.wheel_speed + self.drift)
        utime.sleep(self.straight_length)
        self.stop()

    def back_step(self):
        """Moves the bot backwards one step"""
        self.servos.position(self.left_wheel, degrees=90 - self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 + self.wheel_speed + self.drift)
        utime.sleep(self.straight_length)
        self.stop()

    def turn_right(self):
        """Makes a right turn"""
        self.servos.position(self.left_wheel, degrees=90 + self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 + self.wheel_speed)
        utime.sleep(self.turn_length)
        self.stop()

    def turn_left(self):
        """Makes a left turn"""
        self.servos.position(self.left_wheel, degrees=90 - self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 - self.wheel_speed)
        utime.sleep(self.turn_length)
        self.stop()
