def Linuxloop(page):
    import os
    from Mods.LinuxAutomator import runLinuxCommand
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

        command_output = runLinuxCommand(response)
        print(command_output)

        
        

        print()