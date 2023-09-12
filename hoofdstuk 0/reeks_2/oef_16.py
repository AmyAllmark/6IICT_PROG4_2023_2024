import random
""" Vraag de gebruiker naar een cijfer.
    Genereer een willekeurig getal tussen 1 & cijfer.

    Vraag de gebruiker naar een tweede cijfer. 
    Print het verschil tussen dit cijfer en het getal.
    Het verschil moet positief zijn (gebruik abs).

    >>> Genereer getal tussen 1 en: 7
    >>> Gok het willekeurig getal: 4
    Het willekeurig getal was 4. Je zit er 0 naast.

    >>> Genereer getal tussen 1 en: 23
    >>> Gok het willekeurig getal: 1
    Het willekeurig getal was 10. Je zit er 9 naast.
"""
cijfer= int(input("geef een getal in: "))
getal1 = random.randint(1,cijfer)


getal2= int(input("geef nog een getal in: "))

verschil= abs(getal1-getal2)
print(f"Het willekeurig getal was {getal1}. Je zit er {verschil} naast.")
