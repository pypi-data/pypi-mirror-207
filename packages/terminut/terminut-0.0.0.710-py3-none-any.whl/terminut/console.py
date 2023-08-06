from colorama import Fore
from datetime import datetime
from time     import time
from re       import sub
from colorsys import hsv_to_rgb


class Settings:
    initialized = False
    debug = True 
    timestamp = True
    c_MAIN = Fore.LIGHTBLUE_EX
    c_SECO = Fore.LIGHTBLACK_EX

class Console:
    def init(
        debug: bool = True,
        showTimestamp: bool = True,
        colMain = Fore.LIGHTBLUE_EX,
        colSeco = Fore.LIGHTBLACK_EX,
        madeBy = "vast#1337"
    ):
        Settings.initialized = True
        Settings.debug = debug
        Settings.timestamp = showTimestamp
        Settings.c_MAIN = colMain
        Settings.c_SECO = colSeco


    @staticmethod
    def printf(content: str, mainCol=None, showTimestamp=None):
        if showTimestamp is None: showTimestamp = Settings.timestamp
        if mainCol is None: mainCol = Settings.c_MAIN
        if type(content) != str: return print(content)
        if (
            ("(!)" in content)
            or ("(-)" in content)
            or ("(~)" in content) 
            or ("debug" in content.lower())
            ) and (Settings.debug == False): return
        
        timestamp = f'{Settings.c_SECO}{datetime.fromtimestamp(time()).strftime("%H:%M:%S")}{Fore.RESET} ' if (showTimestamp) else ''
        
        content   = sub(r'\[(.*?)]', rf'{Settings.c_SECO}[{mainCol}\1{Settings.c_SECO}]{Fore.RESET}', content)
        content   = content\
            .replace("|", f"{Settings.c_SECO}|{mainCol}")\
            .replace("->", f"{Settings.c_SECO}->{mainCol}")\
            .replace("(+)", f"{Settings.c_SECO}({Fore.GREEN}+{Settings.c_SECO}){mainCol}")\
            .replace("($)", f"{Settings.c_SECO}({Fore.GREEN}${Settings.c_SECO}){mainCol}")\
            .replace("(-)", f"{Settings.c_SECO}({Fore.RED}-{Settings.c_SECO}){mainCol}")\
            .replace("(!)", f"{Settings.c_SECO}({Fore.RED}!{Settings.c_SECO}){mainCol}")\
            .replace("(~)", f"{Settings.c_SECO}({Fore.YELLOW}~{Settings.c_SECO}){mainCol}")\
            .replace("(#)", f"{Settings.c_SECO}({Fore.BLUE}#{Settings.c_SECO}){mainCol}")\
            .replace("(*)", f"{Settings.c_SECO}({Fore.CYAN}*{Settings.c_SECO}){mainCol}")
        
            # .replace("(", f"{Settings.c_SECO}({Fore.RESET}").replace(")", f"{Settings.c_SECO}){Fore.RESET}")
            # .replace("[", f"{Settings.c_SECO}[{mainCol}")\
            
        return print(timestamp + content, end=f"{Fore.RESET}\n")
        
        
    @staticmethod
    def inputf(content: str):
        if "(?)" not in content: x = f"{Settings.c_SECO}({Settings.c_MAIN}?{Settings.c_SECO}){Fore.RESET} "
        else: x = ""
        content = x + content\
            .replace("(", f"{Settings.c_SECO}({Settings.c_MAIN}").replace(")", f"{Settings.c_SECO}){Settings.c_MAIN}")\
            .replace(">", f"{Settings.c_SECO}>{Fore.RESET}")
        return input(content)




class BetaConsole:
    def __init__(self, speed: int = 2, showMS: int = 4):
        self.colHue = 120
        self.speed = speed
        self.direction = self.speed
        self.showMS = showMS

    def getTimestamp(self):
        rgb = hsv_to_rgb(self.colHue / 360, 1, 1)
        red = int(rgb[0] * 255)
        green = int(rgb[1] * 255)
        blue = int(rgb[2] * 255)

        current_time = datetime.now().strftime("%H:%M:%S.%f")[:-self.showMS]
        timestamp = f"\033[38;2;{red};{green};{blue}m{current_time}\033[0m"

        self.colHue += self.direction
        if self.colHue >= 240:
            self.direction = -self.speed
        elif self.colHue <= 120:
            self.direction = self.speed

        return timestamp

    def alphaPrint(self):
        print(self.getTimestamp())

