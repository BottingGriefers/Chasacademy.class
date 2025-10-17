import os
import time
import json
from datetime import datetime

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else "clear")

def confirmation_to_continue():
    while True:
        c = input("Press C to continue: ").upper()
        if c == "C":
            return
        else: 
            print("You have entered the wrong input. Please press C.")
    

StudentList = []
StudentReg = True

def menu():
    width = 36
    menulist = ["1. Add Student", "2. List Student", "3. Search Student", "4. Delete Student", "5. Exit"]
    screen_cleaner()
    print("+" + "-" * (width) + "+")
    print("|" + "- Welcome to the Student Registry -".center(width) + "|")
    print("+" + "-" * (width) + "+")
    for decoration in menulist:
        print ("|" + decoration.center(width) + "|")
    print("+" + "-" * (width) + "+")

while StudentReg:
    menu()
    choice = input("")
    if choice == "1":
        studentname = input("Enter The Student's Name: ").capitalize()
        while True:
            try:
                studentage = int(input("Enter The Student's Age: "))
                if studentage >= 100:
                    print("You cannot be that old buddy")
                else:
                    break
            except ValueError:
                print("Please enter a valid number for age.")
        print(F"You have succefully added {studentname} and their age is {studentage}\n")
        student_data = {
            'name': studentname,
            'age': studentage}
        StudentList.append(student_data)
        confirmation_to_continue()

    elif choice == "2":
        if not StudentList:
            print("You got no students here")
        else:
            for i, student in enumerate(StudentList, 1):
                    print(f"{i}. Name: {student['name']}, Age: {student['age']}") ###{student['name']} fix this with teacher ?? cuz you cant  have no students 
            print(f"\nThere are {len(StudentList)} students in total.\n")
            confirmation_to_continue() 

    elif choice == "3":
        studentsearch = input("Who are you looking for? ").capitalize()
        for students in StudentList:
            if students ["name"] == studentsearch:
                print(f"you have found {studentsearch}") 
        confirmation_to_continue() 

    elif choice == "4":
        studentsearch = input("Who are you looking for? ").capitalize()
        for students in StudentList:
            if students ["name"] == studentsearch:
                StudentList.remove(students)
        print(f"You have removed {studentsearch}")
        confirmation_to_continue()

    elif choice == "5":
        print("You have exited the program \nhave a wonderful day")
        time.sleep(1)
        screen_cleaner()
        break

    else:
        print("Wrong choice enter through 1 to 5 \n")
        confirmation_to_continue()

    
    

      