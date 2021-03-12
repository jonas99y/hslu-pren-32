
from hal.pin import Pin
import RPi.GPIO as GPIO

class Pwm():
    def __init__(self, pin:Pin, initalSpeed = 10):
        self._pin = pin
        self._currentSpeed = initalSpeed
        self._initGPIO()

    def _initGPIO(self):
        GPIO.setup(self._pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pin, self._currentSpeed)
        self._pwm.start(100)

    def setSpeed(self, speed:int):
        self._currentSpeed = speed
        self._pwm.ChangeDutyCycle(self._currentSpeed)

    def getSpeed(self)->int:
        return self._currentSpeed
        
