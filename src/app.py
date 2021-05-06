#!/usr/bin/env python3
import RPi.GPIO as GPIO
from pathlib import Path
import time
from subprocess import Popen
from config.device_config import lift, sensor, driver, liftDriver
from drive.climb import Climb
from sensor import Sensor
from sensordata import SensorData
src_dir = Path(__file__).parent
from threading import Thread, Lock
CYCLE_LENGTH = 0.1
WARN_IF_CYCLE_LONGER = 0.05

def main():
    try:
        # p = Popen(str(src_dir / 'sensor.py'))
        # sensorData = SensorData(src_dir / 'sensor')

        watchdogThread = Thread(target = watchdog)
        watchdogThread.start()
        lock = Lock()
        climb = Climb(lift)
        climb.start()
        cycleables = [climb]
        while True:
            start = time.time()
            
            sensorstate = sensor.read_sensors()
            for c in cycleables:
                c.cycle(sensorstate)
            end = time.time()
            sensor.write_values(sensorstate) # write to sensor file for debug purposes
            actualCycleLenght = (end - start)
            if actualCycleLenght > WARN_IF_CYCLE_LONGER:
                print(f'Cycle took {actualCycleLenght}')
            with lock:
                global lastSignOfLifeAt
                lastSignOfLifeAt = time.time()
            time.sleep(CYCLE_LENGTH -actualCycleLenght)

            
    finally:
        p.kill()
        GPIO.cleanup()

WATCHDOG_TIMEOUT = 0.1
MAX_TIME_WITH_NO_SIGN_OF_LIFE  = 0.5
def watchdog():
    while True:
        with lock:
            global lastSignOfLifeAt
            if time.time() - lastSignOfLifeAt > MAX_TIME_WITH_NO_SIGN_OF_LIFE:
                emergency_stop()
        time.sleep(WATCHDOG_TIMEOUT)

def emergency_stop():
    print("emergency stop!")
    driver.stop()
    liftDriver.stop()


if __name__ == '__main__':
    main()
