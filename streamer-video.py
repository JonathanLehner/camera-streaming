# run this program on each RPi to send a labelled image stream
import socket
import time
from imutils.video import FileVideoStream
import imagezmq
 
sender = imagezmq.ImageSender(connect_to='tcp://10.1.1.224:5555')
 
rpi_name = socket.gethostname() # send RPi hostname with each image
picam = FileVideoStream("/Users/Jonathanlehner/Asianriding.mp4").start()
time.sleep(2.0)  # allow camera sensor to warm up

while True:  # send images as stream until Ctrl-C
       image = picam.read()
       sender.send_image(rpi_name, image)
