import requests, json
Gebruiker_ingredient=input(f" geef een ingredient in en ik stel u een coctail voor waat het ingredient in zit in het engels:  ")
url_ingredient_ingeven=f"https://www.thecocktaildb.com/api/json/v1/1/search.php?i={Gebruiker_ingredient}"
response_json = requests.get(url_ingredient_ingeven).json()

with open("hfst_2\TaakAPIingredient.json", "w") as file:
    json.dump(response_json, file)


    
  

