import subprocess
import time
import os

#TODO sound not playing
path = '/Users/rileythompson/' + 'Desktop/Einstein/alarm.wav'
class Timer():
    def __init__(self):
        self.time = 0

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
        path = "Desktop/Einstein/alarm.wav"
        os.system("mpg321 " + path)

if __name__ == "__main__":
    t = Timer()
    t.alert()