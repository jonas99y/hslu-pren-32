import tensorflow as tf
import numpy as np
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from hal.led_driver import Piktogram

class IconClassifier:
    def __init__(self, resolutionWidth=720, resolutionHeight=1280):
        self._resolutionWidth = resolutionWidth
        self._resolutionHeight = resolutionHeight

    def detectIcon(self, modelPath, labelPath, cropHeight = 0):
        # Load labels
        labels = open(labelPath, "r").read().splitlines()

        # Load TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path=modelPath)
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        height = input_details[0]['shape'][1]
        width = input_details[0]['shape'][2]

        # Initialize video stream
        camera = PiCamera()
        rawCapture = PiRGBArray(camera)
        # allow the camera to warmup
        time.sleep(0.1)
        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        # Grab frame from video stream and crop it
        frame = image[cropHeight:self._resolutionHeight, 0:self._resolutionWidth]

        # Resize to expected shape [1xHxWx3]
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (width, height))
        input_data = np.expand_dims(frame_resized, axis=0)

        # Perform the actual detection by running the model with the image as input
        interpreter.set_tensor(input_details[0]['index'],input_data)
        interpreter.invoke()

        # output_details[0]['index'] = the index which provides the input
        output_data = np.array(interpreter.get_tensor(output_details[0]['index']))[0]
        score = 0
        labelIndex = 0
        for i in range(5):
            if(output_data[i] > score):
                score = output_data[i]
                labelIndex = i
        icon = labels[labelIndex]

        pictogram = Piktogram.none
        if(icon == "pen"):
            pictogram = Piktogram.pencile
        elif(icon == "ruler"):
            pictogram = Piktogram.ruler
        elif(icon == "hammer"):
            pictogram = Piktogram.hammer
        elif(icon == "bucket"):
            pictogram = Piktogram.bucket
        elif(icon == "taco"):
            pictogram = Piktogram.taco
        
        return pictogram

def main():
    imW = 1280
    imH = 720
    cropHeight = 240
    labelPath = "pren2_team32_icons_model_dict.txt"
    modelPath = "pren2_team32_icons_model.tflite"

    classifier = IconClassifier(resolutionWidth=imW, resolutionHeight=imH)
    detectedIcon = classifier.detectIcon(modelPath=modelPath, labelPath=labelPath, cropHeight=cropHeight)
    print(detectedIcon)

if __name__ == '__main__':
    main()