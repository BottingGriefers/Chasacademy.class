import random

class Student:

    def __init__(self, name, points):
        self.name = name
        self.points = points

#s1 = Student("Calle", 45)
#s2 = Student("Adam", 65)
#s3 = Student("Rapunsel", 20)
no_student = int(input("how many students? "))
student_list = []
for i in range(no_student):
    student_name = "student" + str(i+1)
    student_points = random.randint(0, 100)
    student = Student(student_name, student_points)
    student_list.append(student)

random_student_idx = random.randint(0, no_student-1)
print(random_student_idx)


# student_list = [Student("Calle", 45), Student("Adam", 53)]
