from design import *
from rich.console import Console
from rich.align import Align
from monitor import *
if os.name == "nt":
    import winsound
else:
    winsound = None
import tkinter as tk
console = Console()
getstats = SystemStats()


class AlarmManager:
    """How does a class work? with init its like a personal notebook to AlarmManager so whatever is within it can be destrubuted and saved on onther fucntions"""

    def __init__(self):
        self.alarms = {
            "cpu": [],
            "memory": [],
            "disk": [],
        }  
         # this is a dict that gives each object its own storage, so we can use it for showing object and having the doing smth

    def show_alarm_menu(self):
        # Display the options for configuring alarms.
        border(
            "1. CPU usage\n"
            "2. Memory usage\n"
            "3. Disk usage\n"
            "4. Back to main menu",
            "[bold][#fc035a]=== Create an Alarm ===[/#fc035a][/bold]",
            "[#fc035a][bold]↓↓↓↓↓↓[/bold][/#fc035a]",
        )
        return
    
    def critical_alert(self, message):
        root = tk.Tk()
        root.attributes("-fullscreen", True)  # full-screen window
        root.attributes("-topmost", True)
        root.configure(bg="#000000")  # background color

        # Add a centered message
        label = tk.Label(
            root, text=message, font=("Arial", 48, "bold"), fg="red", bg="#000000"
        )
        label.pack(expand=True)

        root.after(2000, root.destroy)
        root.mainloop() 


    # This is the one that delets a specific alarm(thanks chatgpt)
    def delete_alarm(self, hardware_type):

        if hardware_type not in self.alarms:
            console.print(f"Unknown hardware type: {hardware_type}")
            return

        self.alarms[hardware_type] = []  # empty the list
        console.print(
            Align(
                f"[#03fc62][bold]All alarms for {hardware_type} have been removed.[/#03fc62][/bold]",
                align="center",
            )
        )

    def delete_alarm_menu(self):
        delete_input = console.input(
            Align(
                "[#fc035a][bold]Which alarm would you like to delete[/#fc035a]\n[#ffffff]| 1. CPU | 2. Memory | 3. Disk |[#ffffff][/bold]",
                align="center",
            )
        )
        # we use map to make a choice based on numbers and not a whole text
        choice_map = {"1": "cpu", "2": "memory", "3": "disk"}
        hardware_type = choice_map.get(delete_input)

        if hardware_type:
            alarm_manager.delete_alarm(hardware_type)
        else:
            console.input(
                Align(
                    f"[#fc035a][bold]Invalid choice, no alarms deleted. {hardware_type}[/#fc035a][/bold]\n",
                    align="center",
                )
            )
            console.print()

    def add_alarm(self, hardware_type, level):
        """Add an alarm threshold for CPU, memory, or disk."""
        if hardware_type not in self.alarms:
            console.input(
                Align(
                    f"[#fc035a][bold]Unknown type: {hardware_type}[/#fc035a]\n[#ffffff]| 1. CPU | 2. Memory | 3. Disk |[#ffffff][/bold]",
                    align="center",
                )
            )
            return

            # this says if no hardware found it will return but if it finds you can continue and get a choice between 1 and 100, the usage of not can be changed idk.
        if not (1 <= level <= 100):
            console.print(
                Align(
                    "[#fc035a][bold]Level must be between 1 and 100%[/#fc035a][/bold",
                    align="center",
                )
            )
            return

        # this appends it to the library
        self.alarms[hardware_type].append(level)
        console.print(
            Align(
                f"[#03fc62][bold] Added alarm for[/#03fc62][/bold] [bold][#0349fc]{hardware_type} [/bold][/#0349fc][#03fc62][bold]at[/#03fc62][/bold] [bold][#0349fc]{level}[/bold][#/0349fc][#03fc62][bold]%[/#03fc62][/bold]\n",
                align="center",
            )
        )

        # there is a .join functions which i maybe should try

    def show_alarms(self):

        for hardware, levels in self.alarms.items():
            if levels:
                for lvl in sorted(levels):
                    console.print(
                        Align(
                            f"[bold][#0349fc]{hardware.capitalize()} alarm: [/bold][/#0349fc][#fc035a][bold]{lvl}%[/#fc035a][/bold]",
                            align="center",
                        )
                    )
            else:
                console.print(
                    Align(
                        f"[bold][#0349fc]{hardware.capitalize()} alarm: [/bold][/#0349fc][#fc035a][bold]\-/[/#fc035a][/bold]",
                        align="center".strip()
                    )
                )
        # show all alarms

    def menu_input_choice(self):
        while True:

            choice = (
                console.input(
                    Align(
                        "[#fc035a][bold]what is your choice[/#fc035a][/bold]",
                        align="center",
                    )
                )
                .strip()
            )
            try:
                choice = str(int(choice))  # Ensure choice is a string of an integer
                if choice == "1":
                    hardware = "cpu"
                elif choice == "2":
                    hardware = "memory"
                elif choice == "3":
                    hardware = "disk"
                elif choice == "4":
                    console.print(
                        Align(
                            f"[#ffffff][bold]Returning to the main menu.[/bold][/#ffffff]",
                            align="center",
                        )
                    )
                else:
                    console.print(
                        Align(
                            f"[#ffffff][bold]Invalid choice. Please restart the program and choose 1-4.\n[/bold][/#ffffff]",
                            align="center",
                        )
                    )
                    break
            except ValueError:
                console.print(
                    Align(
                        f"[#ffffff][bold]Invalid input. Please enter a number between 1 and 4.[/bold][/#ffffff]",
                        align="center",
                    )
                )
                continue

            while True:
                if hardware:  # only continue if a valid hardware type was chosen
                    level_input = (
                        console.input(
                            Align(
                                f"[#fc035a] [bold]Now type the percentage for the {hardware} alarm (1-100):[/#fc035a][/bold]",
                                align="center",
                            )
                        )
                       
                        .lower()
                    )
                    if level_input.isdigit() and 1 <= int(level_input) <= 100:
                        level = int(level_input)
                        alarm_manager.add_alarm(hardware, level)
                    else:
                        console.print(
                            Align(
                                f"[#ffffff][bold]That is not a valid number between 1 and 100. No alarm created.[/bold][/#ffffff]",
                                align="center",
                            )
                        )
                        continue
                return

    def custom_alarm_sound(self):
        # Rising pitch alarm
        try:
            for freq in range(100, 500, 15):  # 500 Hz to 1500 Hz
                winsound.Beep(freq, 30)  # 100 ms per tone
            for freq in range(400, 500, -330):  # back down
                winsound.Beep(freq, 30)
        except:
            None
    def check_alarms(self, stats):

        cpu, mem, disk = stats.get_raw_stats()

        alerts = []

        for level in self.alarms["cpu"]:
            if cpu > level:
                alerts.append(f"CPU usage {cpu}% > {level}%")

        for level in self.alarms["memory"]:
            if mem > level:
                alerts.append(f"Memory usage {mem}% > {level}%")

        for level in self.alarms["disk"]:
            if disk > level:
                alerts.append(f"Disk usage {disk}% > {level}%")

        if alerts:
            console.print(
                Align(
                    "[#fc035a][bold]===ALARM TRIGGERED!===[/bold][/#fc035a]\n",
                    align="center",
                )
            )
            for msg in alerts:
                console.print(Align(f"[#fc035a]{msg}[/#fc035a]", align="center"))
            alarm_manager.custom_alarm_sound()
            alarm_manager.critical_alert(
                "WARNING! CRITICAL ALERT! CHECK SYSTEM USAGE!\n AND LOVE YOUR COMPUTER! :)"
            )


alarm_manager = AlarmManager()
