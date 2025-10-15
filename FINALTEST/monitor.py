import psutil

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    cpup = (f"CPU IS AT     {cpu_percent}%")
    memoryp = (f"Memory Usage: {memory.used / (1024 ** 3):.2f} / {memory.total / (1024 ** 3):.2f} bytes")
    diskp = (f"Disk Usage:   {disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 **3):.2f}GB")
    return cpup, memoryp, diskp 
get_system_info()
