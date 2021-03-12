

from hal.motor import Motor
from hal.pwm import Pwm

class Direction():
    stop = 0
    forward = 1
    right = 2
    backward = 3
    left = 4

class MecanumDriver():
    def __init__(self, lf:Motor, lb: Motor, rf:Motor, rb:Motor, pwm:Pwm):
        self._lf = lf
        self._lb = lb
        self._rf = rf
        self._rb = rb
        self._pwm = pwm
    
    def drive(self, direction:Direction):
        if direction == Direction.forward:
            self._lf.forward()
            self._lb.forward()
            self._rf.forward()
            self._rb.forward()
            print("Driving forward")
        elif direction == Direction.backward:
            self._lf.backwards()
            self._lb.backwards()
            self._rf.backwards()
            self._rb.backwards()
        elif direction == Direction.right:
            self._lf.forward()
            self._lb.backwards()
            self._rf.backwards()
            self._rb.forward()
        elif direction == Direction.left:
            self._lf.backwards()
            self._lb.forward()
            self._rf.forward()
            self._rb.backwards()
            print("Driving Left")

    def stop(self):
        self._lf.stop()
        self._lb.stop()
        self._rf.stop()
        self._rb.stop()


    def increaseSpeed(self):
        self._pwm.setSpeed(self._pwm.getSpeed()+10)

    def decreaseSpeed(self):
        self._pwm.setSpeed(self._pwm.getSpeed()-10)