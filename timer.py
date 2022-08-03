import subprocess
import time
import os
from gtts import gTTS

path = '/Users/rileythompson/' + 'Desktop/Einstein/alarm.wav' #CHANGE DIRECTORY TO THE .WAV FILE

class Timer():
    def __init__(self):
        self.time = 0
        self.path = "Desktop/Einstein/alarm.wav"

    def set_time(self, message:str) -> None:
        if 'days' in message:
            amount = int(message.split('days')[0].split()[-1])
            amount = amount * 24 * 60 * 60
            self.time += amount
        if 'hours' in message:
            amount = int(message.split('hours')[0].split()[-1])
            amount = amount * 60 * 60
            self.time += amount
        if 'minutes' in message:
            amount = int(message.split('minutes')[0].split()[-1])
            amount = amount * 60
            self.time += amount
        if 'seconds' in message:
            amount = int(message.split('seconds')[0].split()[-1])
            self.time += amount


    def alert(self) -> None:
        while self.time > 0:
            time.sleep(1)
            self.time -= 1
            print(self.time)
        os.system("mpg321 " + self.path)


class Notification(Timer):
    def set_message(self, audioString:str) -> None:
        print(audioString)
        audioString = "You have a notification: " + audioString
        tts = gTTS(text=audioString, lang='en')
        tts.save("notify.mp3")
        self.path = "notify.mp3"
