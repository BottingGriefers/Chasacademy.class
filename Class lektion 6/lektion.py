import random
import os
from datetime import datetime

def main():
    input= "students.txt"
    output = "student_pairs.txt"

    print("student pairing")

def read_student(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file: # "r" står för read och utf är ibland ett måste för att programmet ska vara compatibil med standarden OCH file: är en variabel
            ''' lines = file.readlines()for line in lines:
                for line in liens:
                    line = line.strip(#man kan spcifiera vad den tar bort from raden )
                    if line: #handles empty lines
                     students.append(line) denna for loopen is another way of doing it'''
            students = [line.strip() for line in file if line.strip()]  # a lines is a list of strings vi go to a list with \n for better readability || LIST comprehension
    except:
        pass

def create_pairs(students):
    student_list = students.copy() #copy gör vi får en likadan lista men inte samma pga det är nestad inutti en functions???? ksk
    random.shuffle(student_list)
    pairs = []
    #skapar en shuffeled list
    for i in range(0, len(student_list), 2):
        if i + 1 < len(student_list):
            pairs.append((student_list[i], student_list[i + 1])) #pair is a tuple och en tuple is a list that is unmodifiable
        else:
            pairs.append((student_list[i], "no partner"))
for i, (student1, student2) in enumerate(pairs, 1):
    print(f"Pair {i:2d}: {student1:<15} - {student2}")

#range listar number från 1 till len(students)
#for i in range(len(students)):

#enumerate gives both index and value
#for i, student in enumerate(students, 1):
             
'''
Numbers_list [x for x in range(10)]
is the same as 
for x in x range(10)
    x'''