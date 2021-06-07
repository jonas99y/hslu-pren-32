
from time import sleep, time
from averagedsensor import AveragedSensor
from states.context import Context
from states.state import State


class ReadSideSensorState(State):
    def __init__(self, sensorLeft:AveragedSensor, sensorRight:AveragedSensor):
        self._left = sensorLeft
        self._right = sensorRight
    
    def start(self, context: Context) -> "State":
        for i in range(0,10):
            sleep(1)
            print(f"{i}:l: {self._left.read()}")
            sleep(1)
            print(f"{i}:r: {self._right.read()}")