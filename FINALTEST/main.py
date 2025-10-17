import time
import psutil
from alarms import *
from design import *
from monitor import *
import os
from datetime import datetime


def get_local_time():
    return datetime.now().strftime("%H:%M")

def press_to_continue():
     while True:
        c = input("Press Enter to continue: ")
        if c == "":   # empty string means Enter was pressed
            break
        else:
            print("Just press Enter, you buffoon")



def console_cleaner():
     os.system('cls' if os.name == 'nt' else 'clear')

def main():
    
    stats = SystemStats()
    
    while True:
        cpu_str, mem_str, disk_str = stats.get_system_info()
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen each second

        border(f"""
1. Start Monitoring System      [#0349fc][bold]Current time: {get_local_time()}[/#0349fc][/bold] 
2. Create an Alarm                   [bold][#0349fc]{cpu_str}[/#0349fc][/bold] 
3. Delete an Alarm              [bold][#0349fc]{mem_str}[/#0349fc][/bold]  
4. Show Alarm              [bold][#0349fc]{disk_str}[/#0349fc][/bold]       
5. Monetoring 
6. Exit
""","""[#fc035a]=== Main Menu ===[/#fc035a]""", "[#fc035a]↓↓↓↓↓↓[/#fc035a]")
        
        time.sleep(1)
        alarm_manager = AlarmManager()
        # refresh every second
        menu_input = console.input(Align("[#fc035a]what is your choice[/#fc035a]", align="center")).strip().lower()
        match menu_input:
            case "1":               
                pass # idk what this is supposed to do
                # time.sleep(5)
            case "2":
                console_cleaner()
                #print(f"CPU Usage: {cpu}%")
                pass
            case "3":
                pass
            case "4":
                alarm_manager.show_alarms()
                press_to_continue()
            case "5":
                pass
            case "6":
                quit()
            case _:
                pass
        # 🟢 Start the program
main()
