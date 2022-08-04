from gtts import gTTS
import os

def respond(audioString:str) -> None:
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")