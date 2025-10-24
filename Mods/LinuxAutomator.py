# # Use 'dir' instead of 'ls' on Windows
# #runs dir and captures it in a var
# a = subprocess.run("dir", stdout=subprocess.PIPE, shell=True)
# wslls = subprocess.run("wsl ls", stdout=subprocess.PIPE, shell=True)
# print(wslls.stdout.decode())
def runLinuxCommand(command):
    import os
    import subprocess


    islin = ""
    if os.name == 'nt':
        islin = "wsl "
    else:
        islin = ""

    commandOutput = subprocess.run(f"{islin} {command}", stdout=subprocess.PIPE, shell=True)


    return commandOutput.stdout.decode()


a = runLinuxCommand("ls")
print(a)