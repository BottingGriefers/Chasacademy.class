'''class Person():

    def __init__(self, name, age): # man måste alltid skriva self i en objekt metod
        self.name = name # det kan ha olika namn men ska ha egentligen samma som i self, name
        self.age = age

    def greet(self):
        print(f"HI, my name is {self.name} and i am {self.age}")

p2 = Person("bert", 90)

p1 = Person("Calle", 21)

p1.greet()
p2.greet()

person_list = [p1,p2,p3]
min_andra_lista = list(x for x in range (1,11)) # list constructor den listar allt mellan det man skriver in, vilket gör det lättare

# skriver man bara objectet så kommer det ett problem eller en error men det problemet säger vart det objektet är lokerat i minnet 
def __str__(self):
    return f"Name: {self.name}  | Age: {self.age}"

for i in range(len(person_list)): #loop som ger oss från 0 upp till x altså så många det finns i person_list
    print(person_list[i])

def get_name(self):
    return self.name
def change_name(self, new_name):
    self.name = new_name
print(f"{p1.name}")

new_name = input(f"New name for {p1.get_name}")
p1.change_name(new_name)


#Dunnder method'''