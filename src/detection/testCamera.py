# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import datetime
import tensorflow as tf
import numpy as np


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
image = cv2.rotate(image, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
image = image[1000:, :]
# display the image on screen and wait for a keypress
#cv2.imshow("Image", image)
#cv2.waitKey(0)

# save image with timestamp in filename
timestamp = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
name = f"img/picamera_{timestamp}.png"
cv2.imwrite(name,image)