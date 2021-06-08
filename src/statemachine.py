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
import numpy
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
        scanPictoState = ScanPictogramState(endState, pictoCam, driver)
        # startState = StartState(scanPictoState, switchStart)
        onFirstStepState = OnFirstStepState(endState, distanceDriver, movetofront, ObstacleCamera())
        firstClimb = ClimbState(onFirstStepState, climb, switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown)

        startState = StartState(scanPictoState, switchStart)
        initState = InitState(startState, lift, switchLiftUp, switchLiftDown)
        self._currentState = initState
        # self._currentState = ReadSideSensorState(sensorSideLeft, sensorSideRight)
        self._context = Context()
        self._context.debug = True
        self._context.pictogram = Piktogram.pencile
        self._context.obstacles = numpy.zeros((5,136), dtype=bool).tolist()

        for i in range(46, 59):
            self._context.obstacles[0][i] = True
        for i in range(98, 124):
            self._context.obstacles[1][i] = True


    def start(self):
        while True:
            self._currentState = self._currentState.start(self._context)