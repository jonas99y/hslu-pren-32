from pathlib import Path
import tensorflow as tf
import numpy as np
import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from hal.led_driver import Piktogram
src_dir = Path(__file__).parent

class PictogramCamera:

    def __init__(self):
        labelPath = str(Path.joinpath(src_dir, "pren2_team32_icons_model_dict.txt"))
        modelPath = str(Path.joinpath(src_dir, "pren2_team32_icons_model.tflite"))

        # Load labels
        self.labels = open(labelPath, "r").read().splitlines()

        # Load TFLite model and allocate tensors.
        self.interpreter = tf.lite.Interpreter(model_path=modelPath)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]        

    def detect_pictogram(self)-> Piktogram:
        cropHeight = 240

        # Initialize video stream
        camera = PiCamera()
        rawCapture = PiRGBArray(camera)

        # allow the camera to warmup
        time.sleep(1.5)

        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        # Grab frame from video stream and crop it
        frame = image[cropHeight:self._resolutionHeight, 0:self._resolutionWidth]

        # Resize to expected shape [1xHxWx3]
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (self.width, self.height))
        input_data = np.expand_dims(frame_resized, axis=0)

        # Perform the actual detection by running the model with the image as input
        self.interpreter.set_tensor(self.input_details[0]['index'],input_data)
        self.interpreter.invoke()

        # output_details[0]['index'] = the index which provides the input
        output_data = np.array(self.interpreter.get_tensor(self.output_details[0]['index']))[0]
        score = 0
        labelIndex = 0
        for i in range(5):
            if(output_data[i] > score):
                score = output_data[i]
                labelIndex = i
        icon = self.labels[labelIndex]
        if(score < 80):
            icon = ""
            
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