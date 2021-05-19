
from states.context import Context
from states.state import State
import sys

class EndState(State):
    def start(self, context: Context) -> "State":
        print("this is the end!")
        sys.exit()