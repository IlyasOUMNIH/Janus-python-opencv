import numpy as np
import cv2
import sys
import math

def drawRectangle( frame, w, h ):
	start_point = (math.floor(w/2) - 200, math.floor(h/2) - 200) 
	
	# Ending coordinate, here (125, 80) 
	# represents the bottom right corner of rectangle 
	end_point = (math.floor(w/2) + 200, math.floor(h/2) + 200) 
	   
	# Black color in BGR 
	color = (0, 0, 0) 
	   
	# Line thickness of -1 px 
	# Thickness of -1 will fill the entire shape 
	thickness = -1
	   
	# Using cv2.rectangle() method 
	# Draw a rectangle of black color of thickness -1 px 
	frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
	return;

def insertText(frame,text):
	# font 
	font = cv2.FONT_HERSHEY_SIMPLEX 
	  
	# org 
	org = (50, 50) 
	  
	# fontScale 
	fontScale = 1
	   
	# Blue color in BGR 
	color = (255, 0, 0) 
	  
	# Line thickness of 2 px 
	thickness = 2
	   
	# Using cv2.putText() method 
	frame = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA) 


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
out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency noise-reduction=10000 bitrate=2048 speed-preset=superfast ! rtph264pay ! udpsink host=192.168.1.16 port=8004',fourcc,60, (1920,960),True) #ouput GStreamer pipeline

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
print('fps : ',fps,' | ',w,',',h)

while True:
	ret,frame = cap.read()

	if ret:
		#cv2.imshow('frame',frame)
		
		#drawRectangle(frame,w,h)
		#insertText(frame, "5GHive TV : Insert video analysis here :)")
		
		# Write to pipeline
		out.write(frame)
		if cv2.waitKey(1)&0xFF == ord('q'):
			break

cap_send.release()
out_send.release()





