
from typing import Dict
from hal.lift_driver import LiftDriver, LiftDirection
from sensordata import SensorData
from sensormonitor import SensorMonitor


class Lift:
    def __init__(self, liftDriver: LiftDriver):
        self._liftDriver = liftDriver
        self._isClimbing = False
        self._isRetracting = False

    def climb(self):
        if self._isRetracting:
            self._isRetracting = False
        elif self._isClimbing:
            print("already climbing")
        else:
            self._isClimbing = True

    def retract(self):
        if self._isClimbing:
            self._isClimbing = False
        elif self._isRetracting:
            print("already retracting")
        else:
            self._isRetracting = True
            
    def cycle(self, sensorstate: Dict[str, float]):
        if self._isClimbing:
            if sensorstate[SensorData.switchLiftUp]:
                self.stop()
            else:
                self._liftDriver.drive(LiftDirection.down)
        elif self._isRetracting:
            if sensorstate[SensorData.switchLiftDown]:
                self.stop()
            else:
                self._liftDriver.drive(LiftDirection.up)
        

    def stop(self):
        self._isClimbing = False
        self._isRetracting = False
        self._liftDriver.stop()
