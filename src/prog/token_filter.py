from src.config.utils import *
import requests
from concurrent.futures import ThreadPoolExecutor

class token_filter:
    def __init__(self):
        self.tokens = None
        self.hide_tokens = True
        self.threads_number = 10
        self.ids = []
        self.total_filtred = 0
        self.stayed = 0
        self.double = 0
        self.invalid = 0
        self.failed = 0
        self.filtred_tokens = []
    
    def filter_tokens(self, token):
        self.total_filtred += 1
        try:
            url = "https://discord.com/api/v9/users/@me"
            headers = {
                "Authorization": token
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                id = response.json().get("id")
                if id not in self.ids:
                    self.filtred_tokens.append(token)
                    self.ids.append(id)
                    self.stayed += 1
                    Log(G, "+", f"VALID   : {f"{token[:50]}**********************" if self.hide_tokens else token}")
                else:
                    self.double += 1
                    Log(R, "x", f"DOUBLE  : {f"{token[:50]}**********************" if self.hide_tokens else token}")
            else:
                self.invalid += 1
                Log(R, "x", f"INVALID : {f"{token[:50]}**********************" if self.hide_tokens else token}")
        except Exception as e:
            input(e)
            self.failed += 1
            Log(O, "!", f"FAILED  : {f"{token[:50]}**********************" if self.hide_tokens else token}")

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
            print("")
            with ThreadPoolExecutor(max_workers=self.threads_number) as executor:
                executor.map(self.filter_tokens, self.tokens)
            
            Log(G, "✓", f"{self.total_filtred} filtered | {G}{self.stayed}{W} stayed | {R}{self.double}{W} double | {R}{self.invalid}{W} invalid | {O}{self.failed}{W} failed", wp=True)

            try:
                with open('./entries/tokens.txt', 'w') as f:
                    for token in self.filtred_tokens:
                        f.write(f"{token}\n")
                Log(G, "✓", "Filtered tokens saved in entries/tokens.txt")
            except:
                Log(R, "x", "Failed to save filtered tokens in entries/tokens.txt")
            input()


        except FileNotFoundError:
            os.makedirs(os.path.dirname('./entries'), exist_ok=True)
            with open('./entries/tokens.txt', 'w', encoding='utf-8') as f:
                f.write('')
            
            SleepLog(R, "x", "No tokens found in entries/tokens.txt", wp=True, timee=3)