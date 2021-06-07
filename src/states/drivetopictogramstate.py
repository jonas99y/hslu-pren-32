

from time import sleep
from drive.distancedriver import DistanceDriver
from hal.distancesensor import DistanceSensor
from hal.led_driver import Piktogram
from hal.mecanum_driver import Direction
from states.context import Context
from states.state import State

pictos = {
    Piktogram.hammer: {
        'dir': Direction.left,
        Direction.left: 11,
        Direction.right: 115,
    },
    Piktogram.taco: {
        'dir': Direction.left,
        Direction.left: 34,
        Direction.right: 84,
    },
    Piktogram.ruler: {
        'dir': Direction.left,
        Direction.left: 56,
        Direction.right: 56,
    },
    Piktogram.bucket: {
        'dir': Direction.right,
        Direction.left: 65,
        Direction.right: 40,

    },
    Piktogram.pencile: {
        'dir': Direction.right,
        Direction.left: 115,
        Direction.right: 11,
    },
}


class DriveToPictogramState(State):
    def __init__(self, nextState: State, distanceDriver: DistanceDriver):
        self._distanceDriver = distanceDriver
        self._sensorRight = distanceDriver._sensorRight
        self._sensorLeft = distanceDriver._sensorLeft
        self._sensors = {
            Direction.left: self._sensorLeft,
            Direction.right: self._sensorRight,
        }
        super().__init__(nextState)

    def _start(self, context: Context) -> State:
        self._distanceDriver.drive(Direction.forward, 50)
        direction = pictos[context.pictogram]['dir']
        oppositeDirection = Direction.left if direction == Direction.right else Direction.right
        if self._sensors[direction].read() == 0:
            self._distanceDriver.drive(oppositeDirection, 20)
        self._print()
        self._distanceDriver.drive_until_distance_reached(pictos[context.pictogram][direction], direction)
        self._print()
        self._distanceDriver.drive_until_distance_reached(pictos[context.pictogram][oppositeDirection], oppositeDirection)
        self._print()
        self._distanceDriver.drive_until_distance_reached(pictos[context.pictogram][direction], direction)
        self._print()

        self._distanceDriver.drive(Direction.forward, 10)
    def _print(self):
        sleep(0.5)
        print(f'left: {self._sensorLeft.read()}')
        sleep(0.5)
        print(f'right: {self._sensorRight.read()}')
        sleep(0.5)


    # def _drive_to_center_if_necessary(self, targetDir: Direction, targetDistance: float):
    #     oppositeSensor = self._sensorLeft if targetDir == Direction.right else self._sensorRight
    #     distanceToOppositeSide = oppositeSensor.read()
    #     if distanceToOppositeSide < 30:
    #         self._distanceDriver.drive(
    #             Direction.left if targetDir == Direction.right else Direction.left, 20)
