from src.config.utils import *
import requests

class token_lookup:
    def __init__(self):
        self.token = None
        self.data = None
        self.user_id = None
        self.display_name = None
        self.username = None
        self.discriminator = None
        self.avatar_url = None
        self.banner_url = None
        self.banner_color = None
        self.mfa_enabled = None
        self.lang = None
        self.premium_type = None
        self.email = None
        self.phone = None
        self.verified = None
        self.nsfw_allowed = None
        self.bio = None
        self.creation_date = None
        self.co = get_co()


    def get_user_id(self):
        return self.data.get('id', "Not available")
    
    
    def get_display_name(self):
        return self.data.get('global_name', "Not available")
    
    def get_username(self):
        return self.data.get('username', "Not available")
    
    def get_discriminator(self):
        return self.data.get('discriminator', "?")
    
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
    
    def get_banner_url(self):
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
    
    def get_mfa_enabled(self):
        return self.data.get('mfa_enabled', "Not available")
    
    def get_lang(self):
        return self.data.get('locale', "Not available")
    
    def get_premium_type(self):
        premium_type = self.data.get('premium_type', "Not available")

        if premium_type == 0:
            return "None"
        elif premium_type == 1:
            return "Nitro Classic"
        elif premium_type == 2:
            return "Nitro"
        else:
            return "Not available"

    def get_email(self):
        return self.data.get('email', "Not available")
    
    def get_phone(self):
        return self.data.get('phone', "Not available")
    
    def get_verified(self):
        verified = self.data.get('verified', "Not available")
        if verified:
            return "Yes"
        else:
            return "No"
        
    def get_nsfw_allowed(self):
        nsfw_allowed = self.data.get('nsfw_allowed', "Not available")
        if nsfw_allowed:
            return "Yes"
        else:
            return "No"
        
    def get_bio(self):
        bio = self.data.get('bio', "Not available")
        if not bio:
            return "None"
        return "\n" + bio
    
    def get_creation_date(self):
        user_id = self.user_id

        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        return creation_date


    def main(self):
        Clear()
        Title("Token Lookup")
        Menu()
        self.token = Ask("\nToken")
        Title(f"Token Lookup - {self.token[:16]}***")
        url = "https://discord.com/api/v9/users/@me"
        headers = { "Authorization": self.token }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            self.data = response.json()

            self.user_id = self.get_user_id()
            self.display_name = self.get_display_name()
            self.username = self.get_username()
            self.discriminator = self.get_discriminator()
            self.avatar_url = self.get_avatar_url()
            self.banner_url, self.banner_color = self.get_banner_url()
            self.mfa_enabled = self.get_mfa_enabled()
            self.lang = self.get_lang()
            self.premium_type = self.get_premium_type()
            self.email = self.get_email()
            self.phone = self.get_phone()
            self.verified = self.get_verified()
            self.nsfw_allowed = self.get_nsfw_allowed()
            self.bio = self.get_bio()
            self.creation_date = self.get_creation_date()

            hide_token = Ask("Hide token (y/n)")
            if hide_token.lower() in ["n", "no", "non", "false"]:
                hide_token = False
            else:
                hide_token = True

            Clear()
            Menu()
            input(f"""
{self.co}Token             :{RESET} {f"{self.token[:50]}**********************" if hide_token else self.token}
{self.co}User ID           :{RESET} {self.user_id}
{self.co}Display Name      :{RESET} {self.display_name}
{self.co}Username          :{RESET} {self.username}#{self.discriminator}
{self.co}Avatar url        :{RESET} {self.avatar_url}
{self.co}Banner url        :{RESET} {self.banner_url}
{self.co}Banner Color      :{RESET} {self.banner_color}
{self.co}Creation Date     :{RESET} {self.creation_date}

{self.co}Premium Type      :{RESET} {self.premium_type}
{self.co}Language          :{RESET} {self.lang}

{self.co}MFA Enabled       :{RESET} {self.mfa_enabled}

{self.co}Email             :{RESET} {self.email}
{self.co}Phone             :{RESET} {self.phone}
{self.co}Verified          :{RESET} {self.verified}
{self.co}NSFW Allowed      :{RESET} {self.nsfw_allowed}

{self.co}Bio               :{RESET} {self.bio}
""")
        else:
            Log(R, "x", "Invalid token", wp=True)
            time.sleep(1.5)