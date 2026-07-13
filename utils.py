import psutil
import time
import logging

# Returns CPU usage in %
def get_cpu_info():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > 90:
        logging.info(f"High CPU usage: {cpu}%")

    return f"CPU % : {cpu} %"

# Returns used and total memory usage
def get_mem_info():
    mem = psutil.virtual_memory()
    used = mem.used / (1024**3)
    total = mem.total / (1024**3)

    return f"MEMORY : {used:.1f} GiB / {total:.0f} GiB"

# Returns download and upload info in MB/s
def get_net_info():
    prev_net = psutil.net_io_counters()

    time.sleep(1)

    curr_net = psutil.net_io_counters()

    download = (curr_net.bytes_recv - prev_net.bytes_recv) / 1_000_000
    upload = (curr_net.bytes_sent - prev_net.bytes_sent) / 1_000_000

    return f"NETWORK: Download : {download:.2f} MB/s | Upload : {upload:.2f} MB/s"

# Returns list of processes with PID, name and CPU %
def get_processes(count=10):
    procs = []

    for p in psutil.process_iter():
        procs.append((p.cpu_percent(), p.pid, p.name()))

    # Sort by cpu_percent
    procs.sort(reverse=True)

    result = []
    for cpu, pid, name in procs[:count]:
        result.append(f"PID: {pid} - «{name}» - {cpu} %")

    return result
