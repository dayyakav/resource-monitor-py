import psutil
import time
import logging

def get_cpu_info():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > 90:
        logging.info(f"High CPU usage: {cpu}%")
        
    return f"CPU % : {cpu} %"

def get_mem_info():
    mem = psutil.virtual_memory()
    used = mem.used / (1024**3)
    total = mem.total / (1024**3)

    return f"MEMORY : {used:.1f} GiB / {total:.0f} GiB"

def get_net_info():
    prev_net = psutil.net_io_counters()

    time.sleep(1)

    curr_net = psutil.net_io_counters()

    download = curr_net.bytes_recv - prev_net.bytes_recv
    upload = curr_net.bytes_sent - prev_net.bytes_sent

    return f"NETWORK: Download : {download} B/s | Upload : {upload} B/s"


def get_processes(count=10):
    procs = []

    for p in psutil.process_iter():
        procs.append((p.cpu_percent(), p.pid, p.name()))

    #sort by cpu_percent
    procs.sort(reverse=True)
    
    result = []
    for cpu, pid, name in procs[:count]:
        result.append(f"PID: {pid} - «{name}» - {cpu} %")

    return result

