#!/usr/bin/env python3
from pathlib import Path
import time
from subprocess import Popen
import sensordata
src_dir = Path(__file__).parent

def main():
    Popen(str(src_dir / 'sensor.py'))
    while True:
        cycle()
        time.sleep(0.01)

def cycle():
    data = sensordata.read()
    print(data)


if __name__ == '__main__':
    main()
