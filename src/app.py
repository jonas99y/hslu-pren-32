#!/usr/bin/env python3
import RPi.GPIO as GPIO
from pathlib import Path
import time
from subprocess import Popen
from config.device_config import lift, sensor, driver, liftDriver
from drive.climb import Climb
from drive.distancedriver import DistanceDriver
from navigate import Navigate
from sensor import Sensor
from sensordata import SensorData
src_dir = Path(__file__).parent
from threading import Thread, Lock
CYCLE_LENGTH = 0.01
WARN_IF_CYCLE_LONGER = 0.05
DEBUG = True
def main():
    try:
        global lastSignOfLifeAt
        lock = Lock()
        lastSignOfLifeAt = time.time()
        watchdogThread = Thread(target = watchdog, args=(lock,))
        if not DEBUG:
            watchdogThread.start()
        navigate = Navigate()
        cycleables = [navigate]
        for i in range(0,10):
            sensor.read_sensors() # makes sure sensors have valid values for avging
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
                
                lastSignOfLifeAt = time.time()
            sleepTime = CYCLE_LENGTH -actualCycleLenght
            if sleepTime< 0:
                sleepTime = 0
            time.sleep(sleepTime)

            
    finally:
        stop_all()
        GPIO.cleanup()


WATCHDOG_TIMEOUT = 0.1
MAX_TIME_WITH_NO_SIGN_OF_LIFE  = 0.5
def watchdog(lock):
    while True:
        with lock:
            global lastSignOfLifeAt
            if time.time() - lastSignOfLifeAt > MAX_TIME_WITH_NO_SIGN_OF_LIFE:
                emergency_stop()
        time.sleep(WATCHDOG_TIMEOUT)

# def read_sensors():
#     while True:
#         start = time.time()
#         data =  sensor.read_sensors()
#         print(f'sensorcycle: {time.time()-start}')

def emergency_stop():
    print("emergency stop!")
    stop_all()

def stop_all():
    driver.stop()
    liftDriver.stop()


if __name__ == '__main__':
    main()
