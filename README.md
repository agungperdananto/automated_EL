# automated_EL

### Install python
    https://www.python.org/downloads/
### Install virtualenv
    https://virtualenv.pypa.io/en/latest/installation.html
### Install requirements
    pip install -r requirements.txt
### Setup chromedriver
Windows
    Create directory C:\bin
    Download chromedriver for Windows (https://sites.google.com/a/chromium.org/chromedriver/home) and save to C:\bin
    Add directory to your PATH:
Depending on your Windows version:
    If you're using Windows 8 or 10, press the Windows key, then search for and select System (Control Panel)
    If you're using Windows 7, right click the Computer icon on the desktop and click Properties
    Click Advanced system settings
    Click Environment Variables
    Under System Variables, find the PATH variable, select it, and click Edit. If there is no PATH variable, click New
    Add C:\bin to the end of the variable value, preceeded by a ;. For example, if the value was C:\Windows\System32, change it to C:\Windows\System32;C:\bin
    Click OK
    Restart your command prompt
    Verify setup with chromedriver.exe -v

### Create local_setting
create local_setting.py and fill config like example.settings.py