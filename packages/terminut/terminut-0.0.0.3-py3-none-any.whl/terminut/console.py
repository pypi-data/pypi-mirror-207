from colorama import Fore
from datetime import datetime
from time     import time

debug = True 
c_MAIN = Fore.LIGHTBLACK_EX
c_SECO = Fore.LIGHTBLUE_EX

@staticmethod
def printf(content: str):
    if type(content) != str: return print(content)
    if (("(!)" in content) or ("(-)" in content) or ("(~)" in content)) and (debug == False): return
    
    print(
        f'{c_MAIN}{datetime.fromtimestamp(time()).strftime("%H:%M:%S")}{Fore.RESET} ' +
        content
        .replace("[", f"{c_MAIN}[{Fore.MAGENTA}")
        .replace("]", f"{c_MAIN}]{Fore.RESET}")
        .replace("|", f"{c_MAIN}|{c_SECO}")
        .replace("->", f"{c_MAIN}->{c_SECO}")

        # .replace("(", f"{c_MAIN}({Fore.RESET}").replace(")", f"{c_MAIN}){Fore.RESET}")
        .replace("(+)", f"{c_MAIN}({Fore.GREEN}+{c_MAIN}){c_SECO}")
        .replace("($)", f"{c_MAIN}({Fore.GREEN}${c_MAIN}){c_SECO}")
        .replace("(-)", f"{c_MAIN}({Fore.RED}-{c_MAIN}){c_SECO}")
        .replace("(!)", f"{c_MAIN}({Fore.RED}!{c_MAIN}){c_SECO}")
        .replace("(~)", f"{c_MAIN}({Fore.YELLOW}~{c_MAIN}){c_SECO}")
        .replace("(#)", f"{c_MAIN}({Fore.BLUE}#{c_MAIN}){c_SECO}")
        .replace("(*)", f"{c_MAIN}({Fore.CYAN}*{c_MAIN}){c_SECO}")
    , end=f"{Fore.RESET}\n")
    
@staticmethod
def inputf(content: str):
    if "(?)" not in content: x = f"{c_MAIN}({c_SECO}?{c_MAIN}){Fore.RESET} "
    else: x = ""
    content = x + content\
        .replace("(", f"{c_MAIN}({c_SECO}").replace(")", f"{c_MAIN}){c_SECO}")\
        .replace(">", f"{c_MAIN}>{Fore.RESET}")
    return input(content)