import os, sys, time, rich
import logger

from utils import get_cpu_info, get_mem_info, get_net_info, get_processes

# Main loop
while True:
    cpu_info = get_cpu_info()
    mem_info = get_mem_info()
    net_info = get_net_info()

    # Configurable process count to display
    processes = get_processes(count=7)

    # If os windows or linux - clear terminal
    os.system("cls" if os.name == "nt" else "clear")

    # Displayed info
    rich.print(cpu_info)
    rich.print(mem_info)
    rich.print(net_info)
    print("")
    for item in processes:
        rich.print(item)
