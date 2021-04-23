from hal.pin import Pin
from hal.led import Led
import RPi.GPIO as GPIO
import time

class Piktogram():
    none = 0
    hammer = 1
    taco = 2
    ruler = 3
    bucket = 4
    pencile = 5

class LedDriver():
    def __init__(self, ledA:Led, ledB:Led, ledC:Led):
        self._ledA = ledA
        self._ledB = ledB
        self._ledC = ledC

    def ledSet(self, piktogram:Piktogram):
        if piktogram == Piktogram.none:
            self._ledA.low()
            self._ledB.low()
            self._ledC.low()
            print("Led: none")
        elif piktogram == Piktogram.hammer:
            self._ledA.high()
            self._ledB.high()
            self._ledC.high() 
            print("Led: hammer")  
        elif piktogram == Piktogram.taco:
            self._ledA.high()
            self._ledB.high()
            self._ledC.low()
            print("Led: taco") 
        elif piktogram == Piktogram.ruler:
            self._ledA.high()
            self._ledB.low()
            self._ledC.high()
            print("Led: ruler") 
        elif piktogram == Piktogram.bucket:
            self._ledA.high()
            self._ledB.low()
            self._ledC.low()
            print("Led: bucket")     
        elif piktogram == Piktogram.pencile:
            self._ledA.low()
            self._ledB.high()
            self._ledC.high()
            print("Led: pencile")  

    def ledBlink(self, piktogram:Piktogram):
        if piktogram == Piktogram.none:
            print("wrong case (ledBlink)")
        elif piktogram == Piktogram.hammer:
            print("LedBlink: hammer")
            for i in range(10):
                LedDriver.ledSet(Piktogram.hammer)
                time.sleep(1)
                LedDriver.ledSet(Piktogram.none)
                time.sleep(1)
            print("LedBlink: end")
        elif piktogram == Piktogram.taco:
            print("LedBlink: taco")
            for i in range(10):
                LedDriver.ledSet(Piktogram.taco)
                time.sleep(1)
                LedDriver.ledSet(Piktogram.none)
                time.sleep(1)
            print("LedBlink: end")
        elif piktogram == Piktogram.ruler:
            print("LedBlink: ruler")
            for i in range(10):
                LedDriver.ledSet(Piktogram.ruler)
                time.sleep(1)
                LedDriver.ledSet(Piktogram.none)
                time.sleep(1)
            print("LedBlink: end")
        elif piktogram == Piktogram.bucket:
            print("LedBlink: bucket")
            for i in range(10):
                LedDriver.ledSet(Piktogram.bucket)
                time.sleep(1)
                LedDriver.ledSet(Piktogram.none)
                time.sleep(1)
            print("LedBlink: end")
        elif piktogram == Piktogram.pencile:
            print("LedBlink: pencile")
            for i in range(10):
                LedDriver.ledSet(Piktogram.pencile)
                time.sleep(1)
                LedDriver.ledSet(Piktogram.none)
                time.sleep(1)
            print("LedBlink: end")
            