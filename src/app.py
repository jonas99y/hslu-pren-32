#!/usr/bin/env python3
from pathlib import Path
import time
from subprocess import Popen
from sensordata import SensorData
from sensormonitor import SensorMonitor
from config.device_config import lift, sensorMonitor
src_dir = Path(__file__).parent
import RPi.GPIO as GPIO

def main():
    try:
        p= Popen(str(src_dir / 'sensor.py'))
               
        lift.climb()
        while True:
            sensorMonitor.cycle()
    finally:
        p.kill()
        GPIO.cleanup()




if __name__ == '__main__':
    main()
