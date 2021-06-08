
from typing import List


def get_position(measuredDistanceLeft:float, measuredDistanceRight:float, obstaclesOfCurrentStep:List[bool]):
    stairWidth = 136
    cameraOffset = 11
    possiblePositionFromLeftSensor = 0
    possiblePositionFromRightSensor = 0
    possiblePositionAverage = 0
    if measuredDistanceLeft > measuredDistanceRight:
        if measuredDistanceRight != 0:
            return round(max(stairWidth - measuredDistanceRight - cameraOffset, cameraOffset))
    elif measuredDistanceLeft != 0:
        return round(min(measuredDistanceLeft + cameraOffset, stairWidth - cameraOffset))

    return 0
    if(possiblePositionFromLeftSensor > 0):
        if(possiblePositionFromRightSensor > 0):
            possiblePositionAverage = (possiblePositionFromLeftSensor + possiblePositionFromRightSensor) / 2
        else:
            possiblePositionAverage = possiblePositionFromLeftSensor
    elif(possiblePositionFromRightSensor > 0):
        possiblePositionAverage = possiblePositionFromRightSensor

    return possiblePositionAverage