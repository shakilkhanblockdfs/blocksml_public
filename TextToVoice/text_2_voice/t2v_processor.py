#!/usr/bin/python3

from t2v_global_config import *
from t2v_magic import *

from t2v_pdf_to_text import *
from t2v_jpeg_to_text import *
from t2v_text_to_mp3 import *
from t2v_processor import *

def convert_to_voice(input_filename):
	## Check if the file is either of text, PDF, JPEG, else return None
	## Call the appropriate method for the PDF, JPEG conversion
	## Check if the converted text file has characters greater than certain 
	# threshold else return None
	##  Convert the file to mp3 and return the filename

	valid_file_type = ["pdf","text","jpeg"]
	f_magic = get_file_magic("./static/upload/" + input_filename)

	if not f_magic in valid_file_type:
		print("Debug file doesn't have valid magic to convert")
		return None

	if f_magic == "pdf":
		converted_text_file = convert_pdf_to_text(input_filename)
		print_debug(f"Converting the file {input_filename} from PDF to text")
		##todo:shakil .. Check if the file has valid text or blank
	elif f_magic == "jpeg":
		converted_text_file = convert_jpeg_to_text(input_filename)
		print_debug(f"Converting the file {input_filename} from JPEG to text")
	elif f_magic == "text":
		cmd = "/bin/cp " + "./static/upload/" + input_filename + " " + "./static/converted_text/" + input_filename
		(status, output) = subprocess.getstatusoutput(cmd)
		print_debug(f"Copying the file {input_filename} converted_text")
		print_debug(f" The status of copying the text file is {status}")
		print_debug(f" The output of copying the text file is {output}")
		converted_text_file = "./static/converted_text/" + input_filename
	else:
		return None

	converted_mp3_filename = convert_text_to_mp3(converted_text_file)

	##todo:shakil.. Check if we need to do validation on the converted_mp3_filename

	return converted_mp3_filename		
	


	
		
