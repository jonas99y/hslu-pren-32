
from time import sleep
from detection.obstaclecamera import ObstacleCamera
from drive.distancedriver import DistanceDriver
from drive.movetofrontofstair import MoveToFrontOfStair
from getposition import get_position
from states.context import Context
from states.state import State
from drive.mecanum_driver import Direction


class OnFirstStepState(State):
    def __init__(self, nextState: State, distanceDriver: DistanceDriver, moveToFront:MoveToFrontOfStair, obstacleCamera:ObstacleCamera):
        super().__init__(nextState)
        self._driver = distanceDriver
        self._obstacleCamera = obstacleCamera
        self._moveToFront = moveToFront
        self._sensorLeft = distanceDriver._sensorLeft
        self._sensorRight = distanceDriver._sensorRight

    def _start(self, context: Context) -> "State":
        vals = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]
        for v in vals:
            self._driver.drive_to_pos(v, context)
            self._update_obstacles_here(context)


    def _update_obstacles_here(self, context:Context):
        sleep(0.5)
        position = self._get_pos(context)
        print(position)
        for i,l in enumerate(context.obstacles):
            print(f"---\n{i}")
            print(l)
        context.obstacles = self._obstacleCamera.get_obstacles(context.obstacles, position ,0)

    def _get_pos(self, context:Context):
        l = self._sensorLeft.read()
        sleep(0.1)
        r = self._sensorRight.read()
        return get_position(l,r,context)
