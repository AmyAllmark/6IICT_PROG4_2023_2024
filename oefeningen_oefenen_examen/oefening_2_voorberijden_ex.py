""" Voorbeelden (API geeft enkel Engelse zinnen terug):

API: https://api.adviceslip.com/

Advies 1:
    Input || Topic for advice: spiders
    Print || Remember that spiders are more afraid of you, than you are of them.
Advies 2:
    Input || Topic for advice: teeth
    Print || You don't need to floss all of your teeth. Only the ones you want to keep.
Advies 3:
    Input || Topic for advice: programming
    Print || No advice slips found matching that search term.

"""

import requests, json

onderwerp= input("on what topic would you like advice?: ")
url= f"https://api.adviceslip.com/advice/search/{onderwerp}"

response = requests.get(url)# krijg info van API
response_json = response.json()

with open("adviceslip2.json", "w") as fp: 
    json.dump(response_json, fp)

if "message" in response_json:
    print("No advice slips found matching that search term.")

else:
    print(response_json["slips"][0]["advice"])

