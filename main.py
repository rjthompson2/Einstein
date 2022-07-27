import time
from commands import Commands
from listener import Listener

time.sleep(2)
listener = Listener()
commands = Commands(listener)
commands.respond("Hi, what can I do for you?")
listening = True
while listener.listening:
    data = listener.listen()
    commands.understand(data)