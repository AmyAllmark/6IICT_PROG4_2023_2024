import requests,json





# deel 1 stel url op 
print("welkom bij de grappengenerator")
print("wat voor soort grap je je hebben?:")
print("als je wilt stoppen geef -1 in.")

cateogorieën= ['programming',"Any","Miscellaneous","Dark","Pun","Spooky"]

for index,cat  in enumerate(cateogorieën):
    print(index+1,cat)


while True: 

    gebruiker=int(input("Kies een categorie: "))
    print('------------------------------------')
    cat= cateogorieën[gebruiker-1]

    if gebruiker == -1:
        break
    basis_url= "https://v2.jokeapi.dev/joke/"
    url = f"{basis_url}{cat}"

    # deel 2 gebruik url om serverdata op te halen 
    response_json = requests.get(url).json()

    #print(url)
    #print(response_json)

    # deel 3 zet server data in json bestand 
    with open("hfst_2/opdrachten/bericht_jokeapi.json", "w") as file:
        json.dump(response_json, file)
        #print("Data gedumpt!")


    # deel 4 verwerk server data 

    if 'setup' in response_json:
        print(response_json["setup"])    # De setup
        print(response_json["delivery"]) # De punchline

    else:
        print(response_json["joke"]) # De joke

    print('------------------------------------')


