"""
Maak oefen mee 11 op basis van de uitleg in OneNote.
Niveau 1
Vraag de gebruiker om een getal tussen 1 en 10. Print vervolgens het getal * 2. 
Als het nummer niet tussen 1 en 10 ligt, raise een ValueError. 
Geef in deze Error mee wat de gebruiker verkeerd deed.

Niveau 2
Indien de gebruiker geen getal heeft ingegeven, raise ook een error. 
Bepaal zelf welke je gebruikt.

"""
gebruiker=int(input("geef een geheel getal in tussen 1 en 10: "))


if 1 < gebruiker < 10:
    print(gebruiker*2)

else:
    raise ValueError("u hebt geen getal ingegeven dat tussen de 1 en 10 lag")

    