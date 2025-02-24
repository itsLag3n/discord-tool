from src.config.config import *

options = {
    "!": lambda: settings().main(),
    ">": lambda: next_page(page).main(),
    "<": lambda: previous_page(page).main(),
    "1": lambda: user_id_lookup().main(),
    "2": lambda: token_lookup().main(),
    "3": lambda: id_to_token().main(),
    "4": lambda: token_checker().main(),
    "5": lambda: multi_token_checker().main(),
    "6": lambda: token_filter().main(),
    
    "!!": lambda: settings().main(),
    ">>": lambda: next_page(page).main(),
    "<<": lambda: previous_page(page).main(),
    "01": lambda: user_id_lookup().main(),
    "02": lambda: token_lookup().main(),
    "03": lambda: id_to_token().main(),
    "04": lambda: token_checker().main(),
    "05": lambda: multi_token_checker().main(),
    "06": lambda: token_filter().main(),
}

def main():
    global page, co
    while 1:
        Clear()
        Title("Menu")
        Menu(page)
        choice = Ask("Choice")
        try:
            result = options[choice]()
            if not result: continue
            if result[0] == "page":
                page = result[1]
            elif result[0] == "color":
                set_color(result[1])
        except:
            InvalidChoice()

main()