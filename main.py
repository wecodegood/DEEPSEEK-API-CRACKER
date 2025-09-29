from cmd import PROMPT
import time
from playwright.sync_api import sync_playwright
from initMods.Loginer import LoginToDeepSeek
from initMods.Message import InitMessage



email = "your5dad6666@gmail.com"
password = "yasin.11A"

with sync_playwright() as p:
    browser = p.firefox.launch(
        headless=False,
        # slow_mo=2000
    )

    # context saves the settings we whant to modify in the prefrencec
    # for example here i did this to make deepseek.com go dark mode because i was getting blind
    context = browser.new_context(
        color_scheme='dark'  # to make it go dark mode
    )
    
    page = context.new_page()





    LoginToDeepSeek(email, password, browser, page) # this is a function from a file named Loginer.py located in initMods folder
    InitMessage(browser, page)





    while True:
        prompt = input("prompt:")
        page.get_by_placeholder("Message DeepSeek").fill(prompt)
        page.keyboard.press("Enter")


    time.sleep(10000)

    browser.close()