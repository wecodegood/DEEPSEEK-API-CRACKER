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

    def linuxChat(page):
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
        current_os = platform.system().lower()
        terminal_cmd = None
        
        if current_os == "linux":
            # Running on actual Linux
            terminal_cmd = ["bash", "-c"]
            print(colored("Detected Linux OS - Using native terminal", "green"))
        elif current_os == "windows":
            # Check if WSL is available
            try:
                # Try to run wsl command to check if it's installed
                result = subprocess.run(["wsl", "--list", "--quiet"], capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    terminal_cmd = ["wsl", "bash", "-c"]
                    print(colored("Detected Windows OS - Using WSL", "green"))
                else:
                    print(colored("WSL not found! Please install WSL to use Linux terminal mode.", "red"))
                    return
            except (subprocess.TimeoutExpired, FileNotFoundError):
                print(colored("WSL not found! Please install WSL to use Linux terminal mode.", "red"))
                return
        else:
            print(colored(f"Unsupported OS: {current_os}. Linux terminal mode not available.", "red"))
            return
        
        print(colored("Terminal ready! AI will systematically complete tasks.", "yellow"))
        print(colored("AI will check prerequisites and execute step-by-step.", "cyan"))
        print()
        
        def execute_command(command):
            """Execute a command and return the result"""
            try:
                print(colored(f"Executing: {command}", "cyan"))
                print(colored(f"Current OS: {current_os}", "blue"))
                print(colored("=" * 60, "blue"))
                
                # Execute the command with real-time output
                if current_os == "linux":
                    print(colored("Using native Linux shell", "blue"))
                    result = subprocess.run(command.strip(), 
                                          shell=True, 
                                          text=True, 
                                          timeout=30)
                else:  # Windows with WSL
                    print(colored("Using WSL", "blue"))
                    result = subprocess.run(["wsl", "bash", "-c", command.strip()], 
                                          text=True, 
                                          timeout=30)
                
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

IMPORTANT: Commands will execute in real-time terminal. You can see the output directly.
Use the terminal output to make informed decisions about the next step.

EXAMPLE for "create games folder and cd into it":
1. mkdir -p ~/games
2. cd ~/games
3. pwd # a command to ensure that commands that are less that 3 cahracters OR equal to 3 characters run
4. --PK--PK--PK--

BUT REMEMBER:
    this linux terminal is in your hands, DO NOT LIMIT YOURSELF TO THE THINGS I TOLD YOU IN THIS PROMP, be creative, to accomplish the task

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
                        follow_up = f"""
Previous command executed: {response.strip()}

Continue with the next step for: {task}
Remember: When completely done, output exactly: "--PK--PK--PK--"
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