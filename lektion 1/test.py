
#du måste definera argument inom print menu () med en variabel och definera dem också
def print_menu(menu_choice_number, message_string):
    #check är en variabel som är en boolean, så den kollar om det finns 1,2,3 om det finns så checkar den om det är true

    check = int(menu_choice_number) in [1, 2, 3]
    if not check: 
        print("invalid choice")     #check är mer kontrollerad den kollar om det valet som user valde är True, om inte då är den false och den gör print("invalid chice") eller not True
        return 
    print(f"You have selected option {menu_choice_number}. {message_string}" )# i menu choice number det kommer bakas in svaret man trycker pa




# app_is_running är variabel som man kan nämna vad som helst
# men det är viktigt att nämna det så man förstår
app_is_running = True 
                     

while app_is_running: # == kollar om det är sant eller falskt, så om app_is_running = False och while app_is_running == True kommer den inte köras, men man kan köra utan == True
                              
    menu_choice = input("enter a choice (1-3) 3 to quit ")

    message_string = "you have selected option"
  

    if menu_choice == '1':
          message_string += f"{menu_choice}. FOODS"
       # print_menu(int(menu_choice), "Food") #print_menu(1, "Food")
    elif menu_choice == "2":
          message_string += f"{menu_choice}. DRINKS"
       # print_menu(int(menu_choice), "Drink") #print_menu(2, "Drink")   #sluta hårdkoda och skriv vad som är sant att "menu_choice är det som är vald"
    elif menu_choice == "3":
        message_string += f"{menu_choice}. QUITS"
        #print_menu(int(menu_choice), "EXIT") #print_menu(3, "EXIT")     # Int är bara definerad för att göra koden mer niche men det behövs inte i python

       # app_is_running = False du kan andvända quit() och exit() men app_is_running = false gör att du går ut i lopen bara
        break #break också går ut i lopen men när men det andvänds när man inte definerar variablar 
    else:
        print("invalid choice")

        menu_choice = input("Enter A choice again ") #THIS loops THE LOOP det finns olika sätt att göra det på men vi andvände oss av denhär,
        #continue kan också andvändas för att Loopa loopen                                               #Testa ta bort den och tryck på option 1 eller 2 

print("program exited")

#scope i programering är vad den känner till för variabel i olika delar av programmet?
#göra lite research på scope i programmering 
# !=, ==, not True, not False, True, False, det är samma sak men olika sätt att säga dem
# Det finns lokala och inte lokala funktioner eller variablar det betyder allt som är inom en annan parent eller säga en funktion blir lokala. ALLT SOM ÄR UTANFÖR ÄR GLOBALT


#Slutsatsen är skriv koden så att den är automatiskt förstådd av andra och digsjälv, utan att kommentera. Andvänd inte onödig kod som gör att det runnar mer onödiga saker istället bara definera dem och ha en bra struktur 