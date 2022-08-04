import time
from commands import Commands
from listener import Listener
from utils import respond

time.sleep(2)
listener = Listener()
commands = Commands(listener)
respond("Hi, what can I do for you?")
while listener.listening:
    data = listener.listen()
    commands.understand(data)