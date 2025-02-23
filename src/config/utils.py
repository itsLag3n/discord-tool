import os
import sys
import ctypes
from datetime import datetime
import time

name = "Discord Tool"
version = "1.0.0"

RESET = "\033[0m"
W = "\033[37m"
M = "\033[35m"
G = "\033[32m"
R = "\033[31m"
B = "\033[34m"
O = "\033[33m"

co = O

banner = f"""
    {co}┌┬┐┬┌─┐┌─┐┌─┐┬─┐┌┬┐    ┌┬┐┌─┐┌─┐┬  
     │││└─┐│  │ │├┬┘ ││     │ │ ││ ││  
    ─┴┘┴└─┘└─┘└─┘┴└──┴┘     ┴ └─┘└─┘┴─┘{RESET}"""

options1 = f"""
{co}[{W}01{co}] {W}User Lookup
{co}[{W}02{co}] {W}Token Lookup
{co}[{W}03{co}] {W}ID To Token
"""

options2 = f"""

"""

def Menu(page: str = None):
    print(banner)
    if page:print(options1 if page == "1" else options2)

def Clear():
    os.system('cls' if os.name=='nt' else 'clear')

def Title(title: str):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(f"{name} v{version} | {title}")
    elif sys.platform.startswith("linux"):
        sys.stdout.write(f"\x1b]2;{name} v{version} | {title}\x07")

def Log(color, symbole, message, end="\n", flush=False, wp=False):
    if wp: print("")
    print(f"{RESET}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {color}[{W}{symbole}{color}]{W} {message}", end=end, flush=flush)

def FormatLog(color, symbole, message, end="\n", flush=False):
    return f"{RESET}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {color}[{W}{symbole}{color}]{W} {message}"

def Ask(text: str):
    return input(f"{co}{text}{W} > {RESET}")

def CommingSoon(wp=True):
    if wp: print("")
    Log(R, "!", "Comming soon")
    time.sleep(1.5)

def InvalidChoice(wp=True):
    if wp: print("")
    Log(R, "!", "Invalid Choice")
    time.sleep(1.5)