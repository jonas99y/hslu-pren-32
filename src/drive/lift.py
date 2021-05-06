
from typing import Dict
from hal.lift_driver import LiftDriver, LiftDirection
from sensordata import SensorData
from sensormonitor import SensorMonitor


class Lift:
    inbetween = 1
    fullyRetracted = 2
    climbed = 3

    def __init__(self, liftDriver: LiftDriver):
        self._liftDriver = liftDriver
        self._isClimbing = False
        self._isRetracting = False
        self._state = Lift.inbetween

    def get_state(self) -> float:
        return self._state
        pass

    def update_state(self, sensorstate: Dict[str, float]):
        if sensorstate[SensorData.switchLiftUp]:
            self._state = Lift.climbed
        elif sensorstate[SensorData.switchLiftDown]:
            self._state = Lift.fullyRetracted
        else:
            self._state = inbetween

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
        self.update_state(sensorstate)
        state = self.get_state()
        if self._isClimbing:
            if state == Lift.climbed:
                self.stop()
            else:
                self._liftDriver.drive(LiftDirection.down)
        elif self._isRetracting:
            if state == Lift.fullyRetracted:
                self.stop()
            else:
                self._liftDriver.drive(LiftDirection.up)

    def stop(self):
        self._isClimbing = False
        self._isRetracting = False
        self._liftDriver.stop()
