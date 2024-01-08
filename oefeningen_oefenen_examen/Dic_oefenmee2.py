# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}



# key en value toevoegen aan dictionarie
fruitmand["aardbij"]=1      # item toegevoegd aan dictionarie | waanneer de string/key  bestaat in de dictionarie voegt die die toe met de naam en waarde die je aangeeft


#ook key en value toevoegen maar met variables
# of  --> fruit= "aardbij"
#         hoeveelheid_fruit= 1
#         fruitmand[fruit]=hoeveelheid_fruit 

#waarde veranderen van een key in de dictionarie
fruitmand["kers"]=49 # bestaat de string/key wel dan veranderd hij de waarde naar de waarde die je aangeeft

# een key en value wissen
fruitmand.pop("appel") # verwijderen uit dictionarie

# of : del fruitmand["appel"]

fruitToPrint= "kers"
print(f'ik heb {fruitmand[fruitToPrint]} {fruitToPrint}')

print(fruitmand)  
    

