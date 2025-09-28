# Def gör att det blir till en funktion som är definerad som print_menu (som jag förstår) och det visar up själva början av programmet 

#   menu_choice_number: När andvändaren skriver ett numer så sparas det in i denna variabeln 
#   message_string: säger you have chosen {menu_choice_number}
def print_menu(menu_choice_number, message_string):
    print(f"You have selected option {menu_choice_number}. {message_string}") # det är en function som definerar vad menu_choice_numer är och message_string

# den delen säger att du faktiskt kör koden "True gör att den körs "
menu_is_running = True


# volume = ""

# När while står så är det en loop vilken gör att du kan göra olika val och den typ reagerar på dina val????????????????
while menu_is_running:
    # Visar menyn valen för den som runnar koden
    menu_choice = input("Enter A choice 1, 2, 3. 4 to exit ")

    # När du skriver 1 så säger den du har valt ett darför står det if. Om if är 1 så skriver den "you have selected option 1. TV settings"
    if menu_choice == "1":
        print_menu(menu_choice, "TV Settings")

    # Menu 2 visar den att du har valt 2an's meny och skriver typ samma sak. elif är när det är många if functioner i en så skriver man (else if) eller elif
    elif menu_choice == "2":
        print_menu(menu_choice, "Choose Channel")
       

    # Menu 3 väljer du 3 valet och där går den in djupare i programmet
    elif menu_choice == "3":
       
        valid_volume = False  # här startar den falsk för att göra att när andvändaren skriver något så blir den True?????
        volume = 0
        # Volume mixare, här när volymen är inte  valid_volume så printar den??????????? det är också en loop inuti en loop
        while not valid_volume:
            # här visar den volymen andvändaren la till
            print(f"Volume is {volume}")
            print_menu(menu_choice, "Change Volume")
            
            # här frågar den om en ny volym som andvändaren ska skriva in MEN också la vi till att hen kan länma den while loopen av programmet
            new_volume = input("Set Volume 1-100. Enter E to exit ")
            
            # här är själva lämnings koden
            if new_volume == "e":
                print("returning to main menu... \n")
                break  # break lägger man till så att det går tillbaka till första loopen
            
            # eftersom volym kan bara bara ett nummer så måste vi verifiera det med en int att bara acceptera det
            elif 0 <= int(new_volume) <= 100:
                # när andändaren skriver en valid nummer så printar den in det och skriver nya volymen
                volume = int(new_volume)
                print(f"Volume set to {volume}")
                valid_volume = True  # sen lämnar den programmet med valid_volume = True istället för false som i början
            
            # här jag vet inte vas som pågår3
            else:
                print("Volume must be between 0-100")
                continue  

    # Menu 4 lämnar du programmet 
    elif menu_choice == "4":
        print(menu_choice, "You have chosen to exit")
        menu_is_running = False  # du kan lägga också break, quit, eller exit för att ha samma effect

    # här hanterar den info som är invalid
    else:
        print("Invalid choice")