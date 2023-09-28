# Pas de URL aan zoals aangegeven in de verschillende niveau's.
import requests,json

url = "https://v2.jokeapi.dev/joke/Christmas?amount=3"
response_json = requests.get(url).json() # Haal JSON uit response.

with open("hfst_2/oefenmee/jokeapi.json", "w") as file:
    json.dump(response_json, file)
    print("Data gedumpt!")

# Bepaal of de grap uit 1 of 2 delen bestaat.

for joke in  response_json["jokes"]:
    print("^^^^^^^^^^^^^^^^^^^^^^")
    if ("joke" in joke):
        print(joke["joke"])     # De grap
    else:
        print(joke["setup"])    # De setup
        print(joke["delivery"]) # De punchline
