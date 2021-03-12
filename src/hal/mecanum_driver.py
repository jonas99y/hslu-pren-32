

from hal.motor import Motor
from hal.pwm import Pwm


class MecanumDriver():
    def __init__(self, lf:Motor, lb: Motor, rf:Motor, rb:Motor, pwm:Pwm):
        self._lf = lf
        self._lb = lb
        self._rf = rf
        self._rb = rb
        self._pwm = pwm
    
    def drive(self):
        self._lf.forward()
        self._lb.forward()
        self._rf.forward()
        self._rb.forward()

    def stop(self):
        self._lf.stop()
        self._lb.stop()
        self._rf.stop()
        self._rb.stop()


    def increaseSpeed(self):
        self._pwm.setSpeed(self._pwm.getSpeed()+10)

    def decreaseSpeed(self):
        self._pwm.setSpeed(self._pwm.getSpeed()-10)