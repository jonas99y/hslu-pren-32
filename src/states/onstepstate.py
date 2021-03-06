
from time import sleep
from states.context import Context
from states.state import State
from drive.movetofrontofstair import MoveToFrontOfStair
from drive.distancedriver import DistanceDriver
from getposition import get_free_sectors, get_position
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder
import sys
class OnStepState(State):
    def __init__(self, nextState: State, moveToFront:MoveToFrontOfStair, distanceDriver:DistanceDriver):
        self._moveToFront = moveToFront
        self._driver = distanceDriver
        self._sensorLeft = distanceDriver._sensorLeft
        self._sensorRight = distanceDriver._sensorRight
        super().__init__(nextState)


    def _start(self, context:Context):
        print("--------------------------------------------------------------------------------------------------------------")
        print("\n\n\n\n")
        print("--------------------------------------------------------------------------------------------------------------")
        print("OnStepState start()")

        currentPosition = get_position(self._sensorLeft,self._sensorRight,context)
        print(f"Current calculated postion: {currentPosition}.")
        print(f"Current step is {context.currentStep}")
        grid = Grid(matrix=context.obstacles, inverse=True)
        start = grid.node(currentPosition, context.currentStep)
        end = grid.node(70, 5)
        finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        print(grid.grid_str(path=path, start=start, end=end))

        for p in path:
            if p[1] == context.currentStep+1:
                targetPosOnNextStep = p[0]
        print(f"Target on next step is: {targetPosOnNextStep}")
        
        sectorsOfNextStep = get_free_sectors(context.get_next_obstacles())
        print(f"Free sectors are: {sectorsOfNextStep}")
        target = None
        for pos, length in sectorsOfNextStep.items():
            if targetPosOnNextStep >= pos and targetPosOnNextStep <= pos + length:
                target = pos + (length/2)
                break
        if not target:    
            raise Exception("mama mia!")
        print(f"Driving to position: {target}")
        self._driver.drive_to_pos(target, context)
        self._driver.drive_to_pos(target, context)
        self._driver.drive_to_pos(target, context)
        self._driver.drive_to_pos(target, context)
        self._driver.drive_to_pos(target, context)
        self._moveToFront.start()
        return
        
    



        
