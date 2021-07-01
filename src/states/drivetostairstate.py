from Bluetin_Echo.Bluetin_Echo import Echo
from detection.stairfindercamera import StairFinderCamera
from drive.mecanum_driver import Direction, MecanumDriver
from hal.switch import Switch 
from states.context import Context
from states.state import State
import time
class DriveToStairState(State):
    def __init__(self, nextState:State, mecanumDriver:MecanumDriver, l:Echo, r:Echo, sl:Switch, sr:Switch):
        super().__init__(nextState)
        self._mecanumDriver = mecanumDriver
        self.l = l
        self.r = r
        self.sl = sl
        self.sr = sr

    def _start(self, context: Context) -> "State":
        THRESHOLD = 10
        while True:
            self._mecanumDriver.drive(Direction.forward)
            time.sleep(0.1)
            self._mecanumDriver.stop()
            if self.l.read() < THRESHOLD and self.r.read() <THRESHOLD:
                return
            
