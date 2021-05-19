
from detection.obstaclecamera import ObstacelCamera
from drive.distancedriver import DistanceDriver
from states.context import Context
from states.state import State
from hal.mecanum_driver import MecanumDriver
from stepawaredriver import StepAwareDriver


class OnFirstStepState(State):
    def __init__(self, nextState: State, mecanumDriver: MecanumDriver, obstacleCamera:ObstacelCamera):
        self._nextState = nextState
        self._driver = StepAwareDriver(
            DistanceDriver(mecanumDriver),[0], None)
        self._obstacleCamera = obstacleCamera

    def cycle(self, context: Context) -> "State":
        self._driver.drive_to(10)
        self._obstacleCamera.get_obstacles()
        self._driver.drive_to(45)
        self._obstacleCamera.get_obstacles()
        self._driver.drive_to(80)
        self._obstacleCamera.get_obstacles()
        self._driver.drive_to(115)
        self._obstacleCamera.get_obstacles()
        return self._nextState
