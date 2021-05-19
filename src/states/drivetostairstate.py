from detection.stairfindercamera import StairFinderCamera
from hal.mecanum_driver import Direction, MecanumDriver
from states.context import Context
from states.state import State
import time
class DriveToStairState(State):
    def __init__(self, nextState:State, stairFinderCamera:StairFinderCamera, mecanumDriver:MecanumDriver):
        self._nextState = nextState
        self._mecanumDriver = mecanumDriver
        self._stairFinderCamera = stairFinderCamera
    
    def cycle(self, context: Context) -> "State":
        if self._stairFinderCamera.is_stair_in_front():
            return self._nextState
        else:
            self._mecanumDriver.rotate(Direction.right)
            time.sleep(1) #1s = about 90 degrees
            self._mecanumDriver.stop()
            return self