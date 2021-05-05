
from pathlib import Path
from drive.lift import Lift
from hal.distancesensor import DistanceSensor
from hal.led import Led
from hal.led_driver import LedDriver
from hal.mecanum_driver import MecanumDriver
from hal.motor import Motor
from hal.pwm import Pwm
from hal.lift_driver import LiftDriver
from config.pins import *
import RPi.GPIO as GPIO

from hal.switch import Switch
from sensor import Sensor
from sensordata import SensorData
from sensormonitor import SensorMonitor
GPIO.setmode(GPIO.BCM)

lf = Motor(MOTOR_FRONT_LEFT_PLUS, MOTOR_FRONT_LEFT_MINUS)
lb = Motor(MOTOR_BACK_LEFT_PLUS, MOTOR_BACK_LEFT_MINUS)
rf = Motor(MOTOR_FRONT_RIGHT_PLUS, MOTOR_FRONT_RIGHT_MINUS)
rb = Motor(MOTOR_BACK_RIGHT_PLUS, MOTOR_BACK_RIGHT_MINUS)
pwm = Pwm(PWM_DRIVE, 40)
driver = MecanumDriver(lf, lb, rf, rb, pwm)


liftMotor = Motor(LIFT_PLUS, LIFT_MINUS)
liftPwm = Pwm(PWM_LIFT, 40)
liftDriver = LiftDriver(liftMotor, liftPwm)

switch = Switch(SWITCH_LIFT_UP)

switchFrontLeft = Switch(SWITCH_FRONT_LEFT)
switchFrontRight = Switch(SWITCH_FRONT_RIGHT)
switchLiftUp = Switch(SWITCH_LIFT_UP)
switchLiftDown = Switch(SWITCH_LIFT_DOWN)

sensorFrontLeft = DistanceSensor(SENSOR_TIGGER, SENSOR_FRONT_LEFT)
sensorFrontRight = DistanceSensor(SENSOR_TIGGER, SENSOR_FRONT_RIGHT)
sensorSideLeft = DistanceSensor(SENSOR_TIGGER, SENSOR_SIDE_LEFT)
sensorSideRight = DistanceSensor(SENSOR_TIGGER, SENSOR_SIDE_RIGHT)

ledA = Led(LED_A)
ledB = Led(LED_B)
ledC = Led(LED_C)
ledDriver = LedDriver(ledA, ledB, ledC)

lift = Lift(liftDriver)
sensorData = SensorData(Path(__file__).parent.parent/'sensor')
sensor = Sensor(
    sensorData,
    switchFrontLeft, switchFrontRight, switchLiftUp, switchLiftDown,
    sensorFrontLeft, sensorFrontRight, sensorSideLeft, sensorSideRight,
)
