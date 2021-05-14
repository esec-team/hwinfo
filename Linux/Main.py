import colorama
import psutil
from colorama import init, Fore, Back
class Main:
    def __init__(self):
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
        return self.riadokFarba + " " * self.lineLen + "‎"

    def lineleft(self, text):
        return self.riadokFarba + text    

    def row(self, text):
        spaces = self.lineLen - len(text)
        return self.riadokFarba + text + " " * spaces + "‎"

    def output(self,):
        self.riadokFarba + " " * self.lineLen + "‎"

    def test(self):
        print(self.line())
        print(self.line())
        print(self.center("Linux PC Analyzer"))
        print(self.line())
        print(self.center("Created by @ Esec Team 2021"))
        print(self.line())
    
    def choose(self):
        print(self.row("Press 1 for analyzing CPU"))
        print(self.row("Press 2 for analyzing Memory"))
        print(self.row("Press 3 for analyzing Disks"))
        print(self.row("Press 4 for analyzing Network"))

        choice = input(self.lineleft("Choose which part you want to analyze:")) 
        print(self.line())

        if choice == "1":
            print(self.row("CPU Times:"))
            user_times = str(psutil.cpu_times_percent()[0]) + " User"
            system_times = str(psutil.cpu_times_percent()[2]) + " System"
            idle_times = str(psutil.cpu_times_percent()[3]) + " Idle"
            print(self.row(user_times))
            print(self.row(system_times))
            print(self.row(idle_times))
            print(self.row(" "))
            print(self.row("CPU Cores:"))
            cpu_cores = str(psutil.cpu_count()) + " CPU Cores"
            usable_cpu_cores = str(len(psutil.Process().cpu_affinity())) + " Usable CPU Cores"
            print(self.row(cpu_cores))
            print(self.row(usable_cpu_cores))
            print(self.row(" "))
            print(self.row("CPU Frequency:"))
            current_cpu_frequency = str(psutil.cpu_freq()[0]) + " Current CPU Frequency"
            max_cpu_frequency = str(psutil.cpu_freq()[1]) + " Maximum CPU Frequency"
            print(self.row(current_cpu_frequency))
            print(self.row(max_cpu_frequency))
            print(self.center("@ Ernest Habán 2021"))
            print(self.row(" "))
        
        elif choice == "2":
            print(self.row("Virtual Memory:"))
            used_virtual_mem = str(psutil.virtual_memory()[3]) + " Used Virtual Memory"
            free_virtual_mem = str(psutil.virtual_memory()[4]) + " Free Virtual Memory"
            print(self.row(used_virtual_mem))
            print(self.row(free_virtual_mem))
            print(self.row(" "))
            print(self.row("Swap Memory:"))
            total_swap_mem = str(psutil.swap_memory()[0]) + " Total Swap Memory"
            used_swap_mem = str(psutil.swap_memory()[1]) + " Used Swap Memory"
            free_swap_mem = str(psutil.swap_memory()[2]) + " Free Swap Memory"
            print(self.row(total_swap_mem))
            print(self.row(used_swap_mem))
            print(self.row(free_swap_mem))
            print(self.center("@ Ernest Habán 2021"))
            print(self.row(" "))
         
        elif choice == "3":
            print(self.row("All disk partitions: "))
            all_partitions = psutil.disk_partitions()
            for partition in all_partitions:
                print(self.row(f"{partition.device} {partition.fstype}"))
            print(self.center("@ Ernest Habán 2021"))
            print(self.row(" "))
        
        elif choice == "4":
            print(self.row("Packet State:"))
            packets_sent = str(psutil.net_io_counters()[2]) + " Bytes Send"
            packets_receive = str(psutil.net_io_counters()[3]) + " Bytes Send"            
            print(self.row(packets_sent))
            print(self.row(packets_receive))
            print(self.row(" "))
            print(self.row("Network Connections:"))
            net_con_count = str(len(psutil.net_connections())) + " Currently connected services"
            print(self.row(net_con_count))
            print(self.row(" "))
            print(self.row("Network Adapters:"))
            net_adapt = psutil.net_if_addrs()
            for adapter_name in net_adapt:
                print(self.row(f"{adapter_name} {net_adapt[adapter_name][0].address} {net_adapt[adapter_name][0].netmask}"))
            print(self.row(" "))
            print(self.row("Network Speed Stats:"))
            net_stat = psutil.net_if_stats()
            for speed_net in net_stat:
                print(self.row(f"{speed_net} {net_stat[speed_net].speed}"))
            print(self.center("@ Ernest Habán 2021"))
            print(self.row(" "))
