
from hal.led_driver import Piktogram

class Context:
    def __init__(self):
        self.pictogram: Piktogram = Piktogram.none