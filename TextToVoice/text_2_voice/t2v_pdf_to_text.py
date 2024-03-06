import subprocess

def convert_pdf_to_text(input_filename):
    cmd = "/usr/bin/python3 ./ocr_sdk/process.py " + "./static/upload/" +  input_filename + " ./static/converted_text/" +input_filename + ".txt"
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        return "./static/converted_text/"+input_filename+".txt"
    else:
        ##todo:shakil..change this later to print debug
        print(output)
        return None
