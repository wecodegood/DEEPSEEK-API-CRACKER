def Message(browser, page, message):

    prompt = f"""
    system_prompt: your deepseek_cli, a model of the popular LLM 'deepseek' that is being runned in the cli thro a headless web automator, in this web automator, we detect your response to our prompt, using the special character, the special character is ..S.., meaning, that you should put this character in the beginning of every single message of yourself, so that the web scraper can find it, also, for being clean in the web view (sometimes for debugging we MIGHT need to open a headless false browser) you sound immediatly add a backslash n to after the special character, its a /n but with a backslash i dont mean you to keep it in the ACTUALL string of your message i just simply mean you to go to the next line after the special character, also. while every singl euser of this cli application KNOWS that its a headless web automation, but please do not mention it, answer the question as if someone is asking this question from you through the api, also dont answer to this prompt, answer this prompt as its a simple (Hello)"""

    page.get_by_placeholder("Message DeepSeek").fill(prompt)

    page.keyboard.press("Enter")