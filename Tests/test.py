import pytest
#imprt your testing envoirment '


def test_init(self):
    transaction = Transaction("e", 500, "food") #om den funkar körs den ner i exxpected = 
    expected = "2023-10-15 food: 500" #då testar expected
#det är bra att göra ny functioner FÖR FARJE test som är olika, så olika saker måste ha olika def...() 

#hur testas det i git hub actions???

'''
man ska skriva tester innan man skriver koden, för att göra det måste man plannera vad du vill göra, det är en skill att lära sig
först ska du bli tydlig med ditt mål, och ha en ritning i ungefär riktning vad du vill, 
det finns ett separat test man gör för github actions 
jobs:
    test:
        runs-on: ubuntu-latest
        strategy: m.m det koden som finns i pipelines är olika från 

'''