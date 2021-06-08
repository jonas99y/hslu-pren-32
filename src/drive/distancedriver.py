from typing import Dict
from averagedsensor import AveragedSensor
from getposition import get_position
from hal.mecanum_driver import Direction, MecanumDriver
import time

from states.context import Context

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
                sensor = self._get_sensor_by_direction(direction)
                if sensor:
                    distance =sensor.read()
                    if distance != 0 and distance < DISTANCE_THRESHOLD:
                        print(f'stop because distance {distance}')
                        self.stop()
                        return

    def _get_sensor_by_direction(self, direction:Direction):
        sensor = None
        if direction == Direction.left:
            sensor = self._sensorLeft
        elif direction == Direction.right:
            sensor = self._sensorRight
        return sensor

    def drive_to_pos(self, pos:float, context:Context):
        actualLeft = self._sensorLeft.read()
        time.sleep(0.1)
        actualRight = self._sensorRight.read()
        actualPos = get_position(actualLeft, actualRight, context)
        print(f"DistanceDriver: actualPos: {actualPos}")
        print(f"DistanceDriver: actualPos: {actualPos}")
        dif = actualPos-pos
        print(f"DistanceDriver: dif: {dif}")
        absDif = abs(actualPos-pos)
        print(f"DistanceDriver: absDif: {absDif}")
        diretion = Direction.left if dif > 0 else Direction.right
        if diretion == Direction.left:
            print(f"DistanceDriver: drinving Left")
        else:
            print(f"DistanceDriver: drinving right")
        if absDif > 5:
            self.drive(diretion, absDif)

    def drive_until_distance_reached(self, distance:float, direction:Direction):
        sensor = self._get_sensor_by_direction(direction)
        if sensor.read() > distance:
            self._driver.drive(direction)
            while True:
                time.sleep(0.1)
                if sensor.read() <= distance:
                    self._driver.stop()
                    return



    def stop(self):
        self._driver.stop()