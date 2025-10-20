import psutil


class SystemStats:
    def __init__(self):
        self.cpup = None
        self.memoryp = None
        self.diskp = None

    def get_system_info(self):

        cpu_percent = psutil.cpu_percent(interval=0)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        self.cpup = f"CPU IS AT: {cpu_percent}%"
        self.memoryp = f"Memory Usage: {memory.used / (1024 ** 3):.2f} GB/ {memory.total / (1024 ** 3):.2f} GB"
        self.diskp = f"Disk Usage: {disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 **3):.2f} GB"

        return self.cpup, self.memoryp, self.diskp

    def get_raw_stats(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        return cpu, mem, disk


status = SystemStats()
