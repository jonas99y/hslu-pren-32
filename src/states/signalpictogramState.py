
from hal.led_driver import LedDriver
from states.context import Context
from states.state import State

class SignalPictogramState(State):
    def __init__(self, nextState:State, ledDriver:LedDriver):
        self._nextState = nextState
        self._ledDriver = ledDriver
    def cycle(self, context: Context) -> "State":
        self._ledDriver.ledSet(context.pictogram)
        return self._nextState
       