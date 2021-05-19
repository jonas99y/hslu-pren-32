
from states.context import Context


class State:
    def __init__(self, nextState:"State"):
        self._nextState = nextState
    
    def start(self, context:Context) -> "State":
        self.next()

    def next(self)-> "State":
        return self._nextState