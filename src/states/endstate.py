
from time import sleep
from hal.switch import Switch
from states.context import Context
from states.state import State
import sys

class EndState(State):
    def __init__(self, camera, switch:Switch):
        self.camera = camera
        self.switch = switch
        pass
    def _start(self, context: Context) -> "State":

        print("this is the end!")
        while True:
            if self.switch.getState():
                return
            else:
                sleep(0.5)