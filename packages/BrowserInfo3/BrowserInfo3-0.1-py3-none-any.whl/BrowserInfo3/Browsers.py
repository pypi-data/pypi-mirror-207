from BrowserInfo3.Utilities import Browser
from BrowserInfo3.chrome import GetVersion as __chr
from BrowserInfo3.edge import Edge as __ecl
from BrowserInfo3.chrome import ChromeNotFound
from BrowserInfo3.chrome import Chrome as __chrm
from BrowserInfo3.edge import GetVersion as __edg
from BrowserInfo3.edge import EdgeNotFound
def GetBrowser() -> Browser:
    try:
        ver = __chr()
        if ver:
            return __chrm()
    except ChromeNotFound:
        try:
            ver = __edg()
            if ver:
                return __ecl()
        except EdgeNotFound:
            return