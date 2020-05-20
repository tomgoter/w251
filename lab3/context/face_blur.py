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

fgbg = cv2.createBackgroundSubtractorMOG2()

kernel_size = (3,3)

while(1):
     ret, frame = cap.read()

     fgmask = fgbg.apply(frame)
     # Using cv2.blur() method  
     image = cv2.blur(fgmask, kernel_size)  
  
     # Displaying the image  
     cv2.imshow("Blurred Image", image)  
     k = cv2.waitKey(30) & 0xff
     if k == 27:
         break

cap.release()
cv2.destroyAllWindows()

