import tensorflow as tf
import numpy as np
import cv2
import time
from videoStream import VideoStream

class IconClassifier:
    def __init__(self, resolutionWidth=640, resolutionHeight=480):
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
        videostream = VideoStream(resolution=(self._resolutionWidth,self._resolutionHeight),framerate=30).start()
        time.sleep(1)

        # Grab frame from video stream
        frame1 = videostream.read()

        # Crop frame
        frame = frame1[cropHeight:self._resolutionHeight, 0:self._resolutionWidth]

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

        # print(f"the output is {output_data}")
        # print(f"{icon} detected")

        videostream.stop()

        return icon

def main():
    imW = 640
    imH = 480
    cropHeight = 240
    labelPath = "pren2_team32_icons_model_dict.txt"
    modelPath = "pren2_team32_icons_model.tflite"

    classifier = IconClassifier(resolutionWidth=imW, resolutionHeight=imH)
    detectedIcon = classifier.detectIcon(modelPath=modelPath, labelPath=labelPath, cropHeight=cropHeight)
    print(detectedIcon)

if __name__ == '__main__':
    main()