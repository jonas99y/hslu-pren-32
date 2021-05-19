from drive.climb import Climb
from sensordata import SensorData
from states.context import Context
from states.state import State
from hal.switch import Switch


class ClimbState(State):
    def __init__(self,nextState:State, climb: Climb, switchLeft: Switch, switchRight: Switch):
        super().__init__(nextState)
        self._climb = climb
        self._switchLeft = switchLeft
        self._switchRight = switchRight

    def start(self, context: Context) -> "State":
        self._climb.start()
        while True:
            sensorData = {
                SensorData.switchFrontLeft: self._switchLeft.getState(),
                SensorData.switchFrontRight: self._switchRight.getState()
            }
            self._climb.cycle(sensorData)
            if not self._climb._moveInProgress:
                print("next step reached...")
                self.next()