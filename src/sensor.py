#!/usr/bin/env python3
from pathlib import Path
import time
import sensordata 
demofile = Path(__file__).parent / 'demofile.txt'


class Sensor():
    def __init__(self) -> None:
        self.count = 0

    def cycle(self):
        sensordata.write(sensordata.SensorData(self.count))
        self.count += 1


def main():
    sensor = Sensor()
    while True:
        sensor.cycle()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
