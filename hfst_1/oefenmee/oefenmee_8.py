# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
stad= str(input("geef een stad in: "))

waarde=steden_temp.get(stad,22)
if stad in steden_temp:
    print(f"het is {waarde}°C")
else:
    print(f"{stad} bestaat niet, het is 22°C in België")

