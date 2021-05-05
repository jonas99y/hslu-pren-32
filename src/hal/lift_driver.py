from typing import Union
from hal.motor import Motor
from hal.pwm import Pwm

class LiftDirection():
    up = 5
    down = 6



class LiftDriver():
    def __init__(self, motor: Motor, pwm:Pwm):
        self._motor = motor
        self._pwm = pwm
        self._currentDirection:Union[int, None] = None

    def drive(self, direction:int):
        if self._currentDirection == direction:
            # drives already in the correct direction
            pass
        else:
            if direction == LiftDirection.down:
                print("Lift down")
                self._motor.stop()
                self._motor.backwards()
            elif direction == LiftDirection.up:
                print("Lift up")
                self._motor.stop()
                self._motor.forward()
            self._currentDirection = direction

    def stop(self):
        self._currentDirection = None
        self._motor.stop()
        print(f'Lift stop')


    def changeSpeed(self, speedDelta:int):
        self._pwm.setSpeed(self._pwm.getSpeed()+speedDelta)