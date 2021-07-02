from picamera.camera import PiCamera
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
        camera = PiCamera()
        pictoCam = PictogramCamera(camera)
        obstacelCam = ObstacleCamera(camera)
        # stairFinderCamera = StairFinderCamera()
        endState = EndState(camera, switchStart)
        climb = Climb(lift, driver)
        hasStepInFrontCheckerState = HasStepInFrontCheckerState(None, None, sensorFrontLeft, sensorSideRight)
        climbstate = ClimbState(hasStepInFrontCheckerState, climb, switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown)
        onStepState = OnStepState(climbstate, movetofront, distanceDriver)
        driveToPictogramState = DriveToPictogramState(endState, distanceDriver)
        hasStepInFrontCheckerState._hasNoStepInFront = driveToPictogramState
        hasStepInFrontCheckerState._hasStepInFront = onStepState

        onFirstStepState = OnFirstStepState(onStepState, distanceDriver, movetofront, obstacelCam)
        firstClimb = ClimbState(onFirstStepState, climb, switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown)
        driveToStairState = DriveToStairState(firstClimb, driver, sensorFrontLeft, sensorFrontRight, switchFrontLeft, switchFrontRight)
        signalPictoState = SignalPictogramState(driveToStairState,ledDriver)
        scanPictoState = ScanPictogramState(signalPictoState, pictoCam, driver)
        # startState = StartState(scanPictoState, switchStart)

        startState = StartState(scanPictoState, switchStart)
        initState = InitState(startState, lift, switchLiftUp, switchLiftDown, ledDriver)
        endState._nextState = initState
        self._currentState = initState
        # self._currentState = ReadSideSensorState(sensorSideLeft, sensorSideRight)
        self._context = Context()
        self._context.debug = False
        self._context.currentStep = 0
        self._context.pictogram = Piktogram.bucket
        self._context.obstacles = numpy.zeros((6,136), dtype=bool).tolist()



    def start(self):
        while True:
            self._currentState = self._currentState.start(self._context)