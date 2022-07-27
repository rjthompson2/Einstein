import subprocess
class Timer():
    def __init__(self):
        self.set = False

    def set_time(self, amount:str):
        # echo /usr/bin/the_command options | at now + 1 day
        command = "echo /usr/bin/the_command options | at now + "
        self.check_amount(amount)
        bash_command = command + amount
        process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        return

    def check_amount(self, amount:str) -> str:
        #checks that the amount is correct
        return

    def alert(self):
        return