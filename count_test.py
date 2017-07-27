import numpy as np
import cv2
import math
import time
import os
import sqlite3
# import videocap
# def capture():
list=[]
faces_cascade=cv2.CascadeClassifier('/home/athul/myproject/haarcascades/haarcascade_frontalface_default.xml')
fn_dir='/home/athul/myproject/'
fn_name='img'
def create_connection(db_file):
	try:
		conn=sqlite3.connect(db_file)
		print "connection successful"
		return conn 
	except Exception as e:
		print e
	# except Error as e:
	# 	print e
	return None
def snap(new_frame):
	# if  frame_count%5==0:
	# 	cv2.imwrite('snap.jpg', new_frame)
	img=cv2.imread('/home/athul/myproject/img/snap.jpg')

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
	t=str(time.strftime('%H:%M:%S'))
	date= str(time.strftime("%x"))
     	cv2.imshow('Image', imgg)
	cv2.destroyAllWindows()
	count_face=int(len(faces))
	result_count=count_face
	result_time=t
	
	
	print "Count is:  " + str(count_face)  +"  Time : " + str(t)

	return count_face,t,date
	

	# conn.commit()
	# conn.close
def count_face():
	
	cap=cv2.VideoCapture(0)
	# ret,frame=cap.read()
	fps=cap.get(cv2.CAP_PROP_FPS)
	print int(fps)
	frame_count=0

	path = os.path.join(fn_dir, fn_name)

	# pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
 #         if n[0]!='.' ]+[0])[-1] + 1

	while (cap.isOpened()):
		ret,frame=cap.read()
		frame_count=frame_count+1
		stop=0
		
		# print ret
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces=faces_cascade.detectMultiScale(gray,1.3,5)
		for x,y,w,h in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
		
		new_frame=cv2.resize(frame, (500,500))
		# if frame_id % math.floor
		cv2.imshow('frame',new_frame)
		time=int(frame_count/fps)
		# print frame_count
		# snap(new_frame,frame_count)
		if frame_count % 30 ==0:
			# print frame_count%30
			cv2.imwrite('%s/snap.jpg'%(path), frame)
			x,y,z=snap(new_frame)
			# conn.commit()
			return x,y,z,stop
		elif cv2.waitKey(1)&0xFF==ord('q'):
			stop=1
			x,y,z=snap(new_frame)
			return x,y,z,stop
			break
				
	cap.release()
	cv2.destroyAllWindows()
	# return a,b
	
	
	# return count,imgg
# capture()q
# query2='CREATE TABLE COUNT_T
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


