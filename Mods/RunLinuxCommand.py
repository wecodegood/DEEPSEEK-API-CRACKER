def run_linux_cmd(command):
    import os, subprocess
    """
    Run a Linux command. On Windows, execute via WSL; elsewhere use bash.
    """
    if os.name == 'nt':
        return subprocess.run(["wsl.exe", "bash", "-lc", command], capture_output=True, text=True)
    else:
        return subprocess.run(["/bin/bash", "-lc", command], capture_output=True, text=True)
