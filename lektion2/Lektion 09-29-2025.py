"""""
import time
username = input("Username: ")
# while True:
   # counter += 1 #Den plussar counter så den plusar sigsjälv 
    
counter2 = 0
repetitions = int(input("how many repetitions? "))
while counter2 < repetitions: # av någon anledning om du skriver <= så blir mer 
    print(f"Hi, {username} , counter valve: {counter2 + 1} ") # man skriver counter + 1 för att göra att det ser andvändar vänligt ut 
    counter2 += 1
    time.sleep(1)

    print("loop over")
    


pers1 = "calle"
pers2 = "adam" 
pers3 = "anna"
List = [pers1, pers2, pers3]
for user in List:
    print(user) # det skriver ut listan utan []

#skriv hur det står under för de blir onödigt att skriva variablar för ett lista 
# list ["Calle", "Adam", "anna"]
#När man plockar ut saker ur listan andvänder man sig av [index] så exempel [1] eller [2] eller [3] mm beror på din lista storlek

for element in List:
    time.sleep(2)
    print(element)
#när man skriver  i början och slutet av koden då kommenteras hela detta området

for i in range(int(1)): # istället för i kan man andvända J k och anndra, men bara när det är nestade innuti andra indexes.
    for j in range(3): #det här är en nester for loop med en variabel j
        print(f"printing {i} #{j}") # f string must be put even tho you have the {}
#efter the program ends it will keep looping back to "for i in range"

#en lista som görsa kan vara one dimention eller 2 dimention vilket gör att du kan göra en lista innuti en lista och det, strukturerar det bättre 

user1 = ["calle", "2323", 'lilgatan']
user2 = ["peter", "123", "Storgatan"]
user3 = ["bob", "12322222", "trumpetvagen"]

user_data = [user1, user2, user3]

for user in user_data:
    for data in user:
#så varje element i listan kan man gå igenom en lista
        time.sleep(0.2) # this is just so it doesnt print everything at once, and has a nice gap between outputs
        print(data, end=" /// ") # end skriver ut vad som kommer i slutet av ett element, det andvänds för att strukturera och see bättre
    print()




/////////////////////////////////////////////////Lektion 2////////////////////////////////////////////////////////////// 


#array is a list but not changeable and more niche 

user1 = ["calle", "2323", 'lilgatan']
user2 = ["peter", "123", "Storgatan"]
user3 = ["bob", "12322222", "trumpetvagen"]

user_data = [user1,user2,user3]




while True:
    add_new_user = input("Do you want to add a new user? Y/N: ")
    if add_new_user.upper() == "Y" or add_new_user.lower() == "yes": # == gämnför add new user som blir inputen med Y. och .upper behövs för att göra det mer vänligt för andvändaren det gör bokstaven stor automatiskt
        new_user_name = input("New Name: ")
        new_personnmr = input("personnummer: ")
        new_adress = input("New Adress: ")
        new_user = [new_user_name, new_personnmr, new_adress] # samlar all information till en variabel new_user
        user_data.append(new_user) #lägger till andvändaresns input in i det existerande lista
    elif add_new_user.upper() == "N":
        break
    else: 
        print("wrong Input")
        
for user in user_data:
    for user_info in user:
        print(user_info, end=" / ")
    

def say_hello(user_name, message=""): # det är en typ av functioner som har en lsita som du kan göra så att det gör något, som här user_name är först i listan, dem är också baralokal kända 
                #name
    print(f"hello kitty {user_name} - {message}") #och vi vill att det ska stå hello kitty och user_name
                        #prints name

    name_length = len(user_name)
    return name_length# ger resultat tillbaka, Jag förstår inte riktigt hur det funkar????


name = input("your name: ") #här skriver vi en variabel name
#is a variable name

len1 = say_hello(name)
print(f"Lenght {len1}") 
        #user_name function inside name
# här skriver vi in functionen och lägger variabel i första definition funktionen (user_name) 
# YOU MUST ALWAYS END WITH () ALSO IT HAS TO BE OUTSIDE THE def

"""
"""
/////////////////////////////////////////////////Lektion 3////////////////////////////////////////////////////////////// 
"""

#innan du kodar försök planera steg för steg vad du vill gör, sen ändra och gör mer flexibila ändringar när du har startat igång
# 1. Data struktur
# 2. loop för menyn
# 3. vad ska menyn ha? 
test_student = {"name": "Adam", "age": "21"}
student_list = [test_student] #first problem solved 

max_no_students_to_print = 10

Menyrun = True
print("Welcome user! ")
while Menyrun:
    print("-------MENU-------")
    print("1. Add a student")
    print("2. List students")
    print("3. Quit program")

    menuchoice = input("Choose 1-3: ")
    if menuchoice == "1":
        # pass andvänds för att skippa den delen av koden men forstätta med den andra koden så den är mest andvänd för programeraren inte för user
        new_student_name = input("New student name: ")
        new_student_age = input("New student age: ")
        new_student_dict = {"name": new_student_name, "age": new_student_age} # you can chose a Name for the data you want to keep, by doing name: or age: or anything else
        print("Student was added")
        print(f"Name: {new_student_dict['name']}")
        print(f"age: {new_student_dict['age']}")
    elif menuchoice == "2": 
        print(student_list)
        break
    elif menuchoice == "3":
        pass
    else:
        print("choice is not valid")


