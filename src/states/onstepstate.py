
from time import sleep
from states.context import Context
from states.state import State
from drive.movetofrontofstair import MoveToFrontOfStair
from drive.distancedriver import DistanceDriver
from getposition import get_position
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class OnStepState(State):
    def __init__(self, nextState: State, moveToFront:MoveToFrontOfStair, distanceDriver:DistanceDriver):
        self._moveToFront = moveToFront
        self._driver = distanceDriver
        self._sensorLeft = distanceDriver._sensorLeft
        self._sensorRight = distanceDriver._sensorRight
        super().__init__(nextState)


    def _start(self, context:Context):
        l = self._sensorLeft.read()
        sleep(0.1)
        r = self._sensorRight.read()
        currentPosition = get_position(l, r, context.get_current_obstacles())

        grid = Grid(matrix=context.obstacles)
        start = grid.node(context.currentStep, currentPosition)
        end = grid.node(5, 70)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        print('operations:', runs, 'path length:', len(path))
        print(grid.grid_str(path=path, start=start, end=end))

        
        # self._moveToFront.start()

        
