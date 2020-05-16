import numpy as np
import cv2
import os
import paho.mqtt.client as mqtt

client = mqtt.Client("face")
client.connect('mosquitto',port=1883)


# Using HAAR Cascade Classifier for Face Detection
xml_path = '/usr/share/OpenCV/haarcascades/'

face_cascade = cv2.CascadeClassifier(xml_path + 'haarcascade_frontalface_default.xml')

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break

    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # face detection and other logic goes here
    
    # Arguments are the image, scale factor, and the number of neighbors for each candidate
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # Grab the face and dump it to bytes
        # The face resides between the start x and y plus the width and height
        face = gray[y:y+h,x:x+w]
        cv2.imshow('Capture - Face Detection', face)
         
        # Encode as PNG
        rc, png = cv2.imencode('.png', face)
        msg = png.tobytes()
        client.publish('hw3_topic', payload=msg)
    if cv2.waitKey(10) == 27:
        break

