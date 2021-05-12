import colorama
import psutil
from colorama import init, Fore, Back
class Main:
    def __init__(self):
        self.headNadpis = "HWInfo"
        self.headText = 25
        self.lineLen = 100
        self.bcgColor = Back.LIGHTBLACK_EX
        self.txtColor = Fore.LIGHTWHITE_EX
        self.riadokFarba = Back.LIGHTRED_EX
    def center(self, text):
        textlen = len(text)
        if textlen %2 != 0:
            text += " "
        zoradenie = (self.lineLen - textlen) // 2
        return self.riadokFarba + " " * zoradenie + text + " " * zoradenie + "‎"
    def line(self):
        return self.riadokFarba + " " * self.lineLen + "‎‎"

    def lineleft(self, text):
        return self.riadokFarba + text    

    def column(self, text):
        spaces = self.lineLen - len(text)
        return self.riadokFarba + text + " " * spaces + "‎"

    def output(self,):
        self.riadokFarba + " " * self.lineLen + "‎"

    def test(self):
        print(self.line())
        print(self.line())
        print(self.center("HWInfo1"))
        print(self.line())
        print(self.center("Created by @ Esec Team 2021"))
        print(self.line())
    
    def choose(self):
        print(self.column("Press 1 for analyzing CPU"))
        print(self.column("Press 2 for analyzing Memory"))
        print(self.column("Press 3 for analyzing Disks"))

        choice = input(self.lineleft("Choose which part you want to analyze:")) 
        print(self.column(" "))

        if choice == "1":
            print(self.column("CPU Times:"))
            user_times = str(psutil.cpu_times_percent()[0]) + " User"
            system_times = str(psutil.cpu_times_percent()[2]) + " System"
            idle_times = str(psutil.cpu_times_percent()[3]) + " Idle"
            print(self.column(user_times))
            print(self.column(system_times))
            print(self.column(idle_times))
            print(self.column(" "))
            print(self.column("CPU Cores:"))
            cpu_cores = str(psutil.cpu_count()) + " CPU Cores"
            usable_cpu_cores = str(len(psutil.Process().cpu_affinity())) + " Usable CPU Cores"
            print(self.column(cpu_cores))
            print(self.column(usable_cpu_cores))
            print(self.column(" "))
            print(self.column("CPU Frequency:"))
            current_cpu_frequency = str(psutil.cpu_freq()[0]) + " Current CPU Frequency"
            max_cpu_frequency = str(psutil.cpu_freq()[1]) + " Maximum CPU Frequency"
            print(self.column(current_cpu_frequency))
            print(self.column(max_cpu_frequency))
        
        elif choice == "2":
            print(self.column("Virtual Memory:"))
            total_virtual_mem = str(psutil.virtual_memory()[0]) + " Total Virtual Memory"
            available_virtual_mem = str(psutil.virtual_memory()[1]) + " Available Virtual Memory"
            percent_virtual_mem = str(psutil.virtual_memory()[2]) + " Percent Virtual Memory"
            used_virtual_mem = str(psutil.virtual_memory()[3]) + " Used Virtual Memory"
            free_virtual_mem = str(psutil.virtual_memory()[4]) + " Free Virtual Memory"
            active_virtual_mem = str(psutil.virtual_memory()[5]) + " Active Virtual Memory"
            inactive_virtual_mem = str(psutil.virtual_memory()[6]) + " Inactive Virtual Memory"
            print(self.column(total_virtual_mem))
            print(self.column(available_virtual_mem))
            print(self.column(percent_virtual_mem))
            print(self.column(used_virtual_mem))
            print(self.column(free_virtual_mem))
            print(self.column(active_virtual_mem))
            print(self.column(inactive_virtual_mem))
            print(self.column(" "))
            print(self.column("Swap Memory:"))
            total_swap_mem = str(psutil.swap_memory()[0]) + " Total Swap Memory"
            used_swap_mem = str(psutil.swap_memory()[1]) + " Used Swap Memory"
            free_swap_mem = str(psutil.swap_memory()[2]) + " Free Swap Memory"
            print(self.column(total_swap_mem))
            print(self.column(used_swap_mem))
            print(self.column(free_swap_mem))
            



