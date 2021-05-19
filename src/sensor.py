#!/usr/bin/env python3
from pathlib import Path
import time
from typing import Dict, Union
from averagedsensor import AveragedSensor
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
                 sensorFrontLeft: AveragedSensor,
                 sensorFrontRight: AveragedSensor,
                 sensorSideLeft: AveragedSensor,
                 sensorSideRight: AveragedSensor,
                 switchStart: Switch,
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
        self._switchStart = switchStart
        self._samples = samples

    def write_values(self, data):
        self._sensorData.write(data)    

    def read_sensors(self)->Dict[str, float]:
        data: Dict[str, Union[float]] = {}
        data[SensorData.switchFrontRight] = float(self._switchFrontRight.getState())
        data[SensorData.switchFrontLeft] = float(self._switchFrontLeft.getState())
        data[SensorData.switchLiftUp] = float(self._switchLiftUp.getState())
        data[SensorData.switchLiftDown] = float(self._switchLiftDown.getState())
        data[SensorData.sensorFrontLeft] =self._sensorFrontLeft.read()
        data[SensorData.sensorFrontRight] = self._sensorFrontRight.read()
        time.sleep(0.06)
        data[SensorData.sensorSideLeft] = self._sensorSideLeft.read()
        time.sleep(0.06)
        data[SensorData.sensorSideRight] = self._sensorSideRight.read()
        time.sleep(0.06)
        data[SensorData.switchStart] = float(self._switchStart.getState())
        return data

    def cycle(self):
        start = time.time()
        data = self.read_sensors()
        self.write_values(data)
        end = time.time()
        print(f'sensor cycle took {end-start}')
