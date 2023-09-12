""" Vraag de gebruiker naar een woord.

    Print hoeveel klinkers er in het woord staan.
        Tip! Maak een teller aan. Overloop de 
             karakters. Als een letter een klinker
             is, verhoog de teller.

    >>> Geef een woord op: appel
    appel bevat 2 klinkers
    >>> Geef een woord op: ajuin
    ajuin bevat 3 klinkers
    >>> Geef een woord op: olifanten
    olifanten bevat 4 klinkers
"""
klinkers= "aieou"
teller= 0
woord= str(input("voer een woord in: "))

for klinker in klinkers:
    if klinker in woord:
        teller=teller+1
print(f"{woord} bevart {teller} klinkers")