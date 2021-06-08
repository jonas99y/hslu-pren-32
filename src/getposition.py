
from typing import Dict, List

def get_position(measuredDistanceLeft:float, measuredDistanceRight:float, obstaclesOfCurrentStep:List[bool]):
    stairWidth = 136
    cameraOffset = 11.5
    errorMargin = 10

    sectors = get_free_sectors(obstaclesOfCurrentStep)

    for position, length in sectors.items():
        if abs(measuredDistanceLeft + measuredDistanceRight + 2*cameraOffset - length) < errorMargin:
            return round(position + measuredDistanceLeft + cameraOffset)

    if measuredDistanceLeft > measuredDistanceRight:
        if measuredDistanceRight != 0:
            return round(max(stairWidth - measuredDistanceRight - cameraOffset, cameraOffset))
    elif measuredDistanceLeft != 0:
        return round(min(measuredDistanceLeft + cameraOffset, stairWidth - cameraOffset))

    return 0

def get_free_sectors(obstaclesOfCurrentStep:List)-> Dict[int,int]:
    matrixSize = len(obstaclesOfCurrentStep)
    possibleDistanceAndPositions = []
    entries= {}
    free = True
    lastFreePosition = 0
    for i in range(1, matrixSize - 1):
        if(obstaclesOfCurrentStep[i]):
            if(free):
                entries[lastFreePosition] = i - 1 - lastFreePosition
                free = False
        elif(not free):
            lastFreePosition = i
            free = True
    if(free):
        entries[lastFreePosition] = matrixSize - 2 -lastFreePosition
    return entries

def main():  
    stairWidth = 136
    matrix = []
    for i in range(1, stairWidth):
        matrix.append(False)

    # place obstacles
    for i in range (20, 45):
        matrix[i] = True

    for i in range (110, 135):
        matrix[i] = True
    
    print(get_position(measuredDistanceLeft=10, measuredDistanceRight=37, obstaclesOfCurrentStep=matrix))

if __name__ == '__main__':
    main()