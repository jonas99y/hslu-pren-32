
from hal.led_driver import LedDriver
from states.context import Context
from states.state import State

class SignalPictogramState(State):
    def __init__(self, nextState:State, ledDriver:LedDriver):
        super().__init__(nextState)
        self._ledDriver = ledDriver

    def _start(self, context: Context) -> "State":
        self._ledDriver.ledSet(context.pictogram)
       