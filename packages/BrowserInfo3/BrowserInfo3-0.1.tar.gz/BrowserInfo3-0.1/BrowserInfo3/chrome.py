from BrowserInfo3.Utilities import Browser
import os
import getpass
class ChromeNotFound(Exception):
    pass
def GetVersion():
    path = r"C:\Users\{}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser())
    if os.path.exists(path):
        with open('{}\\Last Version'.format(path),'r') as file:
            content = file.read()
            if content:
                return content
    else:
        raise ChromeNotFound("Chrome is not installed or you are using an unsupported OS. Use Chrome in Windows.")
class Chrome(Browser):
    def __init__(self):
        super().__init__(
            Name="Google Chrome",

            Version=GetVersion(),

            Path=r'C:\Users\{}\AppData\Local\Google\Chrome'.format(getpass.getuser())

        )