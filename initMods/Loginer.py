def LoginToDeepSeek(evar, pvar, browser, page):
    page.goto("https://chat.deepseek.com")
    page.get_by_placeholder("Phone number / email address").fill(evar)
    page.get_by_placeholder("Password").fill(pvar)
    page.keyboard.press("Enter")
    page.get_by_role("button").nth(0).click()