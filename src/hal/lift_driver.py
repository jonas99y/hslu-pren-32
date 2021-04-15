from hal.motor import Motor
from hal.pwm import Pwm

class LiftDirection():
    up = 5
    down = 6



class LiftDriver():
    def __init__(self, motor: Motor, pwm:Pwm):
        self._motor = motor
        self._pwm = pwm

    def drive(self, direction:LiftDirection):
        if direction == LiftDirection.down:
            print("Lift down")
            self._motor.stop()
            self._motor.backwards()
        elif direction == LiftDirection.up:
            print("Lift up")
            self._motor.stop()
            self._motor.forward()

    def stop(self):
        self._motor.stop()
        print(f'Lift stop')


    def changeSpeed(self, speedDelta:int):
        self._pwm.setSpeed(self._pwm.getSpeed()+speedDelta)