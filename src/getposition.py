
from time import sleep
from typing import Dict, List

from states.context import Context
from Bluetin_Echo.Bluetin_Echo import Echo
def get_position(sensorLeft:Echo, sensorRitgh:Echo, context:Context):
    print("start get_pos")
    stairWidth = 136
    cameraOffset = 11.5
    errorMargin = 10

    sectors = get_free_sectors(context.get_current_obstacles())
    measuredDistanceLeft, measuredDistanceRight = measure_distances(sensorLeft, sensorRitgh)
    possibleSectors = [] # start postions of sectors
    for position, length in sectors.items():
        if abs(measuredDistanceLeft + measuredDistanceRight + 2*cameraOffset - length) < errorMargin:
            possibleSectors.append((position, length))

    foundSector = None
    if len(possibleSectors) == 1:
        foundSector = possibleSectors[0] 
    else:
        for s in possibleSectors:
            if s[0] <= context.lastKnowPosition and s[0]+s[1] >= context.lastKnowPosition:
                foundSector = s

    if foundSector:            
        return round(foundSector[0] + measuredDistanceLeft + cameraOffset)

    print("WARNING: We did not find any matching sectors!!")
            
    if measuredDistanceLeft > measuredDistanceRight:
        if measuredDistanceRight != 0:
            return round(max(stairWidth - measuredDistanceRight - cameraOffset, cameraOffset))
    elif measuredDistanceLeft != 0:
        return round(min(measuredDistanceLeft + cameraOffset, stairWidth - cameraOffset))

    return 0

def measure_distances(sensorLeft:Echo, sensorRitgh:Echo):
    for i in range(0,5):
        l = sensorLeft.read()
        print(f"l: {l}")
        sleep(0.1 + i*0.1)
        if l > 0 and l < 150:
            break

    for i in range(0,5):
        r = sensorRitgh.read()
        print(f"r: {r}")
        sleep(0.1 + i*0.1)
        if r > 0 and r < 150:
            break

    sleep(0.1)
    return l, r

def get_free_sectors(obstaclesOfCurrentStep:List)-> Dict[int,int]:
    matrixSize = len(obstaclesOfCurrentStep)
    possibleDistanceAndPositions = []
    entries= {}
    free = True
    lastFreePosition = 0
    for i in range(1, matrixSize - 1):
        if(obstaclesOfCurrentStep[i]):
            if(free):
                length = i - 1 - lastFreePosition
                if length > 30:
                    entries[lastFreePosition] = length
                free = False
        elif(not free):
            lastFreePosition = i
            free = True
    if(free):
        length = matrixSize - 2 -lastFreePosition
        if length > 30:
            entries[lastFreePosition] = length
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
    
    # print(get_position(measuredDistanceLeft=10, measuredDistanceRight=37, obstaclesOfCurrentStep=matrix))
    print("not woking atm")

if __name__ == '__main__':
    main()