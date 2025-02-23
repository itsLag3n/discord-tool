from src.config.config import *

page = "1"
options = {
    1: user_id_lookup().main,
    2: token_lookup().main,
    3: id_to_token().main,
    4: CommingSoon,
    5: CommingSoon,
    6: CommingSoon,
    7: CommingSoon,
    8: CommingSoon,
    9: CommingSoon,
}

def main():
    while 1:
        Clear()
        Title("Menu")
        Menu(page)
        choice = Ask("Choice")
        try:
            options[int(choice)]()
        except:
            InvalidChoice()

main()