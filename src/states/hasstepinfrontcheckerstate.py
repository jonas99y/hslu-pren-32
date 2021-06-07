
from hal.distancesensor import DistanceSensor
from states.context import Context
from states.state import State

class HasStepInFrontCheckerState:
    def __init__(self, hasStepInFront: State, hasNoStepInFront:State, sensorFrontLeft:DistanceSensor, sensorFronRight:DistanceSensor):
        self._hasStepInFront = hasStepInFront
        self._hasNoStepInFront = hasNoStepInFront
        self._sensorFrontRight = sensorFronRight
        self._sensorFrontLeft = sensorFrontLeft

    def start(self, context:Context):
        readout = self._sensorFrontLeft.read()
        hasStepInFront = readout > 0 and readout < 20
        if hasStepInFront:
            return self._hasStepInFront
        else:
            return self._hasNoStepInFront