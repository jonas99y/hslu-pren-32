
import datetime
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
    cm_per_pixel_1st_step = 0.053
    cm_per_pixel_2nd_step = 0.06
    cm_per_pixel_3rd_step = 0.105
    cm_per_pixel_4th_step = 0.136

    x_offset_1st_step = 19
    x_offset_2nd_step = 24
    x_offset_3rd_step = 38
    x_offset_4th_step = 49

    def __init__(self, camera:PiCamera):
        labelPath = str(Path.joinpath(src_dir, "obstacle_detection_labels.txt"))
        modelPath = str(Path.joinpath(src_dir, "pren2_team32_obstacles_model_2.tflite"))
        
        with open(labelPath, 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]

        self.interpreter = tf.lite.Interpreter(model_path=modelPath)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]

        self.min_conf_threshold = 0.5
        self.camera = camera

    def get_obstacles(self, currentMatrix: List[List[bool]], step:int, position:int)-> List[List[bool]]:
        rawCapture = PiRGBArray(self.camera)
        # grab an image from the camera
        self.camera.capture(rawCapture, format="bgr")
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
                    xmin_cm = int(xmin * self.cm_per_pixel_2st_step) - self.x_offset_2st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_2st_step) - self.x_offset_2st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=4-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)
                # check 3rd step
                elif(ymin < 265 and ymax > 185):
                    xmin_cm = int(xmin * self.cm_per_pixel_3st_step) - self.x_offset_3st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_3st_step) - self.x_offset_3st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=3-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)
                # check 4th step
                elif(ymin < 125 ):
                    xmin_cm = int(xmin * self.cm_per_pixel_4st_step) - self.x_offset_4st_step + position
                    xmax_cm = int(xmax * self.cm_per_pixel_4st_step) - self.x_offset_4st_step + position
                    currentMatrix = self.__update_matrix(currentMatrix=currentMatrix, y_offset=2-step, xmin_cm=xmin_cm, xmax_cm=xmax_cm)

        self._draw(scores, boxes, imW, imH, self.labels, classes, image, 0.2 )



        return currentMatrix

    def __update_matrix(self, currentMatrix: List[List[bool]], y_offset:int, xmin_cm:int, xmax_cm:int)->List[List[bool]]:
        y = min(len(currentMatrix) - y_offset, len(currentMatrix) - 1)
        xmin = max(xmin_cm, 0)
        xmax = min(xmax_cm, len(currentMatrix[0]) - 1)

        for x in range(xmin, xmax + 1):
            currentMatrix[y][x] = True

        return currentMatrix


    def _draw(self, scores, boxes, imW, imH, labels, classes, image, min_conf_threshold):
        for i in range(len(scores)):
            if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):

                # Get bounding box coordinates and draw box
                # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
                ymin = int(max(1,(boxes[i][0] * imH)))
                xmin = int(max(1,(boxes[i][1] * imW)))
                ymax = int(min(imH,(boxes[i][2] * imH)))
                xmax = int(min(imW,(boxes[i][3] * imW)))

                cv2.rectangle(image, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)

                # Draw label
                object_name = labels[int(classes[i])] # Look up object name from "labels" array using class index
                label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
                label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
                cv2.rectangle(image, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
                cv2.putText(image, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text

        # All the results have been drawn on the image, now display the image
        # cv2.imshow('Object detector', image)

        timestamp = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
        Path('img/obstacles').mkdir(parents=True, exist_ok=True)
        name = f"img/obstacles/picamera_{timestamp}_.png"
        cv2.imwrite(name,image)