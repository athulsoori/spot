import sqlite3
import time
import datetime
conn=sqlite3.connect('spot_db.db')
c=conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS result(count TEXT, face_time REAL)')
def data_entry():
	c.execute("INSERT INTO st VALUES ('athul',5)")
	conn.commit()
	
#  ()
stop=0
def entry():
	from count_test import count_face,snap
	count_new,time_new,current_date,stop=count_face()


	# unix=time.time()
	# keyword='python'
	c.execute("INSERT INTO result (count,face_time,face_date) VALUES (?,?,?)",
		(count_new,time_new,current_date))
	conn.commit()
	if stop == 1:
		exit()

# 
# create_table()
# for i in range(1,10):
# 	entry()
# 	time.sleep(1)
while stop ==0:
	entry()

c.close()
conn.close()