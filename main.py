
# librarys:
import time


#framework
from playwright.sync_api import sync_playwright

# moduals:
    #main moduals:
from initMods.Loginer import LoginToDeepSeek
from initMods.GetLastResponse import GetLastResponse
from useExamples.chatWithModel import chatLoop

#moduals:
    #init prompt moduals:
from initMods.Message import InitChatMessage
from initMods.Message import InitLinuxMessage

# moduals: 
    #creds moduals:
from creds import *


#moduals:
    # simple moduals:
from Mods.Message import SendMessage
from Mods.Clear import clean
# from Mods.RunLinuxCommand import run_linux_cmd


with sync_playwright() as p:

    clean()

    browser = p.firefox.launch(
        headless=True,
        # slow_mo=2000
    )

    # context saves the settings we whant to modify in the prefrencec
    # for example here i did this to make deepseek.com go dark mode because i was getting blind
    context = browser.new_context(
        color_scheme='dark'  # to make it go dark mode
    )
    
    page = context.new_page()



    LoginToDeepSeek(email, password, browser, page) # this is a function from a file named Loginer.py located in initMods folder

    InitChatMessage(browser, page)

    chatLoop(page)
    
        







    time.sleep(10000)

    browser.close()
