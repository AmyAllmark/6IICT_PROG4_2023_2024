import requests, json
 
# we maken een menu aan zodat je zelf de volgorde van vragen kunt kiezen 
while True :
    print("welkom bij het keuzemenu :)")
    print("____________________________________________________________")
    print("1. geef een cocktail in en krijg het resept.")
    print("2. krijg een random drankje en het recept er van. ")
    print("3. geef een ingredient in en krijg uitleg over dit ingredient. ")
    print("4. geschieddenis")
    print("5. sluit het programma")
    print("_______________________________________________________________")
    nummer=input("maak een keuze:")


# nummer 1 
    """
deze blok code heeft als bedoelling dat de gebruiker een cocktail kan ingeven en je krijgt de keuze van
in welke taal je het recept wilt ontvangen.
daarbij print hij vervolgens ook de ingredienten.
hij vraagt ook of je wil weten in welke categorie je drankje zich bevind.
    """
    if nummer == "1":
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

        #_______________________________________________________
        # tussen line 42 tot 49 worden de cocktails toegevoed die de gebruiker heeft ingegeven en deze toevoegen aan een geschieddenis voor later bij (nummer 4)
        with open("geschiedenis.json", "r") as file:
            dranken=json.load(file)
            dranken.append(gebruiker)

        with open("geschiedenis.json", "w") as file:
             json.dump(dranken, file)
        #------------------------------------------------------


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
            
            #einde bok 1/nummer1


   # random drankje  
   # deze blok
        """
deze blok code heeft een bedoelling van: dat we vragen aan de gebruiker of we hem een random drankje kunnen voorstellen.
en we printen dan ook het recept van dit drankje
        """
    elif nummer == "2":
#tweeede endpoint 2
        url_random_drankje=f"https://www.thecocktaildb.com/api/json/v1/1/random.php"
        response_json = requests.get(url_random_drankje).json()
        random_drankje=input(f"wilt u dat ik u een drankje voorstel? j/n: ")

        if random_drankje == "j":
            with open("TaakAPIrandom_drankje.json", "w") as file:
                json.dump(response_json, file)
                #print("Data gedumpt!")

        if random_drankje == "n":
            continue


        with open("TaakAPIfout.json", "w") as file:
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
# einde nummer2/blok 2

        """
bij dit stukje code hebben we een bedoelling van: vraag aan de gebruiker om een random ingredient in te geven.
hij geeft dan een uitleg over dit specifiek ingredient
        """
    elif nummer == "3":
        print(" uitleg over ingredient die je zelf ingeeft")
            # ingredient ingeven en krijg je een resept, naam coctail enzo
        Gebruiker_ingredient=input(f" geef een ingredient in engels in en krijg meer info over dit ingredient: ")
        url_ingredient_ingeven=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?i={Gebruiker_ingredient}"
        response_json = requests.get(url_ingredient_ingeven).json()

        with open("TaakAPIingredient.json", "w") as file:
            json.dump(response_json, file)


        inggredient = (response_json["ingredients"][0])
        naam_ingredient= inggredient["strIngredient"]

    

        print(f" meer uileg over {naam_ingredient}")
        print(inggredient["strDescription"])

        if inggredient == None: 
            print("ingredient niet gevonden.")
# einde blok3/nummmer3
    
            """
uitleg voor deze blok van code: 
            """
    elif nummer == "4":
        with open("geschiedenis.json", "r") as file:
            dranken=json.load(file)
        print("____________________________________________")
        print("deze dranken stonden in uw geschiedenis:")

        for drank in dranken:
            print( drank)
        print("____________________________________________")




    elif nummer == "5":
            break
    

    else: 
        print("geef een geldig nummer op")
