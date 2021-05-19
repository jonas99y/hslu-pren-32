from typing import Dict
from averagedsensor import AveragedSensor
from hal.mecanum_driver import Direction, MecanumDriver
import time

CM_PER_S = 33
SPEED = 20
DISTANCE_THRESHOLD = 15
class DistanceDriver:
    def __init__(self, mecanumDriver:MecanumDriver, sensorLeft:AveragedSensor, sensorRight: AveragedSensor):
        self._driver = mecanumDriver
        self._driver.setSpeed(SPEED)
        self._sensorLeft = sensorLeft
        self._sensorRight = sensorRight

    def drive(self, direction:Direction, distance:float):
        print(f'drive {distance} in {direction}')
        endTime = time.time() + distance / CM_PER_S
        
        self._driver.drive(direction)
        while True:
            if time.time() >= endTime:
                print("stop because time is reached")
                self.stop()
                return
            else:
                if direction == Direction.left:
                    sensor = self._sensorLeft
                elif direction == Direction.right:
                    sensor = self._sensorRight
                if sensor:
                    distance =sensor.read()
                    if distance != 0 and distance < DISTANCE_THRESHOLD:
                        print(f'stop because distance {distance}')
                        self.stop()
                        return

    def stop(self):
        self._driver.stop()