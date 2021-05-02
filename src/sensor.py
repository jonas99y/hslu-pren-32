#!/usr/bin/env python3
from pathlib import Path
import time
from typing import Dict, Union
from hal.distancesensor import DistanceSensor
from hal.switch import Switch
from sensordata import SensorData
from config.device_config import switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown, sensorFrontLeft, sensorFrontRight, sensorSideLeft, sensorSideRight


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

    def cycle(self):
        start = time.time()
        data: Dict[str, Union[bool, float]] = {}
        data['switchFrontRight'] = self._switchFrontRight.getState()
        data['switchFrontLeft'] = self._switchFrontLeft.getState()
        data['switchLiftUp'] = self._switchLiftUp.getState()
        data['switchLiftDown'] = self._switchLiftDown.getState()
        data['sensorFrontLeft'] = self._sensorFrontLeft.measure()
        data['sensorFrontRight'] = self._sensorFrontRight.measure()
        data['sensorSideLeft'] = self._sensorSideLeft.measure()
        data['sensorSideRight'] = self._sensorSideRight.measure()
        self._sensorData.write(data)
        end = time.time()
        print(end-start)


def main():
    sensor = Sensor(
        SensorData(Path(__file__).parent/'sensor'),
        switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown,
        sensorFrontLeft, sensorFrontRight, sensorSideLeft, sensorSideRight,

    )
    while True:
        sensor.cycle()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
