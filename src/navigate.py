
from typing import Dict
from detection.pictogramcamera import PictogramCamera
from detection.stairfindercamera import StairFinderCamera

from drive.climb import Climb
from drive.distancedriver import DistanceDriver
from hal.mecanum_driver import Direction
from sensordata import SensorData
from states.context import Context
from states.drivetostairstate import DriveToStairState
from states.endstate import EndState
from states.initstate import InitState
from states.scanpictogramstate import ScanPictogramState
from states.signalpictogramState import SignalPictogramState
from states.startstate import StartState
from states.climbstate import ClimbState
from stepawaredriver import StepAwareDriver
from config.device_config import *

class Navigate:
    def __init__(self):
        pictoCam = PictogramCamera()
        stairFinderCamera = StairFinderCamera()
        endState = EndState()
        climb = Climb(lift, driver)
        climbstate = ClimbState(endState, climb, switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown)
        driveToStairState = DriveToStairState(endState, stairFinderCamera, driver)
        signalPictoState = SignalPictogramState(driveToStairState,ledDriver)
        scanPictoState = ScanPictogramState(signalPictoState, pictoCam)
        # startState = StartState(scanPictoState, switchStart)
        startState = StartState(climbstate, switchStart)
        initState = InitState(startState, lift, switchLiftUp, switchLiftDown)

        self._currentState = initState
        self._context = Context()

    def cycle(self, sensorstate: Dict[str, float]):
        self._currentState = self._currentState.start(self._context)

