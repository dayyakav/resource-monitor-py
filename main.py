import os, sys, time, rich, logging
import logger

from utils import get_cpu_info, get_mem_info, get_net_info, get_processes

# Main loop
while True:
    cpu_info = get_cpu_info()
    mem_info = get_mem_info()
    net_info = get_net_info()

    try:
        # Configurable process count
        processes = get_processes(count=7)

        # Clear terminal
        print("\033c", end="")

        # Displayed info
        rich.print(cpu_info)
        rich.print(mem_info)
        rich.print(net_info)
        print("")
        for item in processes:
            rich.print(item)

    # I know it's a bad idea
    except Exception as e:
        logging.error(e)
