import psutil
from colorama import init, Fore, Back
class Main:
    def __init__(self):
        self.headNadpis = "HWInfo"
        self.headText = 25
        self.lineLen = 100
        self.bcgColor = Back.LIGHTBLACK_EX
        self.txtColor = Fore.LIGHTWHITE_EX
        self.riadokFarba = Back.LIGHTCYAN_EX
    def center(self, text):
        textlen = len(text)
        if textlen %2 != 0:
            text += " "
        zoradenie = (self.lineLen - textlen) // 2
        return self.riadokFarba + " " * zoradenie + text + " " * zoradenie + "‎"
    def line(self):
        return self.riadokFarba + " " * self.lineLen + "‎‎"

    def lineleft(self, text):
        spaces = self.lineLen - len(text)
        return self.riadokFarba + text + " " * spaces + "‎"
    
    def test(self):
        print(self.line())
        print(self.line())
        print(self.center("HWInfo1"))
        print(self.line())
        print(self.center("Created by @ Esec Team 2021"))
        print(self.line())
    def choose(self):
        print(self.lineleft("Choose which part you want to analyze:"))
        hodnota = input("")