import psutil


class SystemStats:

    def get_system_info(self):

        cpu_percent = psutil.cpu_percent(interval=0)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        self.cpu = f"CPU IS AT: {cpu_percent}%"
        self.memory = f"Memory Usage: {memory.used / (1024 ** 3):.2f} GB/ {memory.total / (1024 ** 3):.2f} GB"
        self.disk = f"Disk Usage: {disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 **3):.2f} GB"

        return self.cpu, self.memory, self.disk

    def get_raw_stats(self):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
        return cpu, mem, disk


status = SystemStats()
