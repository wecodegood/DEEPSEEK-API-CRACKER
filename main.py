from email import message
import time
from playwright.sync_api import sync_playwright
from initMods.Loginer import LoginToDeepSeek
from initMods.Message import InitMessage
from initMods.GetLastResponse import GetLastResponse
from initMods.MessageLinux import InitLinuxMessage

from creds import *

from Mods.Message import Message
from useExamples.chatWithModel import ChatExample
import os

def clean():
    """
    this function runs the optimized command to clean the terminal
    """
    os.system('cls') if os.name == 'nt' else os.system('clean')



with sync_playwright() as p:

    clean()

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
    # InitMessage(browser, page) # this is a function also from a file named emssage.py located in initMods folder

    InitLinuxMessage(browser, page)

    # GetLastResponse(page)

    ChatExample(page)

    time.sleep(15)





    time.sleep(10000)

    browser.close()
