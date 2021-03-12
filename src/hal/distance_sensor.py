import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BOARD)

TRIGGER = 10
ECHO = 12

print("Distance Measurement In Progress")
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
time.sleep(0.5)
GPIO.output(TRIGGER, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

while True:
   print("Place the object......")
   GPIO.output(TRIGGER, True)
   time.sleep(0.00001)
   GPIO.output(TRIGGER, False)

   while GPIO.input(ECHO)==0:
      pulse_start = time.time()

   while GPIO.input(ECHO)==1:
      pulse_end = time.time()

   distance = (pulse_end - pulse_start)* 17150
   distance = round(distance+1.15, 3)
  
   print("Distanz: " + str(distance))
   time.sleep(2)
GPIO.cleanup()
