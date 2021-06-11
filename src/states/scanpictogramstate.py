
from time import sleep
from detection.pictogramcamera import PictogramCamera
from drive.mecanum_driver import Direction, MecanumDriver
from states.context import Context
from states.state import State

ROTATE_DURATION = 1

class ScanPictogramState(State):
    def __init__(self, nextState: State, cam: PictogramCamera, mecanumDriver:MecanumDriver):
        self._cam = cam
        self._driver = mecanumDriver
        super().__init__(nextState)

    def _start(self, context: Context) -> "State":
        count = 0
        while True:
            result = self._cam.detect_pictogram()
            if result:
                print("detected")
                context.pictogram = result
                self._rotate_back(count)
                return
            else:
                print("not detected")
                self._driver.rotate(Direction.left)
                count+=1
                sleep(ROTATE_DURATION)
                self._driver.stop()


    #either rotate back or just make a full circle anytime.
    def _rotate_back(self, count:int):
        sleep(0.5) # remove when taking actual pictures
        print("rotate back")
        for i in range(count):
            self._driver.rotate(Direction.right)
            sleep(ROTATE_DURATION)
            self._driver.stop()
            sleep(0.2)
