from src.config.utils import *
import base64

class id_to_token:
    def __init__(self):
        self.user_id = None
        self.first_part_token = None
    
    def get_first_part_token(self):
        encodedBytes = base64.b64encode(self.user_id.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        return encodedStr
    
    def main(self):
        Clear()
        Title("ID to Token")
        Menu()
        self.user_id = Ask("\nUser ID")
        Title(f"User ID: {self.user_id}")
        
        self.first_part_token = self.get_first_part_token()
        
        Clear()
        Menu()
        input(f"\n{W}{self.user_id}{co} > First part token:{W} {self.first_part_token}\n")