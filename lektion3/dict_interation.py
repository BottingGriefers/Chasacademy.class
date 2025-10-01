int_list = [1, 5, 3] # [ Creates a list]
        #  0   1  2
for element in int_list:
    print(element)

d = {"Alice": 25, "Bob": 30}
    # KEY    VALUE: KEY   VALUE

print(d["Alice"]) # Key is Alice valuve would be 25

print(d["Bob"]) # Key is Bob  valuve would be 30



for key in d:
    print(key) # this creates a loop, i think?

print() #empty print for decorative purposes 

for value in d.values(): # .values prints a list with values such as the int 25 and 30
    print(value)

print() #empty print

# approach 1
for key, value in d.items(): #this creates an pair value and keys in an nice order
    print("Key: ", key)
    print("Values: ", value)


name = input("enter your name ")
age = d.get(name, "No key buddy") #dictinary har en inbyggt feature som är .get. vrf vi gjorde det är så programmed inte crashar
print(age)

#approahc 2
if name in d: 
    print(d[name])
else:
    print(f"Key {name} doesnt exist in dict")

#approach 3
while True: #idk if this is a must have
    try:# alla try must have except in the end
        print(d[name]) #
    except:
        print(F"print {name} not here")
        name = input("a new name ")

if __name__ == "__main__":