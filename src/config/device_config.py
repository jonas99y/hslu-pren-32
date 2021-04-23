
from hal.mecanum_driver import MecanumDriver
from hal.motor import Motor
from hal.pwm import Pwm
from hal.lift_driver import LiftDriver
from config.pins import *
import RPi.GPIO as GPIO

from hal.switch import Switch

GPIO.setmode(GPIO.BCM)

lf = Motor(MOTOR_FRONT_LEFT_PLUS, MOTOR_FRONT_LEFT_MINUS)
lb = Motor(MOTOR_BACK_LEFT_PLUS, MOTOR_BACK_LEFT_MINUS)
rf = Motor(MOTOR_FRONT_RIGHT_PLUS, MOTOR_FRONT_RIGHT_MINUS)
rb = Motor(MOTOR_BACK_RIGHT_PLUS, MOTOR_BACK_RIGHT_MINUS)
pwm = Pwm(PWM_DRIVE, 40)
driver = MecanumDriver(lf,lb,rf,rb,pwm)

liftMotor = Motor(LIFT_PLUS, LIFT_MINUS)
liftPwm = Pwm(PWM_LIFT, 40)
liftDriver = LiftDriver(liftMotor, liftPwm)

switch = Switch(SWITCH_LIFT_UP)
