import subprocess
import time
from playsound import playsound

#TODO okayish for now need a better system
class Timer():
    def __init__(self):
        self.set = False
        self.time = 0

    def set_time(self, message:str) -> None:
        # echo /usr/bin/the_command options | at now + 1 day
        path = "/Users/rileythompson/Desktop" + "/Einstein/timer.py"
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
        print(self.time)


    def alert(self) -> None:
        while self.time > 0:
            time.sleep(1)
            self.time -= 1
            print(self.time)
        print("starting noise")
        playsound('Desktop/Einstein/alarm.wav')
        print("Timer done")

if __name__ == "__main__":
    t = Timer()
    t.alert()