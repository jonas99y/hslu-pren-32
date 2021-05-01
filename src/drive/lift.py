
from hal.lift_driver import LiftDriver, LiftDirection
from sensormonitor import SensorMonitor


class Lift:
    def __init__(self, liftDriver: LiftDriver, monitor: SensorMonitor):
        self._liftDriver = liftDriver
        monitor.monitor('switchLiftUp', self._check_break_up)
        monitor.monitor('switchLiftDown', self._check_break_down)

    def climb(self):
        print('starting to climb')
        self._liftDriver.drive(LiftDirection.down)


    def retract(self):
        self._liftDriver.drive(LiftDirection.up)


    def _check_break_up(self, value):
        if value:
            print('Break lifting up')
            self._liftDriver.stop()

    def _check_break_down(self, value):
        if value:
            print('Break lifting down')
            self._liftDriver.stop()
