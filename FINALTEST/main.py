import time
from alarms import *
from design import *
from monitor import *
import os
import logging
if os.name == "nt":
    import winsound
    import msvcrt
else:
    import select
    import termios
    import tty
    import sys

from datetime import datetime


def enter_pressed():
    # Return True if Enter
    if os.name == "nt":
        if msvcrt.kbhit():
            return msvcrt.getch() == b"\r"
        return False
    else:
        # Linux/macOS version
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            # Switch terminal to raw mode temporarily
            old_settings = termios.tcgetattr(sys.stdin)
            try:
                tty.setcbreak(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                return ch == "\n"
            finally:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
        return False


def getlivestats(stats): # Monitoring 
    while True:
        cpu_str, mem_str, disk_str = stats.get_system_info() # Retrieve system stats
        console_cleaner()# Clear the console
        border( #A design function from design.py 
            f"[bold][#ffffff]{cpu_str}\n{mem_str}\n{disk_str}\n[/#ffffff][/bold]",
            "[bold][#fc035a]=== Monetoring Live ===[/#fc035a][/bold]",
            "[#fc035a][bold]Press Enter to stop monitoring...[/#fc035a][/bold]",
        )
        alarm_manager.check_alarms(stats)
        logging.basicConfig(level=logging.WARNING, filename='app.log',filemode="w") 
        logging.warning(f"CPU: {cpu_str}, Memory: {mem_str}, Disk: {disk_str} | {get_local_date()} ")
        if enter_pressed():
            break
        time.sleep(1.5)

def get_local_date():
    return datetime.now().strftime("%d/%m/%Y")
def get_local_time():
    return datetime.now().strftime("%H:%M")


def press_to_continue():
    while True:

        press = console.input(
            Align(
                "[#fc035a][bold]Press Enter to continue[/#fc035a][/bold]",
                align="center",
            )
        )
        if press == "":  # empty string means Enter was pressed
            break
        else:
            console_cleaner()
            console.print(
                Align(
                    "[#fc035a][bold]Just press Enter, you buffoon \n[/#fc035a][/bold]",
                    align="center",
                )
            )


def console_cleaner():
    os.system("cls" if os.name == "nt" else "clear")



runprogram = console.input("Do you want to run the program? Y To confirm: or press anything else to Exit\n").strip().upper()
if runprogram == "Y":
    runprogram = True
    def main():
        while True:
# fix functions in main / comment hard stuff
                stats = SystemStats()

                cpu_str, mem_str, disk_str = stats.get_system_info()
                console_cleaner()  # clear the screen each second

                border(
                    f"""
        1. Monitoring System            [#0349fc][bold]Current time: {get_local_time()}[/#0349fc][/bold] 
        2. Create an Alarm              [bold][#0349fc]{cpu_str}[/#0349fc][/bold] 
        3. Delete an Alarm              [bold][#0349fc]{mem_str}[/#0349fc][/bold]  
        4. Show Alarm                   [bold][#0349fc]{disk_str}[/#0349fc][/bold]       
        5. Monetoring Live
        6. Exit
        """,
                    """[bold][#fc035a]=== Main Menu ===[/#fc035a][/bold]""",
                    "[#fc035a][bold]↓↓↓↓↓↓[/bold][/#fc035a]",
                )

                menu_input = (
                    console.input(
                        Align(
                            "[#fc035a][bold]what is your choice[/#fc035a][/bold]",
                            align="center",
                        )
                    )
                    .strip()
                    .lower()
                )
                match menu_input:
                    case "1":
                        console_cleaner()
                        border(
                            f"[bold][#ffffff]{cpu_str}[/#ffffff][/bold]\n[bold][#ffffff]{mem_str}[/#ffffff][/bold] \n[bold][#ffffff]{disk_str}[/#ffffff][/bold]\n",
                            "[#fc035a]=== Monitoring System ===[/#fc035a]",
                        )
                        press_to_continue()

                    case "2":

                        alarm_manager.show_alarm_menu()
                        alarm_manager.menu_input_choice()

                        press_to_continue()
                    case "3":
                        alarm_manager.delete_alarm_menu()
                        press_to_continue()
                    case "4":

                        alarm_manager.show_alarms()
                        press_to_continue()
                    case "5":
                        getlivestats(stats)

                    case "6":
                        quit()
                    case _:
                        pass
    main()
else: 
    quit()
