import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
	
	#print ("entra ciclo")
	_,frame =cap.read()
	# define the list of boundaries
	boundaries = [
	#([17, 15, 100], [50, 56, 200]), #red
	#([86, 31, 4], [220, 88, 50]), #blue 
	#([25, 146, 190], [62, 174, 250]), #yellow
	#([103, 86, 65], [145, 133, 128]) #gray
	# ([4,4,4], [65,65,66]) #black
	#([224,224,224],[255,255,255]) #white
	#([120,147,156], [179,219,232])#Beige
	#([15,48,59],[36,118,145]) #Beige piel
	([11,35,43],[35,101,122]) #Brown detecta cabello
	]

	# loop over the boundaries
	for (lower, upper) in boundaries:
		# create NumPy arrays from the boundaries
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")

		# find the colors within the specified boundaries and apply
		# the mask
		mask = cv2.inRange(frame, lower, upper)
		output = cv2.bitwise_and(frame, frame, mask = mask)

		cv2.imshow('frame', frame)
		cv2.imshow('mask',mask)

	k= cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
