import cv2
from PIL import Image
import numpy as np 
def image_cap(x):
	
	faces_cascade=cv2.CascadeClassifier('/home/athul/EY/haarcascade_frontalface_default.xml')
	img=cv2.imread(x)
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faces_cascade.detectMultiScale(gray,1.3,5)
	for x,y,w,h in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	print"Number of faces: "+ str(len(faces))
	return len(faces)
# image_cap()
