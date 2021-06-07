from detection.obstaclecamera import ObstacleCamera
from detection.pictogramcamera import PictogramCamera
from detection.stairfindercamera import StairFinderCamera

from drive.climb import Climb
from hal.led_driver import Piktogram
from states.context import Context
from states.drivetopictogramstate import DriveToPictogramState
from states.drivetostairstate import DriveToStairState
from states.endstate import EndState
from states.hasstepinfrontcheckerstate import HasStepInFrontCheckerState
from states.initstate import InitState
from states.onfirststepstate import OnFirstStepState
from states.onstepstate import OnStepState
from states.readsidesensorstate import ReadSideSensorState
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
        hasStepInFrontCheckerState = HasStepInFrontCheckerState(None, None, sensorFrontLeft, sensorSideRight)
        climbstate = ClimbState(hasStepInFrontCheckerState, climb, switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown)
        onStepState = OnStepState(climbstate, movetofront)
        driveToPictogramState = DriveToPictogramState(endState, distanceDriver)
        hasStepInFrontCheckerState._hasNoStepInFront = driveToPictogramState
        hasStepInFrontCheckerState._hasStepInFront = onStepState

        driveToStairState = DriveToStairState(endState, stairFinderCamera, driver)
        signalPictoState = SignalPictogramState(driveToStairState,ledDriver)
        scanPictoState = ScanPictogramState(signalPictoState, pictoCam)
        # startState = StartState(scanPictoState, switchStart)
        # onFirstStepState = OnFirstStepState(endState, distanceDriver, movetofront, ObstacleCamera())
        startState = StartState(onStepState, switchStart)
        initState = InitState(startState, lift, switchLiftUp, switchLiftDown)
        self._currentState = initState
        # self._currentState = ReadSideSensorState(sensorSideLeft, sensorSideRight)
        self._context = Context()
        self._context.debug = True
        self._context.pictogram = Piktogram.pencile


    def start(self):
        while True:
            self._currentState = self._currentState.start(self._context)