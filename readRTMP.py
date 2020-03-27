import numpy as np
import cv2
import sys

rtmp_addr = "rtmp://192.168.1.16/live/test"
cap = cv2.VideoCapture(rtmp_addr)

while(True):
	ret, frame = cap.read()
	if ret==True:
		sys.stdout.buffer.write(frame.tostring())
	if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()
