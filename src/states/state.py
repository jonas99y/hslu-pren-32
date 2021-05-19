
from states.context import Context


class State:
    def __init__(self, nextState:"State"):
        self._nextState = nextState
    
    def start(self, context:Context) -> "State":
        self._start(context)
        return self._nextState

    def _start(self, context:Context) -> "State":
        pass