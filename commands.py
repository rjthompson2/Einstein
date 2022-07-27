from typing import Tuple
from time import ctime
from gtts import gTTS
from listener import Listener
import os
import datetime

class Commands():
    def __init__(self, listener:Listener):
        self.sleep = False
        self.listener = listener

    def understand(self, data) -> None:
        if "hey Einstein" in data:
            self.respond("yes?")
            self.sleep = False

        elif not self.sleep:
            if "what time is it" in data or "what's the time" in data:
                self.respond(ctime())
            
            #TODO provide list of commands a user can input
            # if "list commands" in data or "help" in data:
                
            elif "okay thank you" in data:
                self.sleep = True
                self.respond("You're welcome. say 'hey Einstein' if you need more help")

            elif "go to sleep" in data:
                self.sleep = True
                self.respond("Say 'hey Einstein' to wake me")

            elif "write a note" in data:
                self.respond("What should i write?")
                note = self.listener.listen()
                file = open('notes.txt', 'w')
                self.respond("Should I include the time?")
                answer = self.listener.listen()
                if 'yes' in answer or 'sure' in answer or 'yeah' in answer:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
            
            elif "show note" in data or "read note" in data or "show notes" in data or "read notes" in data:
                self.respond("Reading notes")
                file = open("notes.txt", "r")
                print(file.read())
                self.respond(file.read(6))

            elif "calculate" in data:
                data = data.lstrip('calculate ')
                calculation = eval(data)
                print(calculation)
                self.respond(data + " is " + str(calculation))

            else:
                print('Unable to process command')
                self.respond("Sorry I did not get that")

                
        if "stop listening" in data:
            print('Listening stopped')
            self.respond("Okay shutting down")
            self.listener.listening = False
        
    def respond(self, audioString:str) -> None:
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("speech.mp3")
        os.system("mpg321 speech.mp3")