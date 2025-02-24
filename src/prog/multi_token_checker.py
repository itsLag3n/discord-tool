from src.config.utils import *
import os
import requests
from concurrent.futures import ThreadPoolExecutor

class multi_token_checker:
    def __init__(self):
        self.tokens = None
        self.hide_tokens = True
        self.total_checked = 0
        self.valid = 0
        self.invalid = 0
        self.failed = 0
        self.threads_number = 10
    
    def check_tokens(self, token):
        self.total_checked += 1
        try:
            url = "https://discord.com/api/v9/users/@me"
            headers = {
                "Authorization": token
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.valid += 1
                Log(G, "+", f"VALID: {f"{token[:50]}**********************" if self.hide_tokens else token}")
            else:
                self.invalid += 1
                Log(R, "x", f"INVALID: {f"{token[:50]}**********************" if self.hide_tokens else token}")
        except:
            self.failed += 1
            Log(O, "!", f"FAILED: {f"{token[:50]}**********************" if self.hide_tokens else token}")

    def main(self):
        try:
            with open('./entries/tokens.txt', 'r') as f:
                self.tokens = f.read().splitlines()
            if not self.tokens:
                SleepLog(R, "x", "No tokens found in entries/tokens.txt", wp=True, timee=3)
                return
            
            hide = Ask("Hide tokens (y/n)")
            if hide.lower() in ['n', 'no', 'non', 'false']:
                self.hide_tokens = False
            custom_thread_number = Ask("Custom thread number (y/n)").lower() in ["y", "yes", "o", "oui", "true"]
            if custom_thread_number:
                self.threads_number = Ask("Threads")
                try: self.threads_number = int(self.threads_number)
                except ValueError:
                    SleepLog(R, "x", "Invalid number", wp=True)
                    return
            Clear()
            Menu()
            print("\n")
            with ThreadPoolExecutor(max_workers=self.threads_number) as executor:
                executor.map(self.check_tokens, self.tokens)
            
            Log(G, "✓", f"{self.total_checked} checked | {G}{self.valid}{W} valid | {R}{self.invalid}{W} invalid | {O}{self.failed}{W} failed", wp=True)
            input()
        except FileNotFoundError:
            os.makedirs(os.path.dirname('./entries'), exist_ok=True)
            with open('./entries/tokens.txt', 'w', encoding='utf-8') as f:
                f.write('')
            
            SleepLog(R, "x", "No tokens found in entries/tokens.txt", wp=True, timee=3)