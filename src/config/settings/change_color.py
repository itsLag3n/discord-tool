from src.config.utils import *

class change_color:
    def __init__(self):
        self.options = {
            "1": lambda: self.change_color("orange"),
            "2": lambda: self.change_color("magenta"),
            "3": lambda: self.change_color("green"),
            "4": lambda: self.change_color("blue"),
            "5": lambda: self.change_color("red"),

            "01": lambda: self.change_color("orange"),
            "02": lambda: self.change_color("magenta"),
            "03": lambda: self.change_color("green"),
            "04": lambda: self.change_color("blue"),
            "05": lambda: self.change_color("red"),
        }
        self.colours = {
            "orange": O,
            "magenta": M,
            "green": G,
            "blue": B,
            "red": R
        }

    def change_color(self, color):
        co = self.colours[color]
        Log(co, "!", f"color changed to {co}{color}")
        return co

    def main(self):
        Clear()
        Title("Change Color")
        Menu("change_color")
        choice = Ask("Choice")
        try:
            color = self.options[choice]()
            if color:
                return "color", color
        except:
            InvalidChoice()