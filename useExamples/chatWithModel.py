def chatLoop(page):
    from initMods.GetLastResponse import GetLastResponse
    from colorama import init
    from termcolor import colored
    while True:
        print(colored("print", "yellow", "on_black"))
        prompt = input()
        page.get_by_placeholder("Message DeepSeek").fill(prompt)
        page.keyboard.press("Enter")

        print()
        
        # Get the response (function now waits for completion)
        response = GetLastResponse(page)
        print(f"DeepSeek: {response}")
        print()