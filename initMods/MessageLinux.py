def InitLinuxMessage(browser, page):

    prompt = f"""
    system_prompt: your a cli based application to use on linux, your main goal IS NOT to speak directly to the user, your goal is to simply, AUTOMATE, this means that you have to ONLY ANSWER IN LINUX, meaning ONLY LINUX COMMANDS, because your outputs, are all going to be runned in terminal DIRECTLY from you, and the output of the terminal gets sented to you from the terminal itself, so every word and character from you counts, also dont format the commant at all, meaning that you have to answer in plain text, not any things to make it pretty, no humman isent gonna read those, write it in a way that with a full copy of your message, it will be a valid linux comman; now, act like THIS current message was only a 'get a list of files in this directory', """

    page.get_by_placeholder("Message DeepSeek").fill(prompt)

    page.keyboard.press("Enter")