""" Vraag de gebruiker naar een getal.

    Print de tafel van 9.
    Begin bij 0*9 en eindig bij het getal*9.

    Print tenslotte ook de totaalsom van de tafel.
        Tip! Maak een teller aan voor de for-loop.
    
    >>> Tot welk getal gaat de tafel: 3
    0*9=0
    1*9=9
    2*9=18
    3*9=27
    De totaalsom van de tafel is 54
"""
getal= int(input(" geef een getal: "))
teller=0
for i in range(getal+1):
    print(f"{i}*9={i*9}")
    teller=teller+i*9
print(f"totaal= {teller}")

