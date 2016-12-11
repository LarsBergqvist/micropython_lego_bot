import machine
import servo
import utime


class Bot(object):
    def __init__(self):
        self.i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
        self.servos = servo.Servos(self.i2c)

        # Servo pin assignments
        self.hammer = 5
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

    def hammer_up(self):
        self.servos.position(self.hammer, degrees=50)
        utime.sleep(self.action_wait)

    def hammer_down(self):
        self.servos.position(self.hammer, degrees=130)
        utime.sleep(self.action_wait)

    def close_claws(self):
        self.servos.position(self.left_claw, degrees=150)
        self.servos.position(self.right_claw, degrees=80)
        utime.sleep(self.action_wait)

    def open_claws(self):
        self.servos.position(self.left_claw, degrees=80)
        self.servos.position(self.right_claw, degrees=150)
        utime.sleep(self.action_wait)

    def stop(self):
        self.servos.position(self.left_wheel, degrees=90)
        self.servos.position(self.right_wheel, degrees=90)

    def fw_step(self):
        self.servos.position(self.left_wheel, degrees=90 + self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 - self.wheel_speed + self.drift)
        utime.sleep(0.5)
        self.stop()

    def back_step(self):
        self.servos.position(self.left_wheel, degrees=90 - self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 + self.wheel_speed + self.drift)
        utime.sleep(0.5)
        self.stop()

    def turn_right(self):
        self.servos.position(self.left_wheel, degrees=90 + self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 + self.wheel_speed)
        utime.sleep(self.turn_length)
        self.stop()

    def turn_left(self):
        self.servos.position(self.left_wheel, degrees=90 - self.wheel_speed)
        self.servos.position(self.right_wheel, degrees=90 - self.wheel_speed)
        utime.sleep(self.turn_length)
        self.stop()
