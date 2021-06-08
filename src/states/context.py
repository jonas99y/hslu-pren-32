
from typing import List
from hal.led_driver import Piktogram

class Context:
    def __init__(self):
        self.pictogram: Piktogram = Piktogram.none
        self.debug: bool = False
        self.obstacles: List[List[bool]]
        self.lastKnowPosition = 0
        self.currentStep=0

    def get_current_obstacles(self)-> List[bool]:
        return self.obstacles[self.currentStep]
    def get_next_obstacles(self)-> List[bool]:
        return self.obstacles[self.currentStep+1]