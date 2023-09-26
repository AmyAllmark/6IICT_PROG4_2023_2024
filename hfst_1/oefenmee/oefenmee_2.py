# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
fruit = "banaan"
print( fruitmand[fruit] ) # je print danv de waarde van banaan en dat is hier 3

nieuw_fruit  = "mango"# je voegt een nieuw element toe aan je dictionarrie 
nieuw_aantal1 = 1 # je geeft aan welke waarde gelijk is aan je nieuw element 
fruitmand[nieuw_fruit]= nieuw_aantal1 # nu zet/ print je het nieuw element en de waarde van je element 


fruit = "banaan"
nieuw_aantal2 = 8
fruitmand[fruit]= nieuw_aantal2
terugleggen_fruit = "kers"
fruitmand.pop("kers") # kers verwijderen uit lijst
print(fruitmand)




