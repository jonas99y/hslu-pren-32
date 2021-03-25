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

    def init(self):
        self._isRunning = True
        while self._isRunning:
            print(self._pin)
            # state = GPIO.input(self._pin)
            # if self._prevState != state:
            #     print(f'switch is {state}')
            #     self._prevState = state
            time.sleep(SLEEP)

    def stop(self):
        self._isRunning = False