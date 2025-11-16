## DeepSeek Web Cracker

This repository contains a small experimental script that automates the DeepSeek chat web interface using python, and the framework of Playwright. It opens a real browser(headless or not), logs in with your credentials, sends prompts from your terminal, and prints the model's response after it finishes rendering on the page, and then you can do oprations on that prompt

it is not a API, but it MIGHT be able to act as one, but mostly i would not recommend it as an API, i try to use it for doing system level opration's with a online LLM, IT IS a good option to use a simple API but its paid, and we don't like to pay money :)

---

#### What it does

## Normal chat mode 
- Logs into `chat.deepseek.com` using the credentials you provide
- Lets you type prompts in the terminal and submits them to the site
- Waits until the web response appears to be complete, then prints it

## Linux automation mode 
- Logs into `chat.deepseek.com` using the credentials you provide
- Asks a task from you, from the terminal input 
- goes into a loop of sending Linux commands from Deepseek to terminal 
- gets the Linux command from Deepseek and runs it into the terminal 
- sends the output of the command back to DeepSeek
- this loop runs over and over again UNTIL the task is done, and then DeepSeek says --PK--PK--PK--
- The program gets the string, --PK--PK--PK-- and stops the loop, and asks for the next task 

---


## What it does not do

- It does not handle 2FA,
- It does not handle captchas,

---

## Requirements

- Python 3.10+
- Playwright for Python
- and Firefox browser binaries for Playwright


---

## Install

```bash
python -m venv .venv # <-- make a python virtual environment

.\.venv\Scripts\activate # <-- activate the virtual environment

pip install playwright colorama termcolor # <-- install all the libs (you can do pip install -r requirements.txt)

python -m playwright install firefox # <-- using playwright to install firefox binaries
```


## Configure credentials

The example script currently reads hardcoded placeholders in `creds.py`:

```startLine:endLine:creds.py
1:3:creds.py
email = "YOUR EMAIL"
password = "YOUR PASSWORD"
```

Replace these with your own DeepSeek login email and password before running.

---

## Run

```bash
python main.py
```

---

## Project structure (key files)

- `main.py`: Entry point; launches Playwright, logs in, starts the chat loop
- `initMods/Loginer.py`: Simple login steps (fill email/password, click)
- `initMods/GetLastResponse.py`: Polls the DOM to detect when a response is stable/complete
- `useExamples/chatWithModel.py`: Terminal loop for sending prompts and printing responses

---

## License

No license file is provided at this time. If you intend to reuse this code, please open an issue to discuss appropriate licensing.
