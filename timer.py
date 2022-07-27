import subprocess
from playsound import playsound

class Timer():
    def __init__(self):
        self.set = False

    def set_time(self, amount:str) -> None:
        # echo /usr/bin/the_command options | at now + 1 day
        path = "~/Desktop" + "/Einstein/timer.py"
        command = f"python {path} | at "
        bash_command = command + amount
        print(bash_command)
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    # def set_time_map(self, arg_map:dict) -> None:
    #     command = ""
    #     if "for" in arg_map:
    #         return
    #     if "at" in arg_map:
    #         return
    #     if "on" in arg_map:
    #         return
    #     if "in" in arg_map:
    #         return

    def alert(self) -> None:
        playsound('Desktop/Einstein/alarm.wav')

if __name__ == "__main__":
    t = Timer()
    t.alert()