from __future__ import print_function
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from count import *

UPLOAD_FOLDER = '/uploads'

import sys
import json
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# c=0;
CORS(app)

@app.route('/run', methods=['POST'])
def run():
	print(request.files, file=sys.stdout)

	if request.method=='POST':
		if 'filename' not in request.files:
			return jsonify({'error':'no file'}),422

		file=request.files['filename']
		if file:
			# print (file,file.filename)
			filename=secure_filename(file.filename)
			file.save(filename)
			from  imgcap import image_cap

			x=image_cap(file.filename)
			# x = count()
			# #somefunction(file)
			return jsonify({'faces': x})
			# response.headers.add('Access-Control-Allow-Origin', 'null')
			# resp=json.loads(response)
			# return response,200
@app.route('/runvideo',methods=['POST'])
def runvideo():
	print(request.files,file=sys.stdout)
	if request.method=='POST':
		if 'filename' not in request.files:
			return jsonify({'error'}),422
		file=request.files['filename']
		if file:
			filename=secure_filename(file.filename)
			file.save(filename)
			from vidcap import uploadvid_cap
			face_video=uploadvid_cap(file.filename)
			# response.headers.add('Access-Control-Allow-Origin','null')
			return jsonify({'faces':face_video})

@app.route('/live_video',methods=['GET','POST'])
def live_video():
	result=count_face()
	return jsonify({'Faces':result})
	