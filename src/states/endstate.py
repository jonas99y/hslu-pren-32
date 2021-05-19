
from states.context import Context
from states.state import State
import sys

class EndState(State):
    def __init__(self):
        pass
    def _start(self, context: Context) -> "State":
        print("this is the end!")
        sys.exit()