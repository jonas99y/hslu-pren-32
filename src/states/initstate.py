
from time import sleep
from drive.lift import Lift
from hal.switch import Switch
from sensordata import SensorData
from states.context import Context
from states.state import State


class InitState(State):
    def __init__(self, nextState: State, lift: Lift, switchLiftUp: Switch, switchLiftDown: Switch):
        super().__init__(nextState)
        self._lift = lift
        self._switchLiftDown = switchLiftDown
        self._switchLiftUp = switchLiftUp

    def _start(self, context: Context) -> "State":
        sleep(0.5)
        self._lift.retract()
        while self._lift.get_state({
            SensorData.switchLiftUp: self._switchLiftUp.getState(),
            SensorData.switchLiftDown: self._switchLiftDown.getState(),
        }) != Lift.fullyRetracted:
            sensorData = {
                SensorData.switchLiftUp: self._switchLiftUp.getState(),
                SensorData.switchLiftDown: self._switchLiftDown.getState(),
            }
            self._lift.cycle(sensorData)
        return 
