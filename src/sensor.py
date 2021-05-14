#!/usr/bin/env python3
from pathlib import Path
import time
from typing import Dict, Union
from hal.distancesensor import DistanceSensor
from hal.switch import Switch
from sensordata import SensorData
from Bluetin_Echo import Echo

class Sensor():

    def __init__(self,
                 sensorData: SensorData,
                 switchFrontRight: Switch,
                 switchFrontLeft: Switch,
                 switchLiftUp: Switch,
                 switchLiftDown: Switch,
                 sensorFrontLeft: Echo,
                 sensorFrontRight: Echo,
                 sensorSideLeft: Echo,
                 sensorSideRight: Echo,
                 samples = 1
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
        self._samples = samples

    def write_values(self, data):
        self._sensorData.write(data)    

    def read_sensors(self)->Dict[str, float]:
        data: Dict[str, Union[float]] = {}
        data[SensorData.sensorFrontLeft] =0
        data[SensorData.sensorFrontRight] = 0
        data[SensorData.sensorSideLeft] = 0
        data[SensorData.sensorSideRight] = self._sensorSideRight.read(samples=self._samples)
        return data

    def cycle(self):
        start = time.time()
        data = self.read_sensors()
        self.write_values(data)
        end = time.time()
        print(f'sensor cycle took {end-start}')
