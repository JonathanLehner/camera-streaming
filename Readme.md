Easy way:
- Using code from https://github.com/jeffbass/imagezmq (MIT license)
- use hostname -I to get your own ip address (Windows)
- Head to the Apple menu > System Preferences > Network and then select the connection you are currently using (Mac)
- gives crazy latency with small images ~224x224, but lags a few seconds with full HD
- on raspberry pi might need
  sudo apt-get install libatlas-base-dev to install numpy (and some other packages for opencv, and then change ispicamera to True and install picamera package) and https://medium.com/@kennethjiang/calibrate-fisheye-lens-using-opencv-333b05afa0b0
  
Alternative 1:
- ffmpeg  
- https://github.com/illuspas/Node-Media-Server or: (untested since C++ https://github.com/xiongziliang/ZLMediaKit) 
- https://github.com/Fonbet/argus-tensor-stream

Video direct stream: 
- ffmpeg -re -i ~/video.mp4 -vcodec libx264 -r 30 -g 60 -f flv -listen 1 rtmp://0.0.0.0:1935/live/app

With stream server
Video:
- ffmpeg -re -i ~/video.mp4 -vcodec libx264 -r 30 -g 60 -f flv rtmp://0.0.0.0:1935/live/app
Webcam MacOS:
- ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i "0" -c:v libx264 -preset ultrafast -tune zerolatency -c:a aac -ar 44100 -vf scale=320:-1 -f flv rtmp://localhost/live/jonathan

With stream server 
For ML: change version → needed for argus stream
- ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i "0" -c:v libx264 -preset ultrafast -tune zerolatency -movflags frag_keyframe+empty_moov -c:a aac -ar 44100 -pix_fmt yuv420p -vf scale=320:-1 -f flv rtmp://localhost/live/jonathan

Explanation of flags
- -movflags frag_keyframe+empty_moov --- seems doesn’t make a difference
- -preset ultrafast -tune zerolatency --- makes a bit faster

Streaming rawvideo
- ffmpeg -f avfoundation -framerate 30 -video_size 1280x720 -i "0" -c:v rawvideo -vf scale=320:-1 -f rawvideo -pixel_format bgr24 -listen 1 rtmp://0.0.0.0:1935
- cannot figure out how to display this on screen

Resources
- server side https://gist.github.com/nico-lab/e1ba48c33bf2c7e1d9ffdd9c1b8d0493
- https://gist.github.com/Brainiarc7/4636a162ef7dc2e8c9c4c1d4ae887c0e 
- (untested) https://stackoverflow.com/questions/21213895/how-to-stream-live-videos-with-no-latency-ffplay-mplayer-and-what-kind-of-wra




Alternative 2:
- sudo ./mjpg_streamer -i "./input_uvc.so -f 10 -r 640x320 -n -y" -o "./output_http.so -w ./www -p 80"
- not recommended, due to being unmaintained and getting stuck sometimes. Cannot deal with high resolutions on the raspberry pi.

If not using a media server the connection has to be inside the same network. Otherwise NAT traversal has probably to be achieved. For this another service such as Ngrok or inlet (https://github.com/inlets/inlets) is necessary.
