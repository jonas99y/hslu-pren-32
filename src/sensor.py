#!/usr/bin/env python3
from pathlib import Path
import time
from typing import Dict, Union
from hal.distancesensor import DistanceSensor
from hal.switch import Switch
from sensordata import SensorData


class Sensor():

    def __init__(self,
                 sensorData: SensorData,
                 switchFrontRight: Switch,
                 switchFrontLeft: Switch,
                 switchLiftUp: Switch,
                 switchLiftDown: Switch,
                 sensorFrontLeft: DistanceSensor,
                 sensorFrontRight: DistanceSensor,
                 sensorSideLeft: DistanceSensor,
                 sensorSideRight: DistanceSensor,
                 ):
        self._sensorData = sensorData
        self._switchFrontRight = switchFrontRight
        self._switchFrontLeft = switchFrontLeft
        self._switchLiftUp = switchLiftUp
        self._switchLiftDown = switchLiftDown
        self._sensorFrontLeft = sensorFrontLeft
        self._sensorFrontRight = sensorFrontRight
        self._sensorSideLeft = sensorSideLeft
        self._sensorSideRight = sensorSideRight

    def write_values(self, data):
        self._sensorData.write(data)    

    def read_sensors(self)->Dict[str, float]:
        data: Dict[str, Union[float]] = {}
        data['switchFrontRight'] = float(self._switchFrontRight.getState())
        data['switchFrontLeft'] = float(self._switchFrontLeft.getState())
        data['switchLiftUp'] = float(self._switchLiftUp.getState())
        data['switchLiftDown'] = float(self._switchLiftDown.getState())
        data['sensorFrontLeft'] = self._sensorFrontLeft.measure()
        data['sensorFrontRight'] = self._sensorFrontRight.measure()
        data['sensorSideLeft'] = self._sensorSideLeft.measure()
        data['sensorSideRight'] = self._sensorSideRight.measure()
        return data

    def cycle(self):
        start = time.time()
        data = self.read_sensors()
        self.write_values(data)
        end = time.time()
        print(f'sensor cycle took {end-start}')


# def main():
#     sensor = Sensor(
#         SensorData(Path(__file__).parent/'sensor'),
#         switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown,
#         sensorFrontLeft, sensorFrontRight, sensorSideLeft, sensorSideRight,

#     )
#     while True:
#         sensor.cycle()
#         time.sleep(0.5)


if __name__ == '__main__':
    main()
