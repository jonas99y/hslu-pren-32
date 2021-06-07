from time import sleep
from hal.distancesensor import DistanceSensor
from hal.mecanum_driver import Direction, MecanumDriver
from hal.switch import Switch
from hal.motor import Motor
from hal.pwm import Pwm

SPEED = 20
TARGET_DISTANCE = 4.6
THRESHOLD = 0.4


class MoveToFrontOfStair:
    def __init__(self, lf: Motor, lb: Motor, rf: Motor, rb: Motor, mecanumDriver: MecanumDriver, pwm: Pwm, switchLeft: Switch, switchRight: Switch, sensorLeft: DistanceSensor, sensorRight: DistanceSensor):
        self._lf = lf
        self._lb = lb
        self._rf = rf
        self._rb = rb
        self._pwm = pwm
        self._left = switchLeft
        self._right = switchRight
        self._sensorRight = sensorRight
        self._sensorLeft = sensorLeft
        self._mecanumDriver = mecanumDriver

    def start(self):
        sleep(0.1)
        distanceLeft = self._sensorLeft.read()
        sleep(0.1)
        distanceRight = self._sensorRight.read()

        leftCloseToTarget = self._distance_close_to_target(distanceLeft)
        rightCloseToTarget = self._distance_close_to_target(distanceRight)

        if (not leftCloseToTarget) and (not rightCloseToTarget):
            # we are far away..
            self._mecanumDriver.drive(Direction.forward)
            sleep(0.1)
            self._mecanumDriver.stop()
            self.start()
        else:
            if leftCloseToTarget and not rightCloseToTarget:
                self._mecanumDriver.rotate(Direction.left)
                sleep(0.1)
                self._mecanumDriver.stop()
                self.start()
            elif rightCloseToTarget and not leftCloseToTarget:
                self._mecanumDriver.rotate(Direction.right)
                sleep(0.1)
                self._mecanumDriver.stop()
                self.start()
        

        # self._pwm.setSpeed(SPEED)
        # while not self._contact():
        #     if not self._left.getState():
        #         self._lb.forward()
        #         self._lf.forward()
        #     else:
        #         self._lb.stop()
        #         self._lf.stop()
        #     if not self._right.getState():
        #         self._rb.forward()
        #         self._rf.forward()
        #     else:
        #         self._rb.stop()
        #         self._rf.stop()
        # self.stop()
        # sleep(0.2)

    def _distance_close_to_target(self, distance: float) -> bool:
        return abs(distance - TARGET_DISTANCE) < THRESHOLD

    def stop(self):
        self._lf.stop()
        self._lb.stop()
        self._rf.stop()
        self._rf.stop()

    def _contact(self) -> bool:
        return self._left.getState() and self._right.getState()
