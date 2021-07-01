
from time import sleep
from drive.lift import Lift
from hal.led_driver import LedDriver, Piktogram
from hal.switch import Switch
from sensordata import SensorData
from states.context import Context
from states.state import State


class InitState(State):
    def __init__(self, nextState: State, lift: Lift, switchLiftUp: Switch, switchLiftDown: Switch, led:LedDriver):
        super().__init__(nextState)
        self._lift = lift
        self._switchLiftDown = switchLiftDown
        self._switchLiftUp = switchLiftUp
        self._ledDriver = led

    def _start(self, context: Context) -> "State":
        self._lift.retract()
        self._ledDriver.ledSet(Piktogram.none)
        while self._lift.get_state({
            SensorData.switchLiftUp: self._switchLiftUp.getState(),
            SensorData.switchLiftDown: self._switchLiftDown.getState(),
        }) != Lift.fullyRetracted:
            sensorData = {
                SensorData.switchLiftUp: self._switchLiftUp.getState(),
                SensorData.switchLiftDown: self._switchLiftDown.getState(),
            }
            self._lift.cycle(sensorData)
        print("init done")
        return 
