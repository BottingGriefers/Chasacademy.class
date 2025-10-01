
# Lista som sparar all input som görs vid rad 1 
studentslist = [] 
# Här görs den att den is running True
killerapp = True
while killerapp:
    # här visar den första menyn och vad allt gör 
    menu = input("This is a menu \n Press 1. add students \n Press 2. list a student \n Press 3. Search for a student \n Press 4. Calculate their age \n Press 5. to exit \n")
    #if menu är när du väl trycker 1 så kommer du in till den delen av programmet som har dictionary lista inuti sig 
    if menu == "1": 
        students = { #varför en dictionary? jo för att uppgiften sa du ska visa var i listan det Fanns namn och older
            "Name": input("What are you called?: "),
            "Age": int(input("How many years have you lived?: "))}
        studentslist.append(students) # vi andvänder oss av append för att lägga till nya studenter inom listan med deras nya dictionary
        print("Thank you for adding yourself to the database ")
    elif menu == "2": #här skriver den ut eleverna vilka som finns i en lista och dictionary 
        print(f"Here are the names of our students {studentslist} ")
    elif menu == "3": #här hade jag lite roligt, när man lägger till studenter så efter åt kan man eliminera dem vilket görs att det försvinner från listan
        find_student = input("Enter whom you want to eliminate!!!: ")
        for students in studentslist: # namnet man uppger, inom students som är i studentslist försvinner hen 
            if students["Name"] == find_student:
                print(f"sending warthog towards {students} \n ")
                confirmation = input("Confirm the strike Y/N: \n ").lower() #här får du confirmation om du vill göra det .lower står för att man inte ska skriva stora bokstäver för det kmr göra error 
                if confirmation == "y": 
                    studentslist.remove(students) #här den studenten försvinner
                    print("Target is no longer with us \n ")
                    break
                elif confirmation == "n":
                    print("You wussy \n" )
                    break #forsome reason i had to use break instead of continue idk why but that fixed my problem which printed student was never here  tho it wasnt true the line on 32
            else:
                print("student was never here \n") #om det inte finns en student så kommer denna else
    elif menu == "4": 
        total_age = 0 #här är den totala summan av åldrarna av elever i början av kalkulationen 
        avrage = len(studentslist)  # avrage variabel letar hela "len(studentslist)" len står för allting i listan 
        for elever in studentslist: #här är själva matten du tar alla elevers ålder plussar ihop dem och dividerar med hur många elever
            total_age = total_age + elever["Age"]

        if avrage > 0: # om avrage är mer än 0 så printas det ett svar 
            avrage_age = total_age / avrage
            print(f" the avrage age of the class is {avrage_age}" )
        else:
            print("you got no students" )
            
         #matten var jobbig 

    elif menu == "5":
        print("Program exited")
        killerapp = False

