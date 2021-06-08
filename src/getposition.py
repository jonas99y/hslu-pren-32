
from typing import List


def get_position(measuredDistanceLeft:float, measuredDistanceRight:float, obstaclesOfCurrentStep:List[bool]):
    stairWidth = 136
    cameraOffset = 11
    possiblePositionFromLeftSensor = 0
    possiblePositionFromRightSensor = 0
    possiblePositionAverage = 0
    if(measuredDistanceLeft < 40 and measuredDistanceLeft > 0):
        possiblePositionFromLeftSensor = min(measuredDistanceLeft + cameraOffset, stairWidth - cameraOffset)

    if(measuredDistanceRight < 40 and measuredDistanceRight > 0):
        possiblePositionFromRightSensor = max(stairWidth - measuredDistanceRight - cameraOffset, cameraOffset)

    if(possiblePositionFromLeftSensor > 0):
        if(possiblePositionFromRightSensor > 0):
            possiblePositionAverage = (possiblePositionFromLeftSensor + possiblePositionFromRightSensor) / 2
        else:
            possiblePositionAverage = possiblePositionFromLeftSensor
    elif(possiblePositionFromRightSensor > 0):
        possiblePositionAverage = possiblePositionFromRightSensor

    return possiblePositionAverage