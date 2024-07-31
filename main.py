import psutil

CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 80 

# CPU USAGE:
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"CPU usage is {cpu_percent}%, which exceeds the threshold of {CPU_THRESHOLD}%")

# MEMORY USAGE:
def check_memory_usage():
    mem = psutil.virtual_memory()
    mem_percent = mem.percent
    if mem_percent > MEMORY_THRESHOLD:
        print(f"Memory usage is {mem_percent}%, which exceeds the threshold of {MEMORY_THRESHOLD}%")

# DISK USAGE:
def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent
    if disk_percent > DISK_THRESHOLD:
        print(f"Disk usage is {disk_percent}%, which exceeds the threshold of {DISK_THRESHOLD}%")

# RUNNING PROCESSES:
def check_running_processes():
    num_processes = len(psutil.pids())
    if num_processes > 0:
        print(f"Number of running processes: {num_processes}")
    else:
        print("No running processes found.")


def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
