
from hal.pin import Pin
import RPi.GPIO as GPIO

class Motor():
    def __init__(self, forward:Pin, backward: Pin):
        self._forward = forward
        self._backward = backward
        self._initGPIO()


    def _initGPIO(self):
        GPIO.setup(self._forward, GPIO.OUT)
        GPIO.setup(self._backward, GPIO.OUT)

    def forward(self):
        GPIO.output(self._backward, GPIO.LOW)
        GPIO.output(self._forward, GPIO.HIGH)
        

    def backwards(self):
        GPIO.output(self._forward, GPIO.LOW)
        GPIO.output(self._backward, GPIO.HIGH)


    def stop(self):
        GPIO.output(self._forward, GPIO.LOW)
        GPIO.output(self._backward, GPIO.LOW)