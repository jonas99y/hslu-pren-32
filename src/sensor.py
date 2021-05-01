#!/usr/bin/env python3
from pathlib import Path
import time
from sensordata import SensorData
from config.device_config import switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown


class Sensor():
    def __init__(self, sensorData: SensorData):
        self._sensorData = sensorData

    def cycle(self):
        data = {}
        data['switchFrontRight'] = switchFrontRight.getState()
        data['switchFrontLeft'] = switchFrontLeft.getState()
        data['switchLiftUp'] = switchLiftUp.getState()
        data['switchLiftDown'] = switchLiftDown.getState()
        self._sensorData.write(data)


def main():
    sensor = Sensor(SensorData(Path(__file__).parent/'sensor'))
    while True:
        sensor.cycle()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
