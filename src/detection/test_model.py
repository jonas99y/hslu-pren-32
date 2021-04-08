import tensorflow as tf
import numpy as np
import cv2
import pathlib

required_confidence = 0.5

interpreter = tf.lite.Interpreter(model_path="src\\detection\\obstacle_detection_model.tflite")

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)
print(output_details)

interpreter.allocate_tensors()

for file in pathlib.Path("src\\detection\\img").iterdir():
    img = cv2.imread(r"{}".format(file.resolve()))
    new_img = cv2.resize(img, (512, 512))

    interpreter.set_tensor(input_details[0]['index'], [new_img])

    interpreter.invoke()
    rects = interpreter.get_tensor(
        output_details[0]['index'])
    labels = interpreter.get_tensor(
        output_details[1]['index'])
    scores = interpreter.get_tensor(
        output_details[2]['index'])

    print(f"For file {file.stem}")
    index_max = scores.size - 1
    for i in range(0,index_max):
        if(scores[0][i] > required_confidence):
            print(f"score: {scores[0][i]}, box: {rects[0][i]}")