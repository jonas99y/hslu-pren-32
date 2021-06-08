
from time import sleep
from detection.obstaclecamera import ObstacleCamera
from drive.distancedriver import DistanceDriver
from drive.movetofrontofstair import MoveToFrontOfStair
from getposition import get_position
from states.context import Context
from states.state import State
from hal.mecanum_driver import Direction


class OnFirstStepState(State):
    def __init__(self, nextState: State, distanceDriver: DistanceDriver, moveToFront:MoveToFrontOfStair, obstacleCamera:ObstacleCamera):
        super().__init__(nextState)
        self._driver = distanceDriver
        self._obstacleCamera = obstacleCamera
        self._moveToFront = moveToFront
        self._sensorLeft = distanceDriver._sensorLeft
        self._sensorRight = distanceDriver._sensorRight

    def _start(self, context: Context) -> "State":
        
        self._driver.drive_until_distance_reached(7, Direction.left)
        self._update_obstacles_here(context)

        self._driver.drive_until_distance_reached(80, Direction.right)
        self._update_obstacles_here(context)

        self._driver.drive_until_distance_reached(55, Direction.right)
        self._update_obstacles_here(context)   

        self._driver.drive_until_distance_reached(20, Direction.right)
        self._update_obstacles_here(context)  

        self._driver.drive_until_distance_reached(7, Direction.right)
        self._update_obstacles_here(context)  

    def _update_obstacles_here(self, context):
        position = self._get_pos()
        print(position)
        # context.obstacles = self._obstacleCamera.get_obstacles(context.obstacles, position ,0)

    def _get_pos(self):
        l = self._sensorLeft.read()
        sleep(0.1)
        r = self._sensorRight.read()
        return get_position(l,r,[])
