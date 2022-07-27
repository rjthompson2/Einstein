import speech_recognition as sr
import time
from commands import Commands
import requests, json

def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("I am listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data


time.sleep(2)
commands = Commands()
commands.respond("Hi, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = commands.understand(data)