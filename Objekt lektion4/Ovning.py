'''
class Car():
    def brand(self, brand):
        self.brand = brand
        
        return
        

    def speed(self, accelerate, brake):
        self.accelerate = accelerate
        self.brake = brake
        accelerate = 10
        brake = -10
        return
    
brand1 = Car("Bmw")
brand2 = Car("Mazda")
Speed1 = 



class Car:
    def __init__(self, brand, speed=0): # om det står två parametrar ska det skrivas i koden två parametrar 
        self.speed = speed
        self.brand = brand
    
        
    def __str__(self):
        return f"brand: {self.brand}, Speed={self.speed}

    def accelerate(self):
        
        self.speed += 10
    
    def brake(self):
        if (self.speed <= 0):
            return 0
        else:
            self.speed -= 10
            return self.speed
        self.brake += -10


car1 = Car("Volvo")
Car1.accelerate
car2 = Car("Audi", 100)
'''

class Student:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, x):
        self.points += x

    def has_passed(self):
        if self.points >= 50:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"Name: {self.name}, Points: {self.points}"
    

students1 = Student("Bert", 80)
students2 = Student("Bob", 48)
students3 = Student("Kebab", 99)
students4 = Student("Anna", 21)

students1.add_points(20)
students2.add_points(1)
students3.add_points(0)
students4.add_points(1)

students1.has_passed()
students2.has_passed()
students3.has_passed()
students4.has_passed()

students1input = int(input("skriv in hans betyg"))
students1input += students1.add_points

studentlist = [students1, students2, students3, students4]
for student in studentlist:
    passed = "You have passed buddy" if student.has_passed() else "you shall not pass"
    
    print(f"{passed} - {student}")

