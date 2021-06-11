#!/usr/bin/env python3
import RPi.GPIO as GPIO
from pathlib import Path
import time
from config.device_config import driver, liftDriver
from statemachine import StateMachine
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

        StateMachine().start()
            
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
        
def emergency_stop():
    print("emergency stop!")
    stop_all()

def stop_all():
    driver.stop()
    liftDriver.stop()


if __name__ == '__main__':
    main()
