import sys

from gtts import gTTS
import os

def convert_text_to_mp3(input_filename):
    fh = open(input_filename, "r")
    #todo::shakil Later on make sure that we have limited characters in text file so not to buffer overflow
    mytext =  fh.read()

    ## Later on take user inout for the language
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    mp3_saved_path = "./static/converted_mp3/"+os.path.basename(input_filename)+".mp3"
    myobj.save(mp3_saved_path)
    return mp3_saved_path

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print("Please find the filename to convert to mp3")
		sys.exit(0)

	convert_text_to_mp3(sys.argv[1])
