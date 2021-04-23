from hal.pin import Pin
import RPi.GPIO as GPIO

class Led():
    def __init__(self, led:Pin):
        self._led = led
        self._initGPIO()

    def _initGPIO(self):
        GPIO.setup(self._led, GPIO.OUT)

    def high(self):
        GPIO.output(self._led, GPIO.HIGH)

    def low(self):
        GPIO.output(self._led, GPIO.LOW)