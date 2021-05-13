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
        print(self.column("Press 4 for analyzing Network"))

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
            used_virtual_mem = str(psutil.virtual_memory()[3]) + " Used Virtual Memory"
            free_virtual_mem = str(psutil.virtual_memory()[4]) + " Free Virtual Memory"
            print(self.column(used_virtual_mem))
            print(self.column(free_virtual_mem))
            print(self.column(" "))
            print(self.column("Swap Memory:"))
            total_swap_mem = str(psutil.swap_memory()[0]) + " Total Swap Memory"
            used_swap_mem = str(psutil.swap_memory()[1]) + " Used Swap Memory"
            free_swap_mem = str(psutil.swap_memory()[2]) + " Free Swap Memory"
            print(self.column(total_swap_mem))
            print(self.column(used_swap_mem))
            print(self.column(free_swap_mem))
        
        #Need fix only to show particular partition not in the whole row 
        elif choice == "3":
            print(self.column("Disk Partition: "))
            device_disk_part = str(psutil.disk_partitions()) + " Device Disks Partitions"
            print(self.column(device_disk_part))
        
        elif choice == "4":
            print(self.column("Packet State:"))
            packets_sent = str(psutil.net_io_counters()[2]) + " Bytes Send"
            packets_receive = str(psutil.net_io_counters()[3]) + " Bytes Send"            
            print(self.column(packets_sent))
            print(self.column(packets_receive))
            print(self.column(" "))
            print(self.column("Network Connections:"))
            #Same as the diskparts only show the particular thing
            net_con = str(psutil.net_connections())
            print(self.column(net_con))
            print(self.column(" "))
            print(self.column("Ip Adresses:"))
            ip_addr = str(psutil.net_if_addrs())
            print(self.column(ip_addr))
            print(self.column(" "))
            print(self.column("Network Stats:"))
            net_stat = str(psutil.net_if_stats())
            print(self.column(net_stat))





            
            


