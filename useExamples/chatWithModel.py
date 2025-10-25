def chatLoop(page, lin=False):
    def normalChat(page):
        import os
        from initMods.GetLastResponse import GetLastResponse
        from Mods.Message import SendMessage
        from colorama import init
        from termcolor import colored
        from art import art

        # def lineDrawer(char="-"):
        #     terminal_size = os.get_terminal_size()
        #     print(char * terminal_size.columns)

        print(art)
        while True:
            print(colored("Prompt", "yellow", "on_black"))
            prompt = input()
            SendMessage(page, prompt)

            print()
            # lineDrawer()
            print()

            # Get the response (function now waits for completion)
            response = GetLastResponse(page)
            print(colored("DeepSeek", "blue", "on_black"))
            print(f"\033[1m{response}\033[0m")

            print()

    def linuxChat(page, su=False):
        import os
        import subprocess
        import platform
        import re
        from initMods.GetLastResponse import GetLastResponse
        from Mods.Message import SendMessage
        from colorama import init
        from termcolor import colored
        from art import art
        
        # Initialize colorama
        init()
        
        print(art)
        print(colored("Linux Terminal Mode Activated", "green", "on_black"))
        
        # Detect OS and setup terminal environment
        # we detect the os using this, platform, inside system, find the lower(nae of the os)
        current_os = platform.system().lower()
        # do we have native linux temrina? None is just for declaring a empty varable
        terminal_cmd = None

        # if our os (platform.system().lower()) is linux, 
        if current_os == "linux":
            # Running on actual Linux using bash(can be changed to zsh or oh my zsh but ai dosent care about these
            terminal_cmd = ["bash", "-c"]
            #tell the user that we detected its linux (lin kos XD)
            print(colored("Detected Linux OS - Using native terminal", "green"))
            #if the os in NOT linux, and is the nasty baddie windows
        elif current_os == "windows":
            # Check if WSL is available, kiddos linux (i use it myself, sadly)
            try:
                # Try to run wsl command to check if it's installed or not
                result = subprocess.run(["wsl", "--list", "--quiet"], capture_output=True, text=True, timeout=5)
                # code 0 means YES, the output is NOT an error, meaning wsl is there, 
                if result.returncode == 0:
                    # so meaning that we have a bash, INSIDE out wsl
                    terminal_cmd = ["wsl", "bash", "-c"]
                    # and we will tell the user that we know your a idiot(windows user) and we'll use wsl for your little brain
                    print(colored("Detected Windows OS - Using WSL", "green"))
                else:
                    # if not wsl, pisho pisho the user out of the code, my golden beautiful code dosent whant a kid, using windows, touch it
                    print(colored("WSL not found! Please install WSL to use Linux terminal mode.", "red"))
                    return
            # if it took a lot of time (subprocess.TimeExpired is always 30 sec's)
            except (subprocess.TimeoutExpired, FileNotFoundError):
                # pisho pisho the user out again, telling it that they dont have linux or wsl
                print(colored("WSL not found! Please install WSL to use Linux terminal mode.", "red"))
                return

        else:
            # else, show the user that were CONFUSED AS HELL, not using windows? also not user linux? dude im too lazy to go to shower, and your telling me to learn a new OS? which almost dosent exict?
            print(colored(f"Unsupported OS: {current_os}. Linux terminal mode not available.", "red"))
            return
        
        #if after all those checkings, the dude passed, we ensure terminal is connected and his a LEGEND
        print(colored("Terminal ready! AI will systematically complete tasks.", "yellow"))
        print(colored("AI will check prerequisites and execute step-by-step.", "cyan"))
        print(colored("AI will use cowsay for friendly communication and results!", "magenta"))
        print()
        
        def get_sudo_password():
            """Securely get sudo password from user"""
            import getpass
            print(colored("This command requires sudo access. Please enter your password:", "yellow"))
            password = getpass.getpass("Password: ")
            return password
        
        def execute_command(command):
            """Execute a command and return the result with captured output"""
            try:
                print(colored(f"Executing: {command}", "cyan"))
                print(colored(f"Current OS: {current_os}", "blue"))
                print(colored("=" * 60, "blue"))
                
                # Check if command requires sudo access
                requires_sudo = command.strip().startswith("sudo ")
                
                if requires_sudo:
                    print(colored("⚠ Command requires sudo access", "yellow"))
                    password = get_sudo_password()
                    
                    # Execute the command with sudo password
                    if current_os == "linux":
                        print(colored("Using native Linux shell with sudo", "blue"))
                        process = subprocess.Popen(
                            command.strip(),
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        stdout, stderr = process.communicate(input=password + "\n", timeout=30)
                        result = subprocess.CompletedProcess(
                            args=command.strip(),
                            returncode=process.returncode,
                            stdout=stdout,
                            stderr=stderr
                        )
                    else:  # Windows with WSL
                        print(colored("Using WSL with sudo", "blue"))
                        process = subprocess.Popen(
                            ["wsl", "bash", "-c", command.strip()],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        stdout, stderr = process.communicate(input=password + "\n", timeout=30)
                        result = subprocess.CompletedProcess(
                            args=["wsl", "bash", "-c", command.strip()],
                            returncode=process.returncode,
                            stdout=stdout,
                            stderr=stderr
                        )
                else:
                    # Execute the command without sudo
                    if current_os == "linux":
                        print(colored("Using native Linux shell", "blue"))
                        result = subprocess.run(command.strip(), 
                                              shell=True, 
                                              text=True, 
                                              capture_output=True,
                                              timeout=30)
                    else:  # Windows with WSL
                        print(colored("Using WSL", "blue"))
                        result = subprocess.run(["wsl", "bash", "-c", command.strip()], 
                                              text=True, 
                                              capture_output=True,
                                              timeout=30)
                
                # Display the actual output to user
                if result.stdout:
                    print(colored("STDOUT:", "green"))
                    print(result.stdout)
                if result.stderr:
                    print(colored("STDERR:", "red"))
                    print(result.stderr)
                
                print(colored("=" * 60, "blue"))
                print(colored(f"Command completed with exit code: {result.returncode}", "blue"))
                
                # Return result with captured output for AI
                return result
                        
            except subprocess.TimeoutExpired:
                print(colored("Command timed out after 30 seconds", "red"))
                return None
            except Exception as e:
                print(colored(f"Error executing command: {str(e)}", "red"))
                return None
        
        def send_systematic_prompt(task):
            """Send a systematic prompt for thorough task completion"""
            systematic_prompt = f"""
SYSTEMATIC TASK EXECUTION MODE:
Task: {task}

You must systematically complete this task by:
1. Analyzing ALL prerequisites needed
2. Checking each prerequisite step by step
3. Installing/configuring missing dependencies
4. Executing the main task
5. Verifying completion
but remember, these can change, based on user task, and the way user speaks, you can skip parts, in the process if you found out that the skpped part is important?
you can always do it again

For each step, you must:
- Check if prerequisite exists (use appropriate commands)
- If missing, install/configure it
- Verify installation success
- Move to next step
- Continue until main task is complete

CRITICAL RULES:
- ONLY output Linux commands, NO explanations or text
- ONE command per response
- Use commands: ALL commands that are:
                        - single line commands, meaning they dont OPEN a terminal-gui environment
                        - needed, to do your stuuf, and acomplish your goal
- Use appropriate package managers: 
                        - officials: any official that matches the os, apt pacman etc...
                        - officials: any official that matches the app or action needed, pip, npm, python -m etc...
- Always verify success before proceeding
- When task is COMPLETELY DONE, output exactly: "--PK--PK--PK--" because if the text is smaller that 3 characters, the temrinal wont run it

SUDO PASSWORD HANDLING:
- Commands requiring sudo access (starting with "sudo ") will automatically prompt for password
- The application will securely ask for your password when needed
- You can use sudo commands freely - the password will be handled automatically
- Examples: sudo apt install, sudo snap install, sudo systemctl, etc.

IMPORTANT: Commands will execute in real-time terminal. You can see the output directly.
Use the terminal output to make informed decisions about the next step. also messages that are smaller than 5 characters wont get runned in the terminal, IF your command is small, like pwd, ls, or ANY OTHER COMMAND THAT IS SMALLER THAN 5 CHARACTERS, if a command is smaller than 5 characters, add a comment in front of it, a comment is a string, that we put in our commands to help the hummand/non machines find out that what this code does, meaning they wont actually DO anything, so, if a command is smaller than 5 characters, we can put a command in front of them, like this ```pwd #this is a comment to make the command bigger than 5 characters``` but if the command is ok, and more than 5 characters, like this ```sudo apt install cowsay``` theres no need to any comments, because our bridge to the terminal automatically finds it out and puts it in the terminal

COWSAY INTERACTION RULES:
- Use cowsay to connect with the user and make interactions more friendly
- When user asks for BOTH action AND results (like "show me what's in this folder" or "tell me about this file"), use cowsay to present the results
- Use cowsay for status updates, confirmations, and friendly communication
- Examples of when to use cowsay:
  * After completing a step: cowsay "Step completed successfully!"
  * When showing results: cowsay "Here's what I found in the folder"
  * For confirmations: cowsay "Ready to proceed with next step"
  * When user asks questions: cowsay "Let me check that for you"
- Don't overuse cowsay - use it strategically for meaningful interactions
- Available cowsay options: -f (different animals), -e (eyes), -T (tongue)

EXAMPLE for "create games folder and cd into it":
1. mkdir -p ~/games
2. cd ~/games
3. pwd # a command to ensure that commands that are less that 3 cahracters OR equal to 3 characters run
4. cowsay "Games folder created and ready!"
5. --PK--PK--PK--

EXAMPLE for "show me what's in my home directory":
1. ls -la ~
2. cowsay "Here's what's in your home directory!"
3. --PK--PK--PK--

BUT REMEMBER:
    this linux terminal is in your hands, DO NOT LIMIT YOURSELF TO THE THINGS I TOLD YOU IN THIS PROMP, be creative, to accomplish the task

AND:
    if the user is not asking you to DO anything, you can directly speak to user using cowsay, which will be always installed

Start with the FIRST command for: {task}
"""
            SendMessage(page, systematic_prompt)
        
        # Test command execution
        print(colored("Testing command execution...", "yellow"))
        test_result = execute_command("echo 'Terminal test successful'")
        if test_result and test_result.returncode == 0:
            print(colored("✓ Terminal execution working!", "green"))
        else:
            print(colored("✗ Terminal execution failed!", "red"))
        
        # Test cowsay functionality
        print(colored("Testing cowsay functionality...", "yellow"))
        cowsay_result = execute_command("cowsay 'Hello! I'm ready to help you!'")
        if cowsay_result and cowsay_result.returncode == 0:
            print(colored("✓ Cowsay working! AI will use it for friendly communication!", "green"))
        else:
            print(colored("⚠ Cowsay not available, but AI will still work normally", "yellow"))
        print()
        
        # Main task loop
        while True:
            print(colored("Enter your task:", "yellow", "on_black"))
            task = input()
            
            if not task.strip():
                continue
                
            print(colored(f"Starting systematic execution of: {task}", "green"))
            print(colored("AI will now check prerequisites and execute step-by-step...", "cyan"))
            print()
            
            # Send initial systematic prompt
            send_systematic_prompt(task)
            
            # Execute commands until task is complete
            task_complete = False
            command_count = 0
            max_commands = 20  # Safety limit to prevent infinite loops
            
            while not task_complete and command_count < max_commands:
                print()
                print(colored("Waiting for AI response...", "yellow"))
                
                # Get the response
                response = GetLastResponse(page)
                print(colored("DeepSeek", "blue", "on_black"))
                print(f"\033[1m{response}\033[0m")
                
                # Check for completion signal
                if "--PK--PK--PK--" in response.strip():
                    print(colored("✓ TASK COMPLETED SUCCESSFULLY!", "green", "on_black"))
                    task_complete = True
                    break
                
                # Execute the command if it's not the completion signal
                if response.strip() and "--PK--PK--PK--" not in response.strip():
                    print(colored(f"About to execute command: '{response.strip()}'", "magenta"))
                    result = execute_command(response.strip())
                    command_count += 1
                    
                    # Send follow-up prompt for next step
                    if not task_complete:
                        # Prepare command output for AI
                        output_info = ""
                        if result and hasattr(result, 'stdout') and hasattr(result, 'stderr'):
                            output_info = f"""
Command executed: {response.strip()}
Exit code: {result.returncode}
"""
                            if result.stdout:
                                output_info += f"STDOUT:\n{result.stdout}\n"
                            if result.stderr:
                                output_info += f"STDERR:\n{result.stderr}\n"
                        else:
                            output_info = f"Command executed: {response.strip()}\n(No output captured)"
                        
                        follow_up = f"""
{output_info}

Continue with the next step for: {task}
Remember: When completely done, output exactly: "--PK--PK--PK--"

COWSAY REMINDER:
- Use cowsay for friendly communication and status updates
- When showing results or confirming completion, use cowsay
- Examples: cowsay "Step completed!" or cowsay "Here are the results!"
- Use cowsay strategically to connect with the user
"""
                        SendMessage(page, follow_up)
            
            if command_count >= max_commands:
                print(colored("⚠ Maximum command limit reached. Task may be incomplete.", "yellow"))
            
            print()
            print(colored("=" * 50, "blue"))
            print()

    # Route to appropriate chat function
    if lin:
        linuxChat(page)
    else:
        normalChat(page)
