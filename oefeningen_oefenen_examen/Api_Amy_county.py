import requests, json

name= input("geef me een naam: ")

url= f"https://api.nationalize.io?name={name}"

response = requests.get(url)# krijg info van API
response_json = response.json()

with open("country.json", "w") as fp: 
    json.dump(response_json, fp)


if response_json["count"] > 0: # als de waarde van count groter is dan 0:
    print(f"de kans dat {name} van bepaalde landen komt is: ") # print 
    for landEnKans in response_json["country"]:# kijk in de json respons in de country lijst iedere lijst item is een dictionarie. we willen over elke dictionarie lopen en uit iedere dictionarie land en kans uithalen 
        print(f'land: {landEnKans["country_id"]} kans: {landEnKans["probability"]*100}%')

else:
    print(f'{name} niet gevonden') 



