
from typing import Dict
from drive.lift import Lift
from sensormonitor import SensorMonitor
from hal.mecanum_driver import MecanumDriver, Direction
from sensordata import SensorData
import time

MOVE_FORWARD_TIMESPAN =1
MOVE_FORWARD_SPEED = 20


class Climb:
    def __init__(self, lift: Lift, driver: MecanumDriver):
        self._lift = lift
        self._moveInProgress = False
        self._climbInProgress = False
        self._driver = driver
        self._moveForwardStatedAt: float = 0

    def start(self):
        if self._moveInProgress:
            print("Climb already in progress")
            return
        else:
            self._moveInProgress = True
            self._climbInProgress = True
            self._lift.climb()

    def cycle(self, sensorstate: Dict[str, float]):
        if not self._moveInProgress:
            # self._driver.stop() # todo
            return # nothing to do here!
        liftstate = self._lift.get_state()
        if self._climbInProgress:
            if liftstate == Lift.climbed:
                self._initialize_move_forward()
        else:
            if liftstate == Lift.climbed:
                if time.time() - self._moveForwardStatedAt >= MOVE_FORWARD_TIMESPAN:
                    self._stop_move_forward_and_initalize_retracting()
            if liftstate == Lift.fullyRetracted:
                if self._has_contact_at_front(sensorstate):
                    self._moveInProgress = False
                else:
                    self._initialize_move_to_next_step()
        self._lift.cycle(sensorstate)

    def _has_contact_at_front(self, sensorstate: Dict[str, float]):
        return bool(sensorstate[SensorData.switchFrontLeft]) or bool(sensorstate[SensorData.switchFrontRight])

    def _initialize_move_forward(self):
        self._climbInProgress = False
        self._driver.setSpeed(MOVE_FORWARD_SPEED)
        self._moveForwardStatedAt = time.time()
        self._driver.drive(Direction.forward)

    def _stop_move_forward_and_initalize_retracting(self):
        self._driver.stop()
        self._retractInProgress = True
        self._lift.retract()

    def _initialize_move_to_next_step(self):
        self._moveForwardStatedAt = time.time()
        self._driver.setSpeed(MOVE_FORWARD_SPEED)
        self._driver.drive(Direction.forward)
