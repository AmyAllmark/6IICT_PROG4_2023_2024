""" Vraag een gebruiker naar 3 getallen.
    
    Bepaal het gemiddelde van het kleinste 
    en het grootste van de 3 getallen.
    
    >>> Geef eerste getal op: 7
    >>> Geef tweede getal op: 3
    >>> Geef derde  getal op: 23
    Het gemiddelde van 3 en 23 is 13.0
"""

getal1=int(input("geef een getal in: "))
getal2=int(input("geef een getal in: "))
getal3=int(input("geef een getal in: "))

kleinste_getal=min(getal1,getal2,getal3)
grootste_getal= max(getal1,getal2,getal3)
gemiddelde= ((kleinste_getal*grootste_getal)/2)
print(f"het kleinste getal is {kleinste_getal} en het grootste getal is{grootste_getal }het gemiddelde van deze getaallen is:{gemiddelde}")

