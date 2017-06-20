import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
	
	#print ("entra ciclo")
	_,frame =cap.read()
	hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red= np.array([150,150,50])
	upper_red= np.array([180,255,255])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res= cv2.bitwise_and(frame, frame, mask =mask)

	kernel2= np.ones((5,5), np.uint8)
	erosion= cv2.erode(mask, kernel2, iterations =1)
	dilation = cv2.dilate(erosion,kernel2, iterations= 1)


	kernel = np.ones((15,15), np.float32)/225
	smoothed = cv2.filter2D(dilation,-1,kernel)
	blur= cv2.GaussianBlur(smoothed,(15,15),0)
	median = cv2.medianBlur(blur,15)

	cv2.imshow('frame', frame)
	#cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	cv2.imshow('result',median)

	k= cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
