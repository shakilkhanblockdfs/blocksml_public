import pyttsx3

friend =  pyttsx3.init()
speech = ""

while(speech != 'x') :
	speech = input("Say Something to convert to Voice. Press x to terminate: ")

	if(speech == 'x'):
		friend.say("Now I am going to terminate as you pressed x")
	else:	
		friend.say(speech)

	friend.runAndWait()
