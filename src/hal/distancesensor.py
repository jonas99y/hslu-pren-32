
from hal.pin import Pin
import RPi.GPIO as GPIO
import time


class DistanceSensor:
    def __init__(self, trigger: Pin, echo: Pin):
        print(f"init {trigger} , {echo}")
        self._trigger = trigger
        self._echo = echo
        GPIO.setup(self._trigger, GPIO.OUT)
        GPIO.setup(self._echo, GPIO.IN)
        time.sleep(0.1)
        GPIO.output(self._trigger, False)

    def read(self) -> float:
        try:
            timeoutThreshold = 0.01
            functionStart = time.time()
            GPIO.output(self._trigger, True)
            time.sleep(0.00001)
            GPIO.output(self._trigger, False)
            pulse_start = time.time()
            while GPIO.input(self._echo) == 0:
                pulse_start = time.time()
                if pulse_start - functionStart > timeoutThreshold:
                    return 0
            while GPIO.input(self._echo) == 1:
                pulse_end = time.time()
                if pulse_end - functionStart > timeoutThreshold:
                    return 0
            distance = (pulse_end - pulse_start) * 17150
            distance = round(distance+1.15, 3)
            return distance
        except:
            return 0
