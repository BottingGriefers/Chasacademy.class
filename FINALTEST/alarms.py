from design import *
from rich.console import Console
from rich.align import Align
console = Console()
class AlarmManager: 
    '''How does a class work? with init its like a personal notebook to AlarmManager so whatever is within it can be destrubuted and saved on onther fucntions '''
    def __init__(self):  
        self.alarms = {"cpu": [], "memory": [], "disk": []} # this is a dict that gives each object its own storage, so we can use it for showing object and having the doing smth

        

    def show_alarm_menu(self,):
    #Display the options for configuring alarms.
        border(
        f"1. CPU usage\n"
        "2. Memory usage\n"
        "3. Disk usage\n"
        "4. Back to main menu", "===Configure Alarms===", "[#00FFDD]↓↓↓↓↓↓[/#00FFDD]"
        )

    def add_alarm(self, hardware_type: str, level: int):
        if hardware_type not in self.alarms:
            print(f"Unknown hardware type: {hardware_type}")
            return
        if not (1 <= level <= 100):
            print("Alarm level must be between 1 and 100")
            return
        self.alarms[hardware_type].append(level)
        print(f"Added {hardware_type} alarm at {level}%")


    def show_alarms(self):
        for hardware, levels in self.alarms.items():
            if levels:
                for lvl in levels:
                    print(f"{hardware.capitalize()} larm: {lvl}%")
            else:
                print(f"{hardware.capitalize()} larm: --")
                
        # show all alarms
    def menu_input_choice(self):
        choice = console.input(Align("[#ffffff]what is your choice[/#ffffff]", align="center")).strip().lower()
        if choice == "1":
            hardware = "cpu"
        elif choice == "2":
            hardware = "memory"
        elif choice == "3":
            hardware = "disk"
        elif choice == "4":
            print("Returning to the main menu. No alarm created.")
            hardware = None
        else:
            print("Invalid choice. Please restart the program and choose 1-4.")
            hardware = None
        if hardware:  # only continue if a valid hardware type was chosen
            border(f"Now type the percentage for the {hardware} alarm (1-100):")
            level_input = console.input("[#44C264]> [/#44C264]")
            if level_input.isdigit() and 1 <= int(level_input) <= 100:
                level = int(level_input)
                alarm_manager.add_alarm(hardware, level)
                print(f"You have successfully set an alarm for {hardware} at {level}%")
            else:
                print("That is not a valid number between 1 and 100. No alarm created.")
        return









alarm_manager = AlarmManager()


