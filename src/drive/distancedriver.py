from typing import Dict
from hal.mecanum_driver import Direction, MecanumDriver
import time

CM_PER_S = 33
SPEED = 20

class DistanceDriver:
    def __init__(self, mecanumDriver:MecanumDriver):
        self._driver = mecanumDriver
        self._isDriving = False
        self._endTime:float = 0
        self._driver.setSpeed(SPEED)

    def drive(self, direction:Direction, distance:float):
        print(f'drive {distance} in {direction}')
        if not self._isDriving:
            self._isDriving = True
            self._endTime = time.time() + distance / CM_PER_S
            self._driver.drive(direction)

    def cycle(self, sensorstate: Dict[str, float]):
        if self._isDriving:
            if time.time() >= self._endTime:
                print("stop because time is reached")
                self.stop()

    def stop(self):
        self._isDriving = False
        self._driver.stop()