 # W251 - Summer 20200 - Lab 3
 
 
 
 ## Part 2
 Motion detection instead of face capture. Same concept as homework 3 though. Implemented the motiona capture with blur using cv2 package in python (same as the facial capture). This time we use methods:
 - createBackgroundSubtractorMOG2()
 - blur()
 The first method tries to remove the background from a frame or image. In our case we are streaming from a webcam and grabbing frames. We apply the createBackgroundSubtractorMOG2() method first which results in what resembles a negative. The blur function is then called with the specified 3,3 kernel. All this does is apply a gaussian blur to neiboring pixels and results in a smoothed image. We implement these methods sequentially in the context/face_blur.py script. This script is then added to a docker container called blurapp:v1 using the dockerfiles/Blur.Dockerfilr which is an exact copy of FD.Dockerfile used for HW3 except it uses face_blur.py insetead of face_detectory.py.
Image Built with `docker build -t blurapp:v1 -f dockerfiles/Blur.Dockerfile context`Our aplication is executed by first running a MQQT broker (not absolutely necessary but our python script assumes it is up and running) on a local network - in our case we do this using the mosquitto docker image we created for HW3 using the following command: `docker run --name=mosquitto --network hw03 -p 1883:1883 -ti --rm mosquitto` then we spin up our blurapp docker container using the following command
`xhost local:root
docker run -e DISPLAY=$DISPLAY --rm --privileged --env QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix:rw --device /dev/video0 --network=hw03 -ti blurapp:v1`

Voila! You should see a black and white image of yourself that responds to your movement.
 
