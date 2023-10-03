
# idee, laat de gebruiker zelf een drankje ingeven en geef daar de info van 
# idee, de gebruiker kan ook vragen voor een verassing drankje dus dan kiest die random een drankje



import requests,json
import random


while True:
    print("Welkom, bij deze API kunt u resepten vinden voor Alcoholiche drankjes ")#bv Margarita
    gebruiker=input("van welk soort drankje wilt u het resept?: ")

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

    else: 
        print("taal niet gevonden")

#ingredienten 
    print(f'de ingredienten van {gebruiker} zijn: ')
    for i in range(0, 15):
        if drankje[f'strIngredient{i+1}'] == None:
            
            break
        else:
            print(drankje[f'strIngredient{i+1}'])
    print("---------------------------------------------------------")

#--------------------------------------------------------------------

# categorie van drankje 
    catagorie=input(f"wilt u weten uit welke catagorie {gebruiker} komt? j/n: ")

    if catagorie == "n":
        continue

    if catagorie =="j":
        print("de catagorie is:")
        print(drankje['strCategory'])
    
    else:
        print("**********************************")
        print("ERROR:geen ja of nee ingegeven dus kan info niet geven")
        print("**********************************")


# random drankje 
    random_drankje=input(f"wilt u dat ik u een drankje voorstel? j/n: ")

    if random_drankje == "j":
   # fout vraag meneer     print(random.choice(drankje("strDrink") )

    if random_drankje == "n":
        continue


    with open("hfst_2\TaakAPIfout.json", "w") as file:
            json.dump(response_json, file)
            #print("Data gedumpt!")



    # dranken= ["Margarita","Blue Margarita","Tommy's Margarita","Whitecap Margarita","Strawberry Margarita","Smashed Watermelon Margarita"]
    # if gebruiker in dranken:
    #     print(f'u heeft voor het resept van {gebruiker} gekozen')