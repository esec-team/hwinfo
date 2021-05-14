import psutil
class Main:
    def __init__(self):
        self.lineLen = 100
    def center(self, text):
        textlen = len(text)
        if textlen %2 != 0:
            text += " "
        zoradenie = (self.lineLen - textlen) // 2
        return " " * zoradenie + text + " " * zoradenie

    def test(self):
        print()
        print()
        print(self.center("Windows PC Analyzer"))
        print()
        print(self.center("Created by @ Esec Team 2021"))
        print()
    
    def choose(self):
        print("Press 1 for analyzing CPU")
        print("Press 2 for analyzing Memory")
        print("Press 3 for analyzing Disks")
        print("Press 4 for analyzing Network")

        choice = input(("Choose which part you want to analyze:")) 
        print()

        if choice == "1":
            print("CPU Times:")
            user_times = str(psutil.cpu_times_percent()[0]) + " User"
            system_times = str(psutil.cpu_times_percent()[2]) + " System"
            idle_times = str(psutil.cpu_times_percent()[3]) + " Idle"
            print(user_times)
            print(system_times)
            print(idle_times)
            print(" ")
            print("CPU Cores:")
            cpu_cores = str(psutil.cpu_count()) + " CPU Cores"
            usable_cpu_cores = str(len(psutil.Process().cpu_affinity())) + " Usable CPU Cores"
            print(cpu_cores)
            print(usable_cpu_cores)
            print(" ")
            print("CPU Frequency:")
            current_cpu_frequency = str(psutil.cpu_freq()[0]) + " Current CPU Frequency"
            max_cpu_frequency = str(psutil.cpu_freq()[1]) + " Maximum CPU Frequency"
            print(current_cpu_frequency)
            print(max_cpu_frequency)
            print(self.center("@ Ernest Habán 2021"))
            print(" ")
        
        elif choice == "2":
            print("Virtual Memory:")
            used_virtual_mem = str(psutil.virtual_memory()[3]) + " Used Virtual Memory"
            free_virtual_mem = str(psutil.virtual_memory()[4]) + " Free Virtual Memory"
            print(used_virtual_mem)
            print(free_virtual_mem)
            print(" ")
            print("Swap Memory:")
            total_swap_mem = str(psutil.swap_memory()[0]) + " Total Swap Memory"
            used_swap_mem = str(psutil.swap_memory()[1]) + " Used Swap Memory"
            free_swap_mem = str(psutil.swap_memory()[2]) + " Free Swap Memory"
            print(total_swap_mem)
            print(used_swap_mem)
            print(free_swap_mem)
            print(self.center("@ Ernest Habán 2021"))
            print(" ")
         
        elif choice == "3":
            print("All disk partitions: ")
            all_partitions = psutil.disk_partitions()
            for partition in all_partitions:
                print(f"{partition.device} {partition.fstype}")
            print(self.center("@ Ernest Habán 2021"))
            print(" ")
        
        elif choice == "4":
            print("Packet State:")
            packets_sent = str(psutil.net_io_counters()[2]) + " Bytes Send"
            packets_receive = str(psutil.net_io_counters()[3]) + " Bytes Send"            
            print(packets_sent)
            print(packets_receive)
            print(" ")
            print("Network Connections:")
            net_con_count = str(len(psutil.net_connections())) + " Currently connected services"
            print(net_con_count)
            print(" ")
            print("Network Adapters:")
            net_adapt = psutil.net_if_addrs()
            for adapter_name in net_adapt:
                print(f"{adapter_name} {net_adapt[adapter_name][0].address} {net_adapt[adapter_name][0].netmask}")
            print(" ")
            print("Network Speed Stats:")
            net_stat = psutil.net_if_stats()
            for speed_net in net_stat:
                print(f"{speed_net} {net_stat[speed_net].speed}")
            print(self.center("@ Ernest Habán 2021"))
            print(" ")
