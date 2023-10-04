
# idee, laat de gebruiker zelf een drankje ingeven en geef daar de info van 
# idee, de gebruiker kan ook vragen voor een verassing drankje dus dan kiest die random een drankje
import requests,json



while True:
    print("Welkom, bij deze API kunt u resepten vinden voor Alcoholiche drankjes ")#bv Margarita
    gebruiker=input("van welk soort drankje wilt u het resept?: ")
#eerste endpoint 1
    basis_url= f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={gebruiker}"
    response_json = requests.get(basis_url).json()


#handlijding in welke taal
    if response_json["drinks"] == None: 
        print("het drankje bestaat niet")
        print("--------------------------------------")
        continue
 
    drankje = (response_json["drinks"][0])
    taal_instructies = input(f'welke taal wil je? je kan kiezen uit DE/IT (enter voor EN): ')
    taal_instructies = f'strInstructions{taal_instructies}'

    if taal_instructies in drankje:
        print("-----------------------------------------------------------------------------------")
        print(f"instructies voor {gebruiker}:")
        print(drankje[taal_instructies])
        print("-----------------------------------------------------------------------------------")


#ingredienten 
    else: 
        print("taal niet gevonden")

    print(f'de ingredienten van {gebruiker} zijn: ')
    for i in range(0, 15):
        if drankje[f'strIngredient{i+1}'] == None:
            
            break
        else:
            print(drankje[f'strIngredient{i+1}'])
    print("---------------------------------------------------------")

#--------------------------------------------------------------------

    # categorie van drankje // vraag gebruiker om categorie drankje
    while True:
        catagorie=input(f"wilt u weten uit welke catagorie {gebruiker} komt? j/n: ")

        if catagorie == "n":
            break
        elif catagorie =="j":
            print("de catagorie is:")
            print(drankje['strCategory'])
            break
        else:
            print("**********************************")
            print("ERROR:geen j of n ingegeven dus kan info niet geven")
            print("**********************************")


# random drankje 

#tweeede endpoint 2
    url_random_drankje=f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
    response_json = requests.get(url_random_drankje).json()
    random_drankje=input(f"wilt u dat ik u een drankje voorstel? j/n: ")

    if random_drankje == "j":
         with open("hfst_2\TaakAPIrandom_drankje.json", "w") as file:
            json.dump(response_json, file)
            #print("Data gedumpt!")

    if random_drankje == "n":
        continue


    with open("hfst_2\TaakAPIfout.json", "w") as file:
            json.dump(response_json, file)
            #print("Data gedumpt!")


    if response_json["drinks"] == None: 
            print("het drankje bestaat niet")
            print("--------------------------------------")
            continue
    
    random_drankje = (response_json["drinks"][0])
    naam_random_drankje= random_drankje["strDrink"]
    taal_instructies_random_drankje = input(f'welke taal wil je? je kan kiezen uit DE/IT (enter voor EN): ')
    taal_instructies_random_drankje = f'strInstructions{taal_instructies_random_drankje}'

    if taal_instructies in drankje:
        print("-----------------------------------------------------------------------------------")
        print(f"instructies voor {naam_random_drankje}:")
        print(random_drankje[taal_instructies_random_drankje])
        print("-----------------------------------------------------------------------------------")
    
# ingredient ingeven en krijg je een resept, naam coctail enzo
    Gebruiker_ingredient=input(f" geef een ingredient in engels in en krijg meer info over dit ingredient: ")
    url_ingredient_ingeven=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?i={Gebruiker_ingredient}"
    response_json = requests.get(url_ingredient_ingeven).json()

    with open("hfst_2\TaakAPIingredient.json", "w") as file:
        json.dump(response_json, file)


    inggredient = (response_json["ingredients"][0])
    naam_ingredient= inggredient["strIngredient"]

  

    print(f" meer uileg over {naam_ingredient}")
    print(inggredient["strDescription"])

    if inggredient == None: 
        print("ingredient niet gevonden.")
    
 
  




   