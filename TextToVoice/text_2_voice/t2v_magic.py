import magic
import subprocess
import os
from os import walk
from os.path import isfile


def list_files(my_path):
	cmd = "/usr/bin/find "  + my_path + " -type f"
	(status, output) = subprocess.getstatusoutput(cmd)	
	if status:
		return None
	else:
		return output.split("\n")
	

def get_file_magic(complete_filename_with_path):
	try:
		mime = magic.Magic(mime=True)
		l_magic = mime.from_file(complete_filename_with_path)
		print(f"debug output: {complete_filename_with_path} --------> {l_magic}")

		if l_magic == "video/mp4":
			return "mp4"
		if l_magic == "audio/mpeg":
			return "mp3"
		if l_magic == "video/webm":
			return "webm"
		if l_magic == "video/x-matroska":
			return "mkv"
		if l_magic == "application/pdf":
			return "pdf"
		if l_magic == "application/msword":
			return "doc"
		if l_magic == "image/jpeg":
			return "jpeg"
		if l_magic == "text/plain":
			return "text"
		if l_magic == "inode/x-empty":
			return "empty"

	except:
		return None

if __name__ == "__main__":
	path = "./upload"

	file_list = list_files(path)
	#print(file_list)

	if file_list:	
		for file_t in file_list:
			mime_type = get_file_magic(file_t)
			print(f" {file_t} == {mime_type}")	

