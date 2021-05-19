
from typing import Dict

from drive.climb import Climb
from drive.distancedriver import DistanceDriver
from hal.mecanum_driver import Direction
from sensordata import SensorData


class Navigate:
    def __init__(self, climb: Climb, distanceDriver:DistanceDriver):
        self._climb = climb
        self._distanceDriver = distanceDriver
        self._cycleables = [climb, distanceDriver]
        self._started = False
        # self._distanceDriver.drive(Direction.backward, 50)

    def cycle(self, sensorstate: Dict[str, float]):
        # if self._started:
        #     pass
        # else:
        #     self._check_if_start_switch_on_and_start(sensorstate)
        for c in self._cycleables:
            c.cycle(sensorstate)

    def _check_if_start_switch_on_and_start(self, sensorstate: Dict[str, float]):
        if sensorstate[SensorData.switchStart]:
            self._climb.start()
            self._started = True
