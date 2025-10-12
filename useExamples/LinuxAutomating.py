import subprocess
from Mods.Message import SendGetMessage

iswsl = False

def CheckForWsl():
    import os
    if os.name == "nt":
        iswsl = True
    else:
        iswsl = False
CheckForWsl()

result = "none"

command = "ls"

if iswsl:
    result = subprocess.run(f"wsl {command}", capture_output=True, text=True)
else:
    result = subprocess.run(f"{command}", capture_output=True, text=True)

output = result.stdout.strip()
print(output)