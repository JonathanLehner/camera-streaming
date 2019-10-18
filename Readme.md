Easy way:
Using code from https://github.com/jeffbass/imagezmq (MIT license)

Alternative 1:
Use
- ffmpeg  
- https://github.com/illuspas/Node-Media-Server
- https://github.com/Fonbet/argus-tensor-stream

Alternative 2:
sudo ./mjpg_streamer -i "./input_uvc.so -f 10 -r 640x320 -n -y" -o "./output_http.so -w ./www -p 80"
not recommended, due to being unmaintained and getting stuck sometimes. Cannot deal with high resolutions on the raspberry pi.

If not using a media server the connection has to be inside the same network. Otherwise NAT traversal has probably to be achieved. For this another service such as Ngrok or inlet (https://github.com/inlets/inlets) is necessary.
