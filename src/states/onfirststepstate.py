
from time import sleep
from detection.obstaclecamera import ObstacleCamera
from drive.distancedriver import DistanceDriver
from drive.movetofrontofstair import MoveToFrontOfStair
from states.context import Context
from states.state import State
from hal.mecanum_driver import Direction


class OnFirstStepState(State):
    def __init__(self, nextState: State, distanceDriver: DistanceDriver, moveToFront:MoveToFrontOfStair, obstacleCamera:ObstacleCamera):
        super().__init__(nextState)
        self._driver = distanceDriver
        self._obstacleCamera = obstacleCamera
        self._moveToFront = moveToFront

    def _start(self, context: Context) -> "State":
        self._moveToFront.start()
        self._driver.drive_until_distance_reached(10, Direction.right)
        self._moveToFront.start()
        self._driver.drive_until_distance_reached(10, Direction.left)
        self._moveToFront.start()
        self._driver.drive_until_distance_reached(50, Direction.right)
        return
