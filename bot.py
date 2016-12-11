"""
A bot with servos
Requires the Adafruit PWM servo library:
https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library
"""
import machine
import servo
import utime


class Bot(object):
    """
    A robot car with two continuous servos as wheels
    and three standard servos as weapons (axe and claws)
    """
    def __init__(self):
        self.i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
        self.servos = servo.Servos(self.i2c)

        # Servo pin assignments
        self.axe = 5
        self.left_claw = 7
        self.right_claw = 6
        self.left_wheel = 0
        self.right_wheel = 1

        # Configurations for the wheels
        self.wheel_speed = 10
        self.drift = -0.5
        self.turn_length = 0.5

        # Configurations for the weapon actions
        self.action_wait = 1.0

    def axe_up(self):
        """Rotates the axe servo so that the axe is put in its upper position"""
        self.servos.position(self.axe, degrees=50)
        utime.sleep(self.action_wait)

    def axe_down(self):
        """Rotates the axe servo so that the axe is put in its lower position"""
        self.servos.position(self.axe, degrees=130)
        utime.sleep(self.action_wait)

    def close_claws(self):
        """Rotates the side claws inwards"""
        self.servos.position(self.left_claw, degrees=150)
        self.servos.position(self.right_claw, degrees=80)
        utime.sleep(self.action_wait)

    def open_claws(self):
        """Rotates the side claws outwards"""
        self.servos.position(self.left_claw, degrees=80)
        self.servos.position(self.right_claw, degrees=150)
        utime.sleep(self.action_wait)

    def stop(self):
        """Stops the wheels"""
        self.servos.position(self.left_wheel, degrees=90)
        self.servos.position(self.right_wheel, degrees=90)

    def fw_step(self):
        """Moves the bot forward one step"""
        self.servos.position(self.left_wheel, degrees=90 + self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 - self.wheel_speed + self.drift)
        utime.sleep(0.5)
        self.stop()

    def back_step(self):
        """Moves the bot backwards one step"""
        self.servos.position(self.left_wheel, degrees=90 - self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 + self.wheel_speed + self.drift)
        utime.sleep(0.5)
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
