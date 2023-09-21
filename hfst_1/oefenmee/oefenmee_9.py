# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
hoeveel_mensen= int(input("voor hoeveel mensen kook je?:"))
print("Recept voor worst met wortelen en erwten")
for sleutel, waarde in recept.items():
     print(f"-{sleutel}: {((waarde/4)*hoeveel_mensen)}")
