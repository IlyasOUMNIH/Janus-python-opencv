import numpy as np
import cv2
import sys


rtmp_url = "rtmp://192.168.1.16/live/test"

cap = cv2.VideoCapture(rtmp_url) #open the camera
fourcc = cv2.VideoWriter_fourcc(*'X264')
# sample
#out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay config-interval=1 pt=96 ! udpsink host=192.168.1.16 port=8004',fourcc,20, (800,600),True) #ouput GStreamer pipeline

# for rtmp
#out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay ! udpsink host=192.168.1.16 port=8004',fourcc,20, (3840,1920),True) #ouput GStreamer pipeline

# works with internal camera
#out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay ! udpsink host=192.168.1.16 port=8004',fourcc,20, (1280,720),True) #ouput GStreamer pipeline

# THETA V
out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay ! udpsink host=192.168.1.16 port=8004',fourcc,30, (3840,1920),True) #ouput GStreamer pipeline


while True:
	ret,frame = cap.read()

	if ret:

		#w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		#h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		#print(w,',',h)
	# Write to pipeline
		#cv2.imshow('frame',frame)
		out.write(frame)
		if cv2.waitKey(1)&0xFF == ord('q'):
			break

cap_send.release()
out_send.release()
