import sys
from colorama import init, Fore, Back
import keyboard
init(autoreset=True)


class Main:
    def __init__(self):
        self.lineLen = 64
        self.bgCol = Back.RED
        self.col = Fore.WHITE

        self.allowedChars = "qwertzuiopasdfghjklyxcvbnm "
        return

    def Center(self, txt):
        tlen = len(txt)
        if len(txt) % 2 != 0:
            txt += " "
        centerSpaces = " " * ((self.lineLen - tlen) // 2)
        return centerSpaces + txt + centerSpaces + "⠀"

    def EmptyLine(self):
        return self.bgCol + self.col + " " * self.lineLen + "⠀"

    def CenteredTitle(self, txt):
        return self.bgCol + self.col + self.Center(txt)

    def Text(self, txt):
        tlen = len(txt)
        return self.bgCol + self.col + txt + " " * (self.lineLen - tlen) + "⠀"

    def KeepingInput(self, txt):
        self.altText = txt
        self.thisText = ""
        print(self.Text(self.altText), end="\r")
        # sys.stdout.write(self.Text(self.altText))
        keyboard.hook(self._handleKeyInput)
        try:
            keyboard.wait("enter")
        except KeyboardInterrupt:
            pass
        return

    def _handleKeyInput(self, inf):
        eventType = inf.event_type
        key = inf.name
        if eventType == "down" and key in self.allowedChars:
            if len(self.altText) + len(self.thisText) + 1 >= self.lineLen:
                return
            self.thisText += key
            sys.stdout.write("\r\r" + self.Text(self.altText + self.thisText))
            sys.stdout.flush()
        return

    def PrintMotd(self):
        print(self.EmptyLine())
        print(self.EmptyLine())
        print(self.CenteredTitle("HWinfo"))
        print(self.EmptyLine())
        print(self.CenteredTitle("Created by esec team"))
        print(self.CenteredTitle("(c) 2021"))
        print(self.EmptyLine())
        print(self.EmptyLine())
        # print(self.Text("Select, what do you want to do:"))
        # print(self.EmptyLine())
        return

    def PrintChoices(self):
        return
