""" Vraag een gebruiker zijn/haar naam.
    
    Print alle klinkers die in de naam voorkomen.
        Tip! gebruik de methode .lower()

     Geef een naam op: Korneel
    In Korneel zit een e
    In Korneel zit een o

    EXTRA: print ook hoevaak iedere klinker voorkomt.
"""
klinkers= "aeiou"
naam= str(input("voer uw naam in: "))
naam=naam.lower()

for klinker in klinkers:
    if klinker in naam:
     print(f"in {naam} zit een {klinker} ")


