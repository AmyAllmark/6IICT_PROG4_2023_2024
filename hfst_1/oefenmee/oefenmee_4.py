# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
gebruiker= str(input("kiest u uit appel,banaan of kers?: "))
if gebruiker in fruitmand:
    print(f"het aantal{gebruiker} in de mand is {fruitmand[gebruiker]}.")
if gebruiker not in fruitmand:
    print(f"KeyError: {gebruiker}")