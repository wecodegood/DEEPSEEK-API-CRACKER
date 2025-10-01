## DeepSeek Web Automation

This repository contains a small experimental script that automates the DeepSeek chat web interface using Playwright (Python). It opens a real browser, logs in with your credentials, sends prompts from your terminal, and prints the model's response after it finishes rendering on the page.

It is not an official API client, it does not “crack” anything (i just tought its cool to call it a api cracker), but it actually can guarantee limits(because the web version dosent have any). It is a learning/demo project that may break if the website UI changes.

---

## What it does

- Logs into `chat.deepseek.com` using the credentials you provide
- Lets you type prompts in the terminal and submits them to the site
- Waits until the web response appears to be complete, then prints it
- Opens the browser in dark mode for easier viewing by default
- Includes a small helper for running commands in WSL from Windows (optional)
let me remind you that the code is a really simple code to read/understand, you can easily change it to your liking

---

## What it does not do

- It does not handle 2FA, captchas, or all edge cases
but im thinking about a way to fix it, and its under development, well... its going well

---

## Requirements

- Python 3.10+
- Playwright for Python and the Firefox browser binaries installed via Playwright

---

## Install

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install playwright colorama termcolor
python -m playwright install firefox
```

## Configure credentials

The example script currently reads hardcoded placeholders in `creds.py`:

```startLine:endLine:creds.py
1:3:creds.py
email = "your5dad6666@gmail.com"
password = "yasin.11A"
```

Replace these with your own DeepSeek login email and password before running. For better hygiene, consider using environment variables or a local `.env` file and importing them into `creds.py` (not included by default).

Note: Do not commit real credentials to version control.

---

## Run

```bash
python main.py
```

What to expect:
- A Firefox window opens (headless=False in the code)
- The script navigates to `chat.deepseek.com` and attempts to log in
- The terminal will prompt you to type messages; responses will print after they finish rendering

To stop the script, close the browser window or interrupt the process in your terminal.

---

## Project structure (key files)

- `main.py`: Entry point; launches Playwright, logs in, starts the chat loop
- `initMods/Loginer.py`: Simple login steps (fill email/password, click)
- `initMods/GetLastResponse.py`: Polls the DOM to detect when a response is stable/complete
- `useExamples/chatWithModel.py`: Terminal loop for sending prompts and printing responses

---

## Limitations and caveats

- Selectors are minimal and may fail if the site changes
- 2FA, captcha, or additional login challenges are not handled

---

## Contributing

Issues and small improvements are welcome. Please keep changes honest and aligned with the scope: a straightforward, educational web‑automation example.

---

## License

No license file is provided at this time. If you intend to reuse this code, please open an issue to discuss appropriate licensing.

---

## خودکارسازی وب دیپ‌سیک (نسخه فارسی)

این مخزن شامل یک اسکریپت آزمایشی کوچک است که با استفاده از Playwright (پایتون) رابط وب چت DeepSeek را خودکارسازی می‌کند. یک مرورگر واقعی باز می‌شود، با اطلاعات ورود شما وارد می‌شود، پیام‌ها را از ترمینال شما ارسال می‌کند و پس از اتمام نمایش پاسخ در صفحه، خروجی مدل را چاپ می‌کند.

این یک کلاینت رسمی API نیست، چیزی را «هک/کرک» نمی‌کند (فقط اسم جالبی برای پروژه است)، و تضمینی برای دور زدن محدودیت‌ها ارائه نمی‌دهد؛ هرچند در نسخه وب عموماً محدودیت سفت‌وسختی دیده نمی‌شود. این یک پروژه آموزشی/دمویی است و ممکن است با هر تغییر رابط کاربری سایت از کار بیفتد.

---

## چه کارهایی انجام می‌دهد

- با اطلاعات شما به `chat.deepseek.com` وارد می‌شود
- به شما اجازه می‌دهد در ترمینال پیام بنویسید و آن را در سایت ارسال کند
- منتظر می‌ماند تا پاسخ وب کامل شود، سپس آن را چاپ می‌کند
- به‌صورت پیش‌فرض مرورگر را در حالت تیره باز می‌کند
- کد ساده است و می‌توانید آن را به‌دلخواه خود تغییر دهید

---

## چه کارهایی انجام نمی‌دهد

- تمام حالت‌های ورود مانند 2FA و کپچا را مدیریت نمی‌کند
- ممکن است با تغییرات رابط کاربری DeepSeek از کار بیفتد
- یک SDK رسمی یا کلاینت API نیست

در حال بررسی راه‌حل‌هایی برای بهبود ورود و پایداری هستم.

---

## پیش‌نیازها

- Python 3.10+
- Playwright برای پایتون و نصب باینری‌های Firefox از طریق Playwright

---

## نصب

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install playwright colorama termcolor
python -m playwright install firefox
```

---

## تنظیم اطلاعات ورود

اسکریپت نمونه اطلاعات را از فایل `creds.py` می‌خواند:

```startLine:endLine:creds.py
1:3:creds.py
email = "your5dad6666@gmail.com"
password = "yasin.11A"
```

این‌ها را با ایمیل و گذرواژه خود جایگزین کنید. برای امنیت بهتر، می‌توانید از متغیرهای محیطی یا فایل `.env` استفاده کرده و در `creds.py` بخوانید (به‌صورت پیش‌فرض پیاده‌سازی نشده است). توجه کنید اطلاعات واقعی را در گیت کامیت نکنید.

---

## اجرا

```bash
python main.py
```

چه اتفاقی می‌افتد:
- یک پنجره Firefox باز می‌شود (در کد headless=False است)
- اسکریپت به `chat.deepseek.com` می‌رود و تلاش می‌کند وارد شود
- در ترمینال می‌توانید پیام بنویسید؛ پس از کامل شدن پاسخ در وب، در ترمینال چاپ می‌شود

برای توقف، پنجره مرورگر را ببندید یا فرآیند را در ترمینال متوقف کنید.

---

## ساختار پروژه (فایل‌های مهم)

- `main.py`: نقطه شروع؛ Playwright را راه‌اندازی، ورود و حلقه چت را اجرا می‌کند
- `initMods/Loginer.py`: مراحل ساده ورود (پر کردن ایمیل/گذرواژه و کلیک)
- `initMods/GetLastResponse.py`: وضعیت پاسخ را در DOM بررسی می‌کند تا کامل شدن را تشخیص دهد
- `useExamples/chatWithModel.py`: حلقه ترمینالی برای ارسال پیام و چاپ پاسخ

---

## محدودیت‌ها و نکات

- انتخابگرهای DOM ساده هستند و ممکن است با تغییر سایت از کار بیفتند
- چالش‌های امنیتی مانند 2FA و کپچا پوشش داده نشده‌اند
- این یک نمونه آموزشی است؛ با مسئولیت خود استفاده کنید

---

## مشارکت

پیشنهادها و بهبودهای کوچک خوش‌آمد هستند. لطفاً راست‌گو و در چارچوب هدف آموزشی پروژه بمانید.

---

## مجوز

در حال حاضر فایل مجوزی ارائه نشده است. اگر قصد استفاده مجدد دارید، لطفاً یک Issue باز کنید تا درباره مجوز مناسب گفتگو شود.
