# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
fruit = "banaan"
print( fruitmand[fruit] )

nieuw_fruit  = "mango"
nieuw_aantal1 = 1
fruitmand[nieuw_fruit]= nieuw_aantal1


fruit = "banaan"
nieuw_aantal2 = 8
fruitmand[fruit]= nieuw_aantal2
terugleggen_fruit = "kers"
fruitmand.pop("kers") # kers verwijderen uit lijst
print(fruitmand)




