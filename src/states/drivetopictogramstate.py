

from time import sleep
from drive.distancedriver import DistanceDriver
from hal.distancesensor import DistanceSensor
from hal.led_driver import Piktogram
from drive.mecanum_driver import Direction
from states.context import Context
from states.state import State
from getposition import get_position

pictos = {
    Piktogram.hammer: {
        'dir': Direction.left,
        'time': 0.7

    },
    Piktogram.taco: {
        'dir': Direction.left,
        'time': 0.4

    },
    Piktogram.ruler: {
        'dir': Direction.left,
        'time': 0

    },
    Piktogram.bucket: {
        'dir': Direction.right,
        'time':0.4


    },
    Piktogram.pencile: {
        'dir': Direction.right,
        'time':0.7

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
        self._distanceDriver.drive(Direction.forward, 70)
        self._distanceDriver.drive_to_pos(67,context)
        self._distanceDriver.drive_to_pos(67,context)
        self._distanceDriver.drive_to_pos(67,context)

        rotateDir = pictos[context.pictogram]['dir']
        rotateTime = pictos[context.pictogram]['time']
        driver = self._distanceDriver._driver
        driver.rotate(rotateDir)
        sleep(rotateTime)
        driver.stop()
        driver.drive(Direction.forward)
        sleep(4)
        driver.stop()

        
        
        # direction = pictos[context.pictogram]['dir']
        # oppositeDirection = Direction.left if direction == Direction.right else Direction.right
        # if self._sensors[direction].read() == 0:
        #     self._distanceDriver.drive(oppositeDirection, 20)
        # self._print()
        # self._distanceDriver.drive_until_distance_reached(pictos[context.pictogram][direction], direction)
        # self._print()
        # self._distanceDriver.drive_until_distance_reached(pictos[context.pictogram][oppositeDirection], oppositeDirection)
        # self._print()
        # self._distanceDriver.drive_until_distance_reached(pictos[context.pictogram][direction], direction)
        # self._print()

        # self._distanceDriver.drive(Direction.forward, 10)
    # def _print(self):
    #     sleep(0.5)
    #     print(f'left: {self._sensorLeft.read()}')
    #     sleep(0.5)
    #     print(f'right: {self._sensorRight.read()}')
    #     sleep(0.5)


    # def _drive_to_center_if_necessary(self, targetDir: Direction, targetDistance: float):
    #     oppositeSensor = self._sensorLeft if targetDir == Direction.right else self._sensorRight
    #     distanceToOppositeSide = oppositeSensor.read()
    #     if distanceToOppositeSide < 30:
    #         self._distanceDriver.drive(
    #             Direction.left if targetDir == Direction.right else Direction.left, 20)
