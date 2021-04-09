from hal.motor import Motor
from hal.pwm import Pwm

class LiftDirection():
    up = 0
    down = 1


class LiftDriver():
    def __init__(motor: Motor, pwm:Pwm):
        self._motor = motor
        self._pwm = pwm

    def drive(direction:LiftDirection):
