
from typing import List
import tensorflow as tf
import numpy as np
import cv2
import time
from threading import Thread
from pathlib import Path
from picamera.array import PiRGBArray
from picamera import PiCamera
src_dir = Path(__file__).parent


class ObstacleCamera:
    cm_per_pixel_1st_step = 0.048
    cm_per_pixel_2nd_step = 0.052
    cm_per_pixel_3rd_step = 0.078
    cm_per_pixel_4th_step = 0.136

    x_offset_1st_step = 5
    x_offset_2nd_step = 8
    x_offset_3rd_step = 12
    x_offset_4th_step = 15

    def __init__(self):
        labelPath = str(Path.joinpath(src_dir, "obstacle_detection_labels.txt"))
        modelPath = str(Path.joinpath(src_dir, "pren2_team32_obstacles_model.tflite"))
        
        with open(labelPath, 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]

        self.interpreter = tf.lite.Interpreter(model_path=modelPath)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]

        self.min_conf_threshold = 0.5

    def get_obstacles(self, currentMatrix: List[List[bool]], step:int, position:int)-> List[List[bool]]:
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        rawCapture = PiRGBArray(camera)

        # allow the camera to warmup
        time.sleep(1.5)

        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        image = cv2.rotate(image, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

        imH, imW, _ = image.shape
        image_resized = cv2.resize(image, (self.width, self.height))
        input_data = np.expand_dims(image_resized, axis=0)

        self.interpreter.set_tensor(self.input_details[0]['index'],input_data)
        self.interpreter.invoke()

        # Retrieve detection results
        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])[0] # Bounding box coordinates of detected objects
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])[0] # Class index of detected objects
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])[0] # Confidence of detected objects

        for i in range(len(scores)):
            if ((scores[i] > self.min_conf_threshold) and (scores[i] <= 1.0)):

                # Get bounding box coordinates and draw box
                # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
                ymin = int(max(1,(boxes[i][0] * imH)))
                xmin = int(max(1,(boxes[i][1] * imW)))
                ymax = int(min(imH,(boxes[i][2] * imH)))
                xmax = int(min(imW,(boxes[i][3] * imW)))
                
                # map positions to matrix
                # check 1st step
                if(ymax > 660):
                    xmin_cm = int(xmin * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=5-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)
                # check 2nd step
                elif(ymin < 575 and ymax > 330):
                    xmin_cm = int(xmin * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=4-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)
                # check 3rd step
                elif(ymin < 265 and ymax > 185):
                    xmin_cm = int(xmin * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=3-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)
                # check 4th step
                elif(ymin < 125 ):
                    xmin_cm = int(xmin * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_1st_step) - self.x_offset_1st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=2-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)

        return currentMatrix

    def __update_matrix(self, currentMatrix: List[List[bool]], y_offset:int, xmin_cm:int, xmax_cm:int)->List[List[bool]]:
        y = min(len(currentMatrix) - y_offset, len(currentMatrix) - 1)
        xmin = max(xmin_cm, 0)
        xmax = min(xmax_cm, len(currentMatrix[0]) - 1)

        for x in range(xmin, xmax + 1):
            currentMatrix[y][x] = True

        return currentMatrix