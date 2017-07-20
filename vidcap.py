import cv2
import numpy as np 
def uploadvid_cap(x):
	faces_cascade=cv2.CascadeClassifier('/home/athul/myproject/haarcascade_frontalface_default.xml')
	cap=cv2.VideoCapture(x)

	while True:
		ret,frame=cap.read()
		if ret:

			gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		# print cap.shape
			faces=faces_cascade.detectMultiScale(gray,1.5,5)
			for x,y,w,h in faces:
				cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,255),2)
			cv2.imshow('video',gray)
			return len(faces)
			# imgg = cv2.resize(gray, (500, 500)) 
			# cv2.imshow('Frame',imgg)
			

		if cv2.waitKey(1) &0xFF== ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()
	# print"Number of faces: "+ str(len(faces))
	# return len(faces)rin
# uploadvid_cap()
