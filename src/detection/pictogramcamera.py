
from hal.led_driver import Piktogram


class PictogramCamera:

    def detect_pictogram(self)-> Piktogram:
        return Piktogram.hammer