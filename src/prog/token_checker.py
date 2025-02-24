from src.config.utils import *
import requests

class token_checker:
    def __init__(self):
        self.token = None

    def check_token(self):
        try:
            url = "https://discord.com/api/v9/users/@me"
            headers = {
                "Authorization": self.token
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False
    
    def main(self):
        Clear()
        Title("Token Checker")
        Menu()
        self.token = Ask("\nToken")
        valid = self.check_token()
        if valid:
            SleepLog(G, "+", "Token is valid", wp=True)
        else:
            SleepLog(R, "-", "Token is invalid", wp=True)