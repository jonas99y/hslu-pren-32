import tensorflow as tf
import numpy as np
import cv2
import time
from threading import Thread
from pathlib import Path
from videoStream import VideoStream
from obstacledetectiondata import ObstacleDetectionData

class ObstacleDetector:
    def __init__(self, obstacleDetectionData: ObstacleDetectionData, minConfidenceThreshold = 0.5, resolutionWidth = 640, resolutionHeight = 480):
        self._minConfidenceThreshold = minConfidenceThreshold
        self._resolutionWidth = resolutionWidth
        self._resolutionHeight = resolutionHeight
        self._detecting = False
        self._obstacleDetectionData = obstacleDetectionData

    def startDetection(self, modelPath):
        self.detecting = True
        interpreter = tf.lite.Interpreter(model_path=modelPath)

        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        height = input_details[0]['shape'][1]
        width = input_details[0]['shape'][2]

        # Initialize video stream
        videostream = VideoStream(resolution=(self._resolutionWidth,self._resolutionHeight),framerate=30).start()
        time.sleep(1)

        cycle = 0
        #for frame1 in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
        while self.detecting:

            cycle += 1
            # Grab frame from video stream
            frame1 = videostream.read()

            # Acquire frame and resize to expected shape [1xHxWx3]
            frame = frame1.copy()
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_resized = cv2.resize(frame_rgb, (width, height))
            input_data = np.expand_dims(frame_resized, axis=0)

            # Perform the actual detection by running the model with the image as input
            interpreter.set_tensor(input_details[0]['index'],input_data)
            interpreter.invoke()

            # Retrieve detection results
            boxes = interpreter.get_tensor(output_details[0]['index'])[0] # Bounding box coordinates of detected objects
            classes = interpreter.get_tensor(output_details[1]['index'])[0] # Class index of detected objects
            scores = interpreter.get_tensor(output_details[2]['index'])[0] # Confidence of detected objects
            
            data = {}
            data['cycle'] = cycle
            data['detected obstacles'] = []

            obstacleNumber = 0
            # Loop over all detections and draw detection box if confidence is above minimum threshold
            for i in range(len(scores)):
                if ((scores[i] > self._minConfidenceThreshold) and (scores[i] <= 1.0)):
                    obstacleNumber += 1

                    # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
                    obstacleData = {}
                    obstacleData['obstacle number'] = obstacleNumber
                    obstacleData['confidence'] = scores[i]
                    obstacleData['ymin'] = float(max(0,boxes[i][0]))
                    obstacleData['xmin'] = float(max(0,boxes[i][1]))
                    obstacleData['ymax'] = float(min(1,boxes[i][2]))
                    obstacleData['xmax'] = float(min(1,boxes[i][3]))

                    data['detected obstacles'].append(obstacleData)

            self._obstacleDetectionData.write(data)

        # Clean up
        cv2.destroyAllWindows()
        videostream.stop()

    def stopDetection(self):
        self._detecting = False

def main():  
    min_conf_threshold = 0.5
    imW = 640
    imH = 480
    labelsPath = 'obstacle_detection_labels.txt'
    modelPath = 'pren2_team32_obstacles_model_2.tflite'

    detector = ObstacleDetector(ObstacleDetectionData((Path(__file__).parent/'obstacles')), minConfidenceThreshold=min_conf_threshold, resolutionHeight=imH, resolutionWidth=imW)
    detector.startDetection(labelsPath=labelsPath, modelPath=modelPath)

    time.sleep(5)

    detector.stopDetection()

if __name__ == '__main__':
    main()