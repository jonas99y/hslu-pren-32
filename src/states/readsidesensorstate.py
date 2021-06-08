
from time import sleep, time
from averagedsensor import AveragedSensor
from getposition import get_position
from states.context import Context
from states.state import State


class ReadSideSensorState(State):
    def __init__(self, sensorLeft:AveragedSensor, sensorRight:AveragedSensor):
        self._left = sensorLeft
        self._right = sensorRight
    
    def start(self, context: Context) -> "State":
        for i in range(0,1000):
            sleep(0.5)
            l = self._left.read()
            print(f"{i}:l: {l}")
            sleep(0.5)
            r = self._right.read()
            print(f"{i}:r: {r}")
            print(f"get_position(): {get_position(l,r,[])}")
            print("\n-----\n")