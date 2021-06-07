from detection.obstaclecamera import ObstacleCamera
from detection.pictogramcamera import PictogramCamera
from detection.stairfindercamera import StairFinderCamera

from drive.climb import Climb
from states.context import Context
from states.drivetostairstate import DriveToStairState
from states.endstate import EndState
from states.initstate import InitState
from states.onfirststepstate import OnFirstStepState
from states.scanpictogramstate import ScanPictogramState
from states.signalpictogramState import SignalPictogramState
from states.startstate import StartState
from states.climbstate import ClimbState
from config.device_config import *

class StateMachine:
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
        onFirstStepState = OnFirstStepState(endState, distanceDriver, movetofront, ObstacleCamera())
        startState = StartState(onFirstStepState, switchStart)
        initState = InitState(startState, lift, switchLiftUp, switchLiftDown)
        self._currentState = initState
        # self._currentState = ReadSideSensorState(sensorFrontLeft, sensorFrontRight)
        self._context = Context()
        self._context.debug = True


    def start(self):
        while True:
            self._currentState = self._currentState.start(self._context)