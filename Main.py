from colorama import init, Fore, Back
init(autoreset=True)


class Main:
    def __init__(self):
        self.lineLen = 64
        self.bgCol = Back.RED
        self.col = Fore.WHITE
        return

    def Center(self, txt):
        tlen = len(txt)
        if len(txt) % 2 != 0:
            txt += " "
        centerSpaces = " " * ((self.lineLen - tlen) // 2)
        out = centerSpaces + txt + centerSpaces + "⠀"
        return centerSpaces + txt + centerSpaces + "⠀"

    def EmptyLine(self):
        return self.bgCol + " " * self.lineLen + "⠀"

    def CenteredTitle(self, txt):
        return self.bgCol + self.col + self.Center(txt)

    def Text(self, txt):
        tlen = len(txt)
        return self.bgCol + txt + " " * (self.lineLen - tlen) + "⠀"

    def PrintMotd(self):
        print(self.EmptyLine())
        print(self.EmptyLine())
        print(self.CenteredTitle("HWinfo"))
        print(self.EmptyLine())
        print(self.CenteredTitle("Created by esec team"))
        print(self.CenteredTitle("(c) 2021"))
        print(self.EmptyLine())
        print(self.EmptyLine())
        print(self.Text("Select, what do you want to do:"))
        print(self.EmptyLine())
        return

    def PrintChoices(self):
        return
