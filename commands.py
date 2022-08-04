from time import ctime
from listener import Listener
from timer import Timer, Notification
from utils import respond
import os
import datetime

path = "/Users/rileythompson//Desktop/Einstein/" #SET YOUR OWN PATH TO EINSTEIN


class Commands():
    def __init__(self, listener:Listener):
        self.sleep = False
        self.listener = listener

    def understand(self, data) -> None:
        if "nevermind" in data:
            data = data.split('nevermind')[-1]

        if "stop listening" in data:
            print('Listening stopped')
            respond("Okay shutting down")
            self.listener.listening = False
            return

        if "hey Einstein" in data or "Einstein you there?" in data:
            respond("yes?")
            self.sleep = False

        elif not self.sleep:
            if "what time is it" in data or "what's the time" in data:
                respond(ctime())
                
            elif "okay thank you" in data:
                self.sleep = True
                respond("You're welcome. say 'hey Einstein' if you need more help")

            elif "go to sleep" in data:
                self.sleep = True
                respond("Say 'hey Einstein' to wake me")

            elif "write a note" in data:
                respond("What should i write?")
                note = self.listener.listen()
                file = open('notes.txt', 'w')
                respond("Should I include the time?")
                answer = self.listener.listen()
                if 'yes' in answer or 'sure' in answer or 'yeah' in answer:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                file.write(note)
                respond("Note saved")
            
            elif "show note" in data or "read note" in data or "show notes" in data or "read notes" in data:
                respond("Reading notes")
                file = open("notes.txt", "r")
                read_back = file.read()
                if read_back:
                    respond(read_back)
                else:
                    respond("Nothing in your notes")

            elif "calculate" in data:
                data = data.lstrip('calculate ')
                calculation = eval(data)
                print(calculation)
                respond(data + " is " + str(calculation))
            
            elif "help me" in data or "show commands" in data or "what do i do" in data or "list commands" in data:
                file = open(path+"help.txt", "r")
                read_back = file.read()
                print(read_back)
                respond(read_back)

            elif "record" in data or "start recording" in data:
                respond("Recording now")
                recording = ""
                listening = True
                while listening:
                    chunk = self.listener.listen()
                    if 'Einstein stop recording' in chunk:
                        recording += data.strip('Einstein stop recording') #TODO this will break it
                        break
                    recording += chunk
                file = open('recording.txt', 'w')
                respond("Should I include the time?")
                answer = self.listener.listen()
                if 'yes' in answer or 'sure' in answer or 'yeah' in answer:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                file.write(recording)
                respond("Note saved")

            elif "playback" in data:
                respond("Playing back recording")
                file = open("recording.txt", "r")
                read_back = file.read()
                if read_back:
                    respond(read_back)
                else:
                    respond("Nothing in your notes")

            elif "set a timer" in data or 'set an alarm' in data:
                data = data.lstrip("set a timer")
                data = data.lstrip(" for ")
                timer = Timer()
                timer.set_time(data)
                pid = os.fork()
                if pid > 0:
                    print(1)
                    respond("Okay timer set")
                else:
                    print(0)
                    timer.alert()
                    os._exit(0)

            elif "set a notification" in data or 'notify me' in data or 'remind me' in data or 'set a reminder' in data:
                respond("okay what would you like the message to say?")
                message = self.listener.listen()
                notification = Notification()
                notification.set_time(data)
                notification.set_message(message)
                pid = os.fork()
                if pid > 0:
                    respond("Okay notification set")
                else:
                    notification.alert()
                    os._exit(0)

            else:
                print('Unable to process command')
                respond("Sorry I did not get that")