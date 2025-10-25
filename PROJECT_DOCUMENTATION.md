# DeepSeek API Cracker - Project Documentation

## Overview

**DeepSeek API Cracker** is a Python-based web automation tool that interfaces with the DeepSeek chat web interface using Playwright. Despite its name suggesting "API cracking," this is actually a legitimate web automation project that provides a command-line interface to interact with DeepSeek's chat service through browser automation.

## Project Purpose

This project serves as an educational demonstration of web automation techniques, providing users with:
- A terminal-based interface to interact with DeepSeek's chat service
- Automated login and session management
- Real-time response monitoring and display
- Special Linux terminal mode for systematic task execution
- Cross-platform support (Windows with WSL, native Linux)

## Key Features

### 1. Web Automation Core
- **Browser Control**: Uses Playwright with Firefox browser
- **Login Automation**: Automated login to chat.deepseek.com
- **Response Monitoring**: Intelligent polling system to detect when responses are complete

### 2. Dual Chat Modes
- **Normal Chat Mode**: Standard conversational interface
- **Linux Terminal Mode**: Systematic task execution with real-time command execution

### 3. Cross-Platform Support
- **Windows**: Uses WSL (Windows Subsystem for Linux) for terminal commands
- **Linux**: Native terminal support
- **Automatic Detection**: Detects OS and configures appropriate terminal environment

## Technical Architecture

### Core Components

#### 1. Main Entry Point (`main.py`)
```python
# Framework initialization
- Playwright browser setup
- Login automation
- Enter a Chat loop, linux, or normal chatloop
```

#### 2. Authentication Module (`initMods/Loginer.py`)
```python
def LoginToDeepSeek(evar, pvar, browser, page, url="https://chat.deepseek.com"):
    """This function takes a email and a password, fills the email/password feild in the form, and press the login button to Log into deepseek accoung"""
    # Automated login process
    # Email/password form filling
    # Tab navigation and Enter key submission -- needs some improvements, but it works for now
```

#### 3. Response Monitoring (`initMods/GetLastResponse.py`)
```python
def GetLastResponse(page, max_wait_ms=60000, stable_checks_required=5):
    """this function, monitors the deepseek's webpage animation, and makes sure the animation is done, Then, it returns the full message text, and it in a varable"""
    # Intelligent response detection
    # DOM polling with stability checks
    # Timeout handling
    # Real-time response monitoring
```

#### 4. Message Handling (`Mods/Message.py`)
```python
def SendMessage(page, message):
    """fills the message textBox and sents the message"""
    # Message input automation
    # Enter key submission

def SendGetMessage(page, message):
    """fills the message textBox and sends the message, and gets the answer and returns it"""
    # Combined send and receive functionality
```

#### 5. Chat Interface (`useExamples/chatWithModel.py`)
- **Normal Chat**: Standard conversational interface
- **Linux Terminal Mode**: Advanced systematic task execution

### Linux Terminal Mode Features

The Linux Terminal Mode provides sophisticated automation capabilities:

#### Systematic Task Execution
- **Prerequisite Analysis**: Automatically checks required dependencies
- **Step-by-Step Execution**: Breaks complex tasks into manageable steps
- **Real-time Feedback**: Shows command output and execution status
- **Error Handling**: Manages command failures and timeouts
- **Completion Detection**: Uses special markers to signal task completion -- needs improvements and a smarter way, this one's goofy

#### Command Execution Features
- **OS Detection**: Automatically detects Windows/Linux environments
- **WSL Integration**: Seamless Windows Subsystem for Linux support
- **Package Manager Support**: apt, snap, pip, npm, curl, wget, git -- overhally tried to NOT limit it to a certain os
- **Safety Limits**: Maximum command execution limits to prevent infinite loops -- can be easily turned off to do long term tasks(havent tested it much)
- **Cowsay Integration**: Friendly communication using cowsay utility -- just a little funny way to make the ai speak directly to the user

#### Example Workflow
```
Task: "Install Visual Studio Code"
1. Check internet connectivity: ping -c 1 google.com
2. Check snapd availability: snap list
3. Install snapd if missing: sudo apt install snapd
4. Verify snapd installation: snap list
5. Install VS Code: sudo snap install code --classic
6. Verify installation: which code
7. Signal completion: --PK--PK--PK-- <-- this is the part that i think needs improvement, makes the app feel cheap, because its actually cheap
```

## File Structure

```
deepseek-api-cracker/
├── main.py                    # Main entry point
├── creds.py                   # Credentials configuration <-- needs improvement
├── art.py                     # ASCII art for terminal display <-- fun
├── requirements.txt           # Python dependencies
├── README.md                  # Project readme <-- this current file
├── initMods/                  # Initialization modules
│   ├── Loginer.py            # Login automation <-- when called, and passed the arguments, logs into the account
│   ├── GetLastResponse.py    # Response monitoring <-- when called, and passed the arguments, gets the last response coming from deepseek
│   └── initMessages.py      # Initial message setup <-- gives deepseek a simple prompt to make it know that its a cli tool 
├── Mods/                      # Core modules
│   └── Message.py            # Message handling <-- got used in a few other files too, like initMessage.py
└── useExamples/              # Usage examples
    └── chatWithModel.py      # Chat interface implementation <-- stored both linux automation and simple chat in here, because im lazy seperating them
```

## Dependencies

### Required Packages
- **playwright**: Web automation framework
- **playwright --firefox**: firefox browser for playwright
- **colorama**: Cross-platform colored terminal text
- **termcolor**: Terminal text coloring
- **time**: Built-in Python timing utilities

### Required Packages install
- **playwright**: pip install playwright
- **playwright --firefox**: python -m playwright install firefox
- **colorama**: pip install colorama
- **termcolor**: pip install termcolor
- **time**: just be happy, 

### System Requirements
- **Python 3.10+**: Required Python version
- **Firefox Browser**: Installed via Playwright
- **WSL** (Windows only): For Linux terminal mode on Windows

## Installation and Setup

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.\.venv\Scripts\activate

# Install dependencies
pip install playwright colorama termcolor

# Install Firefox browser
python -m playwright install firefox
```

### 2. Credentials Configuration
Edit `creds.py` with your DeepSeek credentials:
```python
email = "your_email@example.com"
password = "your_password"
```

**Security Note**: Never commit real credentials to version control.

### 3. Running the Application
```bash
python main.py
```

## Usage Modes

### Normal Chat Mode
- Standard conversational interface
- Type prompts in terminal
- Receive responses from DeepSeek
- Colored output for better readability

### Linux Terminal Mode
- Systematic task execution
- Real-time command execution
- Prerequisite checking and installation
- Friendly cowsay communication
- Cross-platform terminal support

## Configuration Options

### Browser Settings
- **Headless Mode**: Currently disabled for visual feedback
- **Slow Motion**: Available for debugging (commented out)

### Response Monitoring
- **Max Wait Time**: 60 seconds default
- **Stability Checks**: 5 consecutive stable readings required
- **Poll Interval**: 0.2 seconds
- **Minimum Start Characters**: 5 characters

### Terminal Mode Settings
- **Command Timeout**: 30 seconds
- **Maximum Commands**: 20 commands per task
- **Minimum Command Length**: 5 characters (with comment workaround)

## Security Considerations

### Credential Management
- Credentials stored in plain text (consider environment variables)
- No encryption or secure storage implemented
- Users responsible for credential security

### Web Automation Risks
- Relies on DOM selectors that may change
- No handling of 2FA or captcha challenges
- May break with website UI updates

## Limitations and Known Issues

### Technical Limitations
1. **DOM Dependency**: Relies on specific CSS selectors that may change
2. **Authentication**: No support for 2FA or additional security measures
3. **Error Handling**: Limited error recovery mechanisms
4. **Browser Compatibility**: Only supports Firefox via Playwright

### Functional Limitations
1. **Rate Limiting**: Subject to DeepSeek's web interface limitations
2. **Session Management**: No persistent session handling
3. **Multi-user**: Single user session only
4. **Offline Mode**: Requires internet connection

## Development and Maintenance

### Code Quality
- Simple, readable code structure
- Modular design for easy modification
- Extensive comments and documentation
- Educational focus for learning web automation

### Future Enhancements
- Enhanced error handling and recovery
- Support for additional authentication methods
- Improved session management
- Better cross-platform compatibility
- Enhanced security features

## Legal and Ethical Considerations

### Terms of Service
- Users must comply with DeepSeek's terms of service
- No guarantee of service availability or stability
- Educational and personal use recommended

### Ethical Usage
- Respects website rate limits and usage policies
- No malicious or harmful automation
- Transparent about automation nature
- Educational and learning purposes

## Troubleshooting

### Common Issues

#### 1. Login Failures
- Verify credentials in `creds.py`
- Check internet connectivity
- Ensure DeepSeek website is accessible

#### 2. Browser Issues
- Reinstall Firefox: `python -m playwright install firefox`
- Check Playwright installation
- Verify browser permissions

#### 3. Terminal Mode Issues
- Install WSL on Windows
- Verify Linux terminal availability
- Check command execution permissions

#### 4. Response Detection Issues
- Website UI may have changed
- Check CSS selectors in `GetLastResponse.py`
- Verify page loading completion

### Debug Mode
Enable slow motion for debugging:
```python
browser = p.firefox.launch(
    headless=False,
    slow_mo=2000  # Uncomment for debugging
)
```

## Contributing

### Development Guidelines
- Keep code simple and educational
- Maintain cross-platform compatibility
- Add comprehensive comments
- Test on multiple operating systems
- Follow existing code style

### Reporting Issues
- Include operating system information
- Provide error messages and logs
- Describe steps to reproduce
- Check for existing issues first

## License and Disclaimer

### License Status
- No formal license provided
- Contact project maintainer for licensing questions
- Educational and personal use recommended

### Disclaimer
- This is not an official DeepSeek API client
- No guarantee of functionality or stability
- Use at your own risk
- Educational purposes only

## Conclusion

The DeepSeek API Cracker project demonstrates practical web automation techniques while providing a useful interface to DeepSeek's chat service. Its modular design, educational focus, and cross-platform support make it an excellent learning resource for web automation and Python development.

The project successfully bridges the gap between web interfaces and command-line tools, offering both casual users and developers a practical solution for interacting with AI services through automation.

---

*This documentation provides a comprehensive overview of the DeepSeek API Cracker project. For specific implementation details, refer to the source code and inline comments.*
