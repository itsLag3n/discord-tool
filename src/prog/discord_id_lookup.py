from src.config.utils import *
import requests

class user_id_lookup:
    def __init__(self):
        self.user_id = None
        self.data = None
        self.avatar_url = None
        self.banner_url = None
        self.banner_color = None
        self.display_name = None
        self.username = None
        self.discriminator = None
        self.creation_date = None
    
    def get_avatar_url(self):
        data = self.data
        user_id = self.user_id

        avatar_id = data.get('avatar', "Not available")
        if avatar_id == None:
            return "None"
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
        response = requests.get(f"{avatar_url}.gif")
        if response.status_code != 200:
            return f"{avatar_url}.png"
        return f"{avatar_url}.gif"

    def get_banner(self):
        data = self.data
        user_id = self.user_id

        banner_id = data.get('banner', "Not available")
        banner_color = data.get('banner_color', "Not available")
        if banner_id != None:
            banner_url = f"https://cdn.discordapp.com/banners/{user_id}/{banner_id}"
            response = requests.get(f"{banner_url}.gif")
            if response.status_code != 200:
                return f"{banner_url}.png", banner_color
            return f"{banner_url}.gif", banner_color
        return "None", banner_color

    def get_display_name(self):
        data = self.data
        
        display_name = data.get('global_name', "Not available")
        return display_name

    def get_username(self):
        data = self.data
        
        username = data.get('username', "Not available")
        return username

    def get_discriminator(self):
        data = self.data
        
        discriminator = data.get('discriminator', "?")
        return discriminator
    
    def get_creation_date(self):
        user_id = self.user_id

        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        return creation_date


    def main(self):
        Clear()
        Title("User ID Lookup")
        Menu()
        self.user_id = Ask("\nUser ID")
        Title(f"User ID Lookup - {self.user_id}")
        url = f"https://dashboard.botghost.com/api/public/tools/user_lookup/{self.user_id}"
        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.json()

            self.avatar_url = self.get_avatar_url()
            self.banner_url, self.banner_color = self.get_banner()
            self.display_name = self.get_display_name()
            self.username = self.get_username()
            self.discriminator = self.get_discriminator()
            self.creation_date = self.get_creation_date()
            
            Clear()
            Menu()
            input(f"""
{co}Avatar url        :{RESET} {self.avatar_url}
{co}Banner            :{RESET} {self.banner_url}
{co}Banner Color      :{RESET} {self.banner_color}
{co}User Id           :{RESET} {self.user_id}
{co}Display Name      :{RESET} {self.display_name}
{co}Username          :{RESET} {self.username}#{self.discriminator}
{co}Created at        :{RESET} {self.creation_date}
""")
        else:
            Log(R, "!", "Error while getting user information", wp=True)
            time.sleep(1.5)