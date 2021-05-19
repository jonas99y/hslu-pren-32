
from typing import Dict, List, Union
from drive.distancedriver import DistanceDriver
from hal.mecanum_driver import Direction
from sensordata import SensorData

WIDTH = 130
DEVICE_WIDTH = 20
CENTER_AT = 65
MIN_DISTANCE_LEFT_AND_RIGHT = 20


class StepDirection():
    left = Direction.left
    right = Direction.right


class StepAwareDriver:
    def __init__(self, distanceDriver: DistanceDriver, obstacles: List[bool], startposition: Union[float, None]):
        self._distanceDriver = distanceDriver
        self._distancePerObstacelEntry = WIDTH / len(obstacles)
        self._obstacles = obstacles
        self._position = startposition
        self._isDistanceDriverDriving = False
        self._isDriving = False
        self._target = None
        self._direction = None

    def drive_to_center(self):
        self.drive_to(CENTER_AT)

    def drive_to(self, value: float):
        self._target = value
        self._isDriving = True

    def cycle(self, sensorstate: Dict[str, float]):
        if not self._isDriving:
            return

        if not self._isDistanceDriverDriving:  # drive not yet started
            direction = self._get_direction()
            self._direction = direction
            maxPossibleDriveDistance = self._get_distance_to_next_obstace_or_border(
                direction)
            print(self._position)
            print(self._target)
            print(abs(self._position-self._target))
            distance = abs(self._position-self._target)
            if distance >  maxPossibleDriveDistance:
                print(f'cannot drive to where you want!{self._target}, {maxPossibleDriveDistance} > {distance}')
            self._distanceDriver.drive(direction, distance)
            self._isDistanceDriverDriving = True
        else:
            if not self._distanceDriver._isDriving:  # drive ended
                self._isDistanceDriverDriving = False
                self._isDriving = False
            else:  # drive in progress
                sensorOfIntrest = sensorstate[SensorData.sensorSideLeft] if self._direction == StepDirection.left else sensorstate[SensorData.sensorSideRight]
                if sensorOfIntrest < MIN_DISTANCE_LEFT_AND_RIGHT:
                    print("stop because there is something close!")
                    self._distanceDriver.stop()
                else:
                    print(sensorOfIntrest)
        self._distanceDriver.cycle(self._distanceDriver)

    def _get_direction(self) -> StepDirection:
        if self._position > self._target:
            return StepDirection.left
        else:
            return StepDirection.right

    def _get_postion_in_obstacle_list(self) -> int:
        return round(self._position / self._distancePerObstacelEntry)

    def _get_distance_to_next_obstace_or_border(self, direction: StepDirection):
        listIndex = self._get_postion_in_obstacle_list()
        if direction == StepDirection.left:
            relevantPartOfList = self._obstacles[0:listIndex]
        else:
            relevantPartOfList = self._obstacles[listIndex:len(
                self._obstacles)]

        distance = 0
        for isObstacle in relevantPartOfList:
            if isObstacle:
                break
            else:
                distance += self._distancePerObstacelEntry
        return distance
