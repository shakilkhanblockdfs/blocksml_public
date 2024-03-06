#!/usr/local/bin/python3

import speech_recognition as sr
listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Listening')
        voice = listener.listen(source, timeout=2, phrase_time_limit=4)
        # voice = listener.listen(source)
        command = listener.recognize_google(voice)
        # command = listener.recognize_google()
        print(command)
except:
    pass
