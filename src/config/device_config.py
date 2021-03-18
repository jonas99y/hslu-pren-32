
from hal.mecanum_driver import MecanumDriver
from hal.motor import Motor
from hal.pwm import Pwm
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

switch = Switch(SWITCH_LIFT)
