
from states.context import Context
from states.state import State
from drive.movetofrontofstair import MoveToFrontOfStair

class OnStepState(State):
    def __init__(self, nextState: State, moveToFront:MoveToFrontOfStair):
        self._moveToFront = moveToFront
        super().__init__(nextState)


    def _start(self, context:Context):
        self._moveToFront.start()
        # TODO save the current position to context somewhere...
        

    def _navigate_left_right(self, context:Context):
        pass