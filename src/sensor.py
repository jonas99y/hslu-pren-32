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
        data['switchFrontRight'] = float(self._switchFrontRight.getState())
        data['switchFrontLeft'] = float(self._switchFrontLeft.getState())
        data['switchLiftUp'] = float(self._switchLiftUp.getState())
        data['switchLiftDown'] = float(self._switchLiftDown.getState())
        data['sensorFrontLeft'] = float(self._sensorFrontLeft.read(samples=self._samples))
        data['sensorFrontRight'] = float(self._sensorFrontRight.read(samples=self._samples))
        data['sensorSideLeft'] = float(self._sensorSideLeft.read(samples=self._samples))
        data['sensorSideRight'] = float(self._sensorSideRight.read(samples=self._samples))
        return data

    def cycle(self):
        start = time.time()
        data = self.read_sensors()
        self.write_values(data)
        end = time.time()
        print(f'sensor cycle took {end-start}')
