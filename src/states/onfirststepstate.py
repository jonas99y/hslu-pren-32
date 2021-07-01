
from time import sleep
from pathfinding.core.diagonal_movement import DiagonalMovement

from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
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
        vals = [0,20,30,40,50,60,70,80,90,100,110,120]
        for v in vals:
            self._driver.drive_to_pos(v, context)
            self.print_path_und_so(context)
            self._update_obstacles_here(context)
        self.print_path_und_so(context)
        self._fix_the_matrix(context)
        self.print_path_und_so(context)


    def print_path_und_so(self, context:Context):
        grid = Grid(matrix=context.obstacles, inverse=True)
        start = grid.node(0, context.currentStep)
        end = grid.node(70, 5)
        finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        print(grid.grid_str(path=path, start=start, end=end))
        print(path)


    def _update_obstacles_here(self, context:Context):
        sleep(0.5)
        position = self._get_pos(context)

        
        context.obstacles = self._obstacleCamera.get_obstacles(context.obstacles, context.currentStep ,position)


    def _fix_the_matrix(self, context:Context):
        m = context.obstacles
        for l in m:
            lastObstacle = 0
            lastEntry = True
            for i, entry in enumerate(l):
                if not entry:
                    if lastEntry:
                        lastObstacle = max(0,i-1)
                else:
                    if i - lastObstacle < 35:
                        for y in range(lastObstacle, i):
                            l[y] = True
    
                lastEntry = entry

            if i+1 - lastObstacle <35:
                for y in range(lastObstacle, i+1):
                            l[y] = True
    

    def _get_pos(self, context:Context):
        return get_position(self._sensorLeft,self._sensorRight,context)
