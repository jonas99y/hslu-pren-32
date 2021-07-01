import tensorflow as tf
import numpy as np
import cv2
import time
import datetime
from threading import Thread
from pathlib import Path
from picamera.array import PiRGBArray
from picamera import PiCamera

# position: 0 = left, 1 = middle left, 2 = middle right, 3 = right
def detectObstacles(matrix, position):
    positionOffset = 0
    if(position == 1):
        positionOffset = 2
    elif(position == 2):
        positionOffset = 5
    elif(position == 3):
        positionOffset = 7

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    # allow the camera to warmup
    time.sleep(0.1)
    # grab an image from the camera
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    #image = cv2.imread("detection/img/picamera_05-14-2021_09.49.44.png")

    # save image with timestamp in filename
    #timestamp = datetime.datetime.now().strftime('%m-%d-%Y_%H.%M.%S')
    #name = f"img/picamera_{timestamp}.png"
    #cv2.imwrite(name,image)

    min_conf_threshold = 0.5

    PATH_TO_LABELS = "detection/obstacle_detection_labels.txt"
    PATH_TO_MODEL = "detection/pren2_team32_obstacles_model_2.tflite"

    with open(PATH_TO_LABELS, 'r') as f:
        labels = [line.strip() for line in f.readlines()]

    interpreter = tf.lite.Interpreter(model_path=PATH_TO_MODEL)

    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    image = cv2.rotate(image, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

    imH, imW, _ = image.shape
    image_resized = cv2.resize(image, (width, height))
    input_data = np.expand_dims(image_resized, axis=0)

    interpreter.set_tensor(input_details[0]['index'],input_data)
    interpreter.invoke()

    # Retrieve detection results
    boxes = interpreter.get_tensor(output_details[0]['index'])[0] # Bounding box coordinates of detected objects
    classes = interpreter.get_tensor(output_details[1]['index'])[0] # Class index of detected objects
    scores = interpreter.get_tensor(output_details[2]['index'])[0] # Confidence of detected objects

    for i in range(len(scores)):
        if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):

            # Get bounding box coordinates and draw box
            # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
            ymin = float(max(0,(boxes[i][0])))
            xmin = float(max(0,(boxes[i][1])))
            ymax = float(min(1,(boxes[i][2])))
            xmax = float(min(1,(boxes[i][3])))
            # check 2nd step
            if (ymin > 0.53):
                if(xmin < 0.33):
                    matrix[3][0 + positionOffset] = 0
                    if(xmax > 0.33):
                        matrix[3][1 + positionOffset] = 0
                elif(xmin < 0.66):
                    matrix[3][1 + positionOffset] = 0
                if(xmax > 0.66):
                    matrix[3][2 + positionOffset] = 0

            # check 3rd step
            elif (ymax > 0.28 and ymax < 0.47):
                if(xmin < 0.33):
                    matrix[2][0 + positionOffset] = 0
                    if(xmax > 0.33):
                        matrix[2][1 + positionOffset] = 0
                elif(xmin < 0.66):
                    matrix[2][1 + positionOffset] = 0
                if(xmax > 0.66):
                    matrix[2][2 + positionOffset] = 0
            # check 4th step
            elif (ymax > 0.10 and ymax < 0.28):
                if(xmin < 0.33):
                    matrix[1][0 + positionOffset] = 0
                    if(xmax > 0.33):
                        matrix[1][1 + positionOffset] = 0
                elif(xmin < 0.66):
                    matrix[1][1 + positionOffset] = 0
                if(xmax > 0.66):
                    matrix[1][2 + positionOffset] = 0
            # check 5th step
            elif (ymin < 0.15):
                if(xmin < 0.33):
                    matrix[0][0 + positionOffset] = 0
                    if(xmax > 0.33):
                        matrix[0][1 + positionOffset] = 0
                elif(xmin < 0.66):
                    matrix[0][1 + positionOffset] = 0
                if(xmax > 0.66):
                    matrix[0][2 + positionOffset] = 0

def main():  
    matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    detectObstacles(matrix=matrix, position=0)



if __name__ == '__main__':
    main()