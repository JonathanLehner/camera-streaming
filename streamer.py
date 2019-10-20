# run this program on each RPi to send a labelled image stream
import socket
import time
from imutils.video import VideoStream
import imagezmq
import cv2
 
sender = imagezmq.ImageSender(connect_to='tcp://10.1.1.224:5555')
 
rpi_name = socket.gethostname() # send RPi hostname with each image
picam = VideoStream(usePiCamera=False).start()
time.sleep(2.0)  # allow camera sensor to warm up
while True:  # send images as stream until Ctrl-C
       image = picam.read()
       resized = cv2.resize(image, (224, 224), interpolation = cv2.INTER_AREA)
       cv2.imshow("Resized image", resized) # doesn't show somehow
       sender.send_image(rpi_name, resized)
