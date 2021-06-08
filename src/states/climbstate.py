from drive.climb import Climb
from sensordata import SensorData
from states.context import Context
from states.state import State
from hal.switch import Switch


class ClimbState(State):
    def __init__(self, nextState:State, climb: Climb, switchLeft: Switch, switchRight: Switch, switchLiftUp:Switch, switchLiftDown:Switch):
        super().__init__(nextState)
        self._climb = climb
        self._switchLeft = switchLeft
        self._switchRight = switchRight
        self._switchLiftDown = switchLiftDown
        self._switchLiftUp = switchLiftUp

    def _start(self, context: Context) -> "State":
        self._climb.start()
        while True:
            sensorData = {
                SensorData.switchFrontLeft: self._switchLeft.getState(),
                SensorData.switchFrontRight: self._switchRight.getState(),
                SensorData.switchLiftUp: self._switchLiftUp.getState(),
                SensorData.switchLiftDown: self._switchLiftDown.getState(),
            }
            self._climb.cycle(sensorData)
            if not self._climb._moveInProgress:
                self._climb._driver.stop() #HACK
                print("next step reached...")
                context.currentStep+=1
                return