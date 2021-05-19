
from states.context import Context
from states.state import State
from hal.switch import Switch

class StartState(State):
    def __init__(self, nextState:State, startSwitch:Switch):
        self._nextState = nextState
        self._startSwitch = startSwitch
    
    def start(self, context:Context) -> "State":
        if self._startSwitch.getState():
            print("starting...")
            return self._nextState
        return self