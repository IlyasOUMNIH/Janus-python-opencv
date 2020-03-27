import numpy as np
import cv2
import sys

rtmp_addr = "rtmp://192.168.1.16/live/test"
cap = cv2.VideoCapture(rtmp_addr)


#fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
#print('fourcc : ',fourcc)
#vid = cv2.VideoWriter('output.mp4',fourcc, 15.0,(640,480))

fourcc = cv2.VideoWriter_fourcc(*'H264')
#vid = cv2.VideoWriter('appsrc ! queue ! videoconvert ! video/x-raw ! omxh264enc ! video/x-h264 ! h264parse ! rtph264pay ! udpsink host=192.168.1.16 port=8004 sync=false',0,25.0,(640,480))

vid = cv2.VideoWriter('appsrc ! videoconvert ! x264enc noise-reduction=10000 tune=zerolatency byte-stream=true threads=4 ! mpegtsmux ! udpsink host=192.168.1.16 port=8004',0,25.0,(640,480))

while(True):
	ret, frame = cap.read()
	if ret==True:
		vid.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
vid.release()
cv2.destroyAllWindows()


#gst-launch-1.0 -v rtmpsrc location=rtmp://192.168.1.16/live/test ! flvdemux ! h264parse ! rtph264pay ! udpsink host=192.168.1.16 port=8004


#gst-launch-1.0 -v rtmpsrc location=rtmp://192.168.1.16/live/test ! appsrc ! videoconvert ! x264enc noise-reduction=10000 tune=zerolatency byte-stream=true threads=4 ! mpegtsmux ! udpsink host=192.168.1.16 port=8004

#gst-launch-1.0 -v rtmpsrc location=rtmp://192.168.1.16/live/test ! h264parse ! rtph264pay ! udpsink host=192.168.1.16 port=8004
