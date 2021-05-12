from colorama import init, Fore, Back
from Main import Main

init(autoreset=True)

main = Main()
main.PrintMotd()
main.PrintChoices()
main.KeepingInput("Write something about niggers: ")
