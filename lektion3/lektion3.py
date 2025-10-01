def say_hello(user_name, extra_message=""):
    print(f"Hello user {user_name} - {extra_message}")

def get_name_length(name):
    length = len(name)
    return length

name = input("you name: ")
name1 = "Calle"

say_hello(name1," Vad fin du är")
len1 = get_name_length(name1)
print(f"Length of name {name1} is {len1}")

name2 = "Bob"
say_hello(name2," Vad fin du är")
len2 = get_name_length(name2)
print(f"Length of name {name2} is {len2}")

say_hello(name, "you are smart")
len3 = get_name_length(name)
print(f"Lenght of {name} is {len3}")

#isalpha är en inbyggd function i python som gör att den validerar om det som skrivs är bara alphabetiska bokstäver, så inga siffror!
#Varför en funktion andvänds
'''/////
Det är återandvändbar, du kan lätta andvända samma funktion i många ställen, och om du vill byta en bit av koden så gör du bara funktionen och det gör saker snabbare

för det ska funka måste du definera innan du andvänder vilekt är logiskt ändå

det gör koden mer struktur och läsbarhet, FÖR ANDRA KODARE vilket är viktigt i branchen

det ska vara minde upprepningar så man själv inte blir för trött och det är snabbare läst

standarden ska vara att while loopen ska ha så lite saker som möjligt i den så definera allt du behöver, ännu en bättre practice är att ha 
defenitioner i en annan fil och importera i main koden (from ........ import (functions variabel))

vi kommer behöva baka in vår huvud logic i main programmet för vårt "student" project

man andvänder #def main(): och i slutet av koden main() för att köra programmet 

problemet vi hade var att vi kör en string med " men i mitten av stingen kan vi inte lägga " igen för då avslutas stränger "" det ska se ut såhär då (f"Något random som du vill skriva ['exempel']" )
se vi la till ' ' inuti en " " då funkar det

https://github.com/CalleFreme/DOE25-Python-Calle 

vad jag behöver göra och 

 project/
        Tasks/
            main.py
            helper_functions.py
        README.md
////'''


