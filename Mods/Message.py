def SendMessage(browser, page, message):

    
    page.get_by_placeholder("Message DeepSeek").fill(message)

    page.keyboard.press("Enter")
