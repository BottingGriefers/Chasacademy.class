import time
import psutil
from alarms import *
from design import *
from monitor import *
import os
from datetime import datetime
stats = get_system_info(cpu=True, memory=True, disk=True)

def get_local_time():
    return datetime.now().strftime("%H:%M:%S")


def main():
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen each second

        border(f"""=== Main Menu ===
1. Start Monitoring System      {get_local_time()}
2. Show Alarm                   CPU at: {stats["cpu"]} %
3. Create an Alarm              Disk Usage: {stats["disk"]}   
4. Remove an Alarm              Memory Usage: {stats['memory'].used_gb}      
5. Show Alarms
6. Exit
""")

        time.sleep(5)  # refresh every second


# 🟢 Start the program
main()
