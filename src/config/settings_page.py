from src.config.utils import *
from src.config.settings.change_color import *

class settings:
    def __init__(self):
        self.options = {
            "1": lambda: change_color().main(),
            
            "01": lambda: change_color().main(),
        }

    def main(self):
        while 1:
            Clear()
            Title("Settings")
            Menu("settings")
            choice = Ask("Choice")
            try:
                if choice in ["!", "!!"]:
                    break
                result = self.options[choice]()
                if result:
                    return result
            except:
                InvalidChoice()
