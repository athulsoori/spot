import numpy as np
import cv2
import math
import time
# import videocap
# def capture():

def count_face():
	faces_cascade=cv2.CascadeClassifier('/home/athul/EY/haarcascade_frontalface_default.xml')
	cap=cv2.VideoCapture('http://172.16.5.236:8080/video')
	# ret,frame=cap.read()

	while (cap.isOpened()):
		
		ret,frame=cap.read()
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces=faces_cascade.detectMultiScale(gray,1.3,5)
		for x,y,w,h in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
		
		new_frame=cv2.resize(frame, (1000,1000))
		cv2.imshow('frame',new_frame)
		if cv2.waitKey(1)&0xff==ord('q'):
			cv2.imwrite("snap.jpg",frame)
			break
	cap.release()
	cv2.destroyAllWindows()
	
	
	img=cv2.imread('/home/athul/myproject/snap.jpg')

	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	
	faces=faces_cascade.detectMultiScale(gray,1.3,5)
	
	for (x,y,w,h) in faces:
		font=cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img,time.strftime('%H:%M:%S'),(50,50),font,0.5,(255,255,0),2,cv2.LINE_AA)
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)	
	#length=len(faces)
	#cv2.putText(img,str(length),(200,200),font,0.5,(255,255,0),2,cv2.LINE_AA)
	
		#bgmask=background.apply(frame)
	imgg = cv2.resize(img, (1366, 720)) 

	cv2.destroyAllWindows()
	count=len(faces)
	print count
	# return count,imgg
# capture()
# count_face()
#displaying the image

	

#cv2.imshow('frame',frame)
	
    	
	#k=cv2.waitKey(1)&0xFF
	#if k==ord('q'):
	#	break
	#cv2.putText(frame, time.strftime("%H:%M:%S"),
              #  (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	
	
#img.release()
#cv2.destroyAllWindows()


