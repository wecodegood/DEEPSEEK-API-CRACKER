def LoginToDeepSeek(evar, pvar, browser, page, url="https://chat.deepseek.com"):
    page.goto("https://chat.deepseek.com/a/chat/s/be63d0a8-c16e-4ac4-99d0-d816688e9c8e")
    page.get_by_placeholder("Phone number / email address").fill(evar)
    page.get_by_placeholder("Password").fill(pvar)
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Enter")
    # page.get_by_role("button").nth(0).click()