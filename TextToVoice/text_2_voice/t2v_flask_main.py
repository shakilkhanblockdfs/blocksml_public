import os
from werkzeug.utils import secure_filename
from t2v_processor import *

#from flask import Flask, session, request, render_template
from flask import *
#from flask.ext.session import Session
app = Flask(__name__)  

@app.route('/')  
def upload():  
	return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
	if request.method == 'POST':  
		f = request.files['file']  
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))	
		voice_file_name = convert_to_voice(f.filename)
		print(f"File mp3 filename created is {voice_file_name}")
		#return render_template("success.html", name = f.filename)  
		session['voice_file_name'] = voice_file_name
		text_data = open( "./static/converted_text/"+f.filename+".txt","r").read()
		session['text_data'] = text_data
		print_debug(f"Now going to play {voice_file_name}")
		##todo:shakil..Check if the data needs to be display in text or PDF/jpg format
		## Check if we can make the text highlighted as its being read.
		return render_template('play_video.html',data=voice_file_name, text_data = text_data)

@app.route('/play_video')
def play_video():
	voice_file_name = session.get('voice_file_name', None)
	text_data = session.get('text_data', None)
	print(f"Now going to play the file {voice_file_name}")
	return render_template('play_video.html', data=voice_file_name, text_data=text_data)

def create_dir_recursively(my_path):
	os.makedirs(my_path, exist_ok=True)
  
if __name__ == '__main__':  
	app.secret_key = 'super secret key sucks'
	app.config['SESSION_TYPE'] = 'filesystem'

	create_dir_recursively("./static/upload")
	create_dir_recursively("./static/converted_text")
	create_dir_recursively("./static/converted_mp3")
	app.config['UPLOAD_FOLDER'] = './static/upload'
	app.config['MAX_CONTENT-PATH'] = 16*1024*1024
	app.run(host="0.0.0.0",port=8000, debug = True)  

