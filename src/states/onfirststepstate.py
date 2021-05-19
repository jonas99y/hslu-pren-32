
from detection.obstaclecamera import ObstacelCamera
from drive.distancedriver import DistanceDriver
from states.context import Context
from states.state import State
from hal.mecanum_driver import Direction


class OnFirstStepState(State):
    def __init__(self, nextState: State, distanceDriver: DistanceDriver, obstacleCamera:ObstacelCamera):
        super().__init__(nextState)
        self._driver = distanceDriver
        self._obstacleCamera = obstacleCamera

    def _start(self, context: Context) -> "State":
        self._driver.drive(Direction.left, 100) # drive to the left
        self._driver.drive(Direction.right, 30)
        # take some pictures and stuff inbetween
        self._driver.drive(Direction.right, 30)
        self._driver.drive(Direction.right, 30)

        # start with pathfinding....
        return
