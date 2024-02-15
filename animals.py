

import tensorflow as tf
import numpy as np
import cv2

# Load the MobileNetV2 model
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Open the video file
cap = cv2.VideoCapture("test.mp4")

if not cap.isOpened():
    print("Error: Unable to open video file.")
    exit()

# Read and process each frame from the video
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to the required input dimensions of MobileNetV2 (224x224 pixels)
    resized = cv2.resize(frame, (224, 224))
    resized = tf.keras.preprocessing.image.img_to_array(resized)
    resized = tf.keras.applications.mobilenet_v2.preprocess_input(resized)

    # Make predictions
    predictions = model.predict(np.array([resized]))
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=2)

    # Display top predictions for each frame
    for _, label, score in decoded_predictions[0]:
        print(f"ceci est  {label}: probability {score}")

    # Display the frame with predictions (you can also save it to a video file)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

