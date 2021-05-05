
from typing import Dict
from drive.lift import Lift
from sensormonitor import SensorMonitor


class Climb:
    def __init__(self, lift: Lift):
        self._lift = lift
        self._climbInProgress = False

    def start(self):
        if self._climbInProgress:
            print("Climb already in progress")
            return
        else:
            self._climbInProgress = True
            self._lift.climb()

    def cycle(self, sensorstate:Dict[str, float]):
        self._lift.cycle(sensorstate)



