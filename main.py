#framework
from playwright.sync_api import sync_playwright

# moduals:
    #main moduals:
from initMods.Loginer import LoginToDeepSeek
from initMods.GetLastResponse import GetLastResponse
from useExamples.chatWithModel import chatLoop
from useExamples.linux import Linuxloop

#moduals:
    #init prompt moduals:
from initMods.initMessages import InitChatMessage
from initMods.initMessages import InitLinuxMessage

# moduals: 
    #creds moduals:
from creds import *


#moduals:
    # simple moduals:
from Mods.Message import SendMessage
from Mods.Clear import clean
# from Mods.RunLinuxCommand import run_linux_cmd
#moduals:
    #librarys
import time


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




    clean()

    LoginToDeepSeek(email, password, browser, page) # this is a function from a file named Loginer.py located in initMods folder

    InitLinuxMessage(browser, page)

    Linuxloop(page)



    time.sleep(10000)

    browser.close()
