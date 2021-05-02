from time import time
from hal.pin import Pin
import RPi.GPIO as GPIO
import time

SLEEP = 0.001

class Switch():
    def __init__(self, pin: Pin):
        self._pin = pin
        self._isRunning = False
        self._prevState = None
        GPIO.setup(self._pin, GPIO.IN)

    def getState(self) -> bool:
        return GPIO.input(self._pin)