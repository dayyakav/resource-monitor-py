import os
import sys
import time

import rich

import setup
from utils import get_cpu_info, get_mem_info, get_net_info, get_processes

# main loop
while True:
    cpu_info = get_cpu_info()
    mem_info = get_mem_info()
    net_info = get_net_info()
    processes = get_processes(count=7)

    os.system("cls" if os.name == "nt" else "clear")

    rich.print(cpu_info)
    rich.print(mem_info)
    rich.print(net_info)
    print("")
    for item in processes:
        rich.print(item)
