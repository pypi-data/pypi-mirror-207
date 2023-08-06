from BrowserInfo3.Utilities import Browser
import os
import getpass
class EdgeNotFound(Exception):
    pass
def GetVersion():
    path = r"C:\Users\{}\AppData\Local\Microsoft\Edge\User Data".format(getpass.getuser())
    if os.path.exists(path):
        with open('{}\\Last Version'.format(path), 'r') as file:
            content = file.read()
            if content:
                return content
    else:
        raise EdgeNotFound("Edge is not installed or you are using an unsupported OS. Use Edge in Windows.")
class Edge(Browser):
    def __init__(self):
        super().__init__(
            Name="Microsoft Edge",

            Version=GetVersion(),

            Path=r'C:\Users\{}\AppData\Local\Microsoft\Edge'.format(getpass.getuser()

            )
        )