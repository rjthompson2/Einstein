from typing import Tuple
from time import ctime
from gtts import gTTS
import os

class Commands():
    def __init__(self):
        self.sleep = False

    def understand(self, data):
        if not self.sleep:
            if "what time is it" in data:
                self.respond(ctime())

            elif "okay thank you" in data:
                self.sleep = True
                self.respond("You're welcome. say 'hey Einstein' if you need more help")

            elif "go to sleep" in data:
                self.sleep = True
                self.respond("say 'hey Einstein' to wake me")

            else:
                print('Unable to process command')
                self.respond("sorry I did not get that")

        elif "hey Einstein" in data:
            self.respond("yes?")
            self.sleep = False
                
        if "stop listening" in data:
            print('Listening stopped')
            self.respond("okay shutting down")
            return False

        return True
        
    def respond(self, audioString:str) -> None:
        print(audioString)
        tts = gTTS(text=audioString, lang='en')
        tts.save("speech.mp3")
        os.system("mpg321 speech.mp3")