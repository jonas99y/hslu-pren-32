import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

Forward=26
Backward=20
PWM=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(PWM, GPIO.OUT)

pwm0 = GPIO.PWM(PWM,100)

def forward(duration:int):
    GPIO.output(Forward,GPIO.HIGH)
    print("Moving Forward")
    time.sleep(duration)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward,GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

pwm0.start(100)
forward(5)
reverse(5)
pwm0.ChangeDutyCycle(10)
print("dc 10")
forward(3)
pwm0.ChangeDutyCycle(20)
print("dc 20")
forward(3)
pwm0.ChangeDutyCycle(30)
print("dc 30")
forward(3)
pwm0.ChangeDutyCycle(40)
print("dc 40")
forward(3)
pwm0.ChangeDutyCycle(50)
print("dc 50")
forward(3)
pwm0.ChangeDutyCycle(60)
print("dc 60")
forward(3)
pwm0.ChangeDutyCycle(70)
print("dc 70")
forward(3)
pwm0.ChangeDutyCycle(80)
print("dc 80")
forward(3)
pwm0.ChangeDutyCycle(90)
print("dc 90")
forward(3)
pwm0.ChangeDutyCycle(100)
print("dc 100")
forward(3)
pwm0.stop()
print("PWM stop")
forward(5)
reverse(5)
GPIO.cleanup()