from states.context import Context
from states.state import State
from hal.switch import Switch
import time
class StartState(State):
    def __init__(self, nextState:State, startSwitch:Switch):
        super().__init__(nextState)
        self._startSwitch = startSwitch
    
    def start(self, context:Context) -> "State":
        if context.debug:
            return self._nextState
        while self._startSwitch.getState():
            time.sleep(0.1)
        print("starting...")
        return self._nextState