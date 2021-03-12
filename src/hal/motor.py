
from hal.pin import Pin


class Motor():
    def __init__(self, forward:Pin, backward: Pin, pwm: Pin):
        self.forward = forward
        self.backward = backward
        self.pwm = pwm