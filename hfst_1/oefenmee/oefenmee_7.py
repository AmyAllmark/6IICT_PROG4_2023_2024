# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True:
    gebruiker= str(input( "wat is je naam? :"))
    if gebruiker == "stop":
        break
    print(gasten.get(gebruiker," niet aanwezig")) # met get kijk je of een element aanwezig is in je dictionarry hier kijk je of de naam die je aan je gebruiker hebt gevraagd aanwezig is in je dictionarry

    if gebruiker in gasten:
        print(f"welkom {gasten[gebruiker]} {gebruiker}.") # uitkom: welkom  reporter Jan !! let hier op je gaat in gasten dan gebruiker om je waarde van jan te krijgen 
        gasten.pop(gebruiker)# daarna wordt jan vzrwijderd uit de lijst 
    else:
        print(f"{gebruiker} staat niet op de lijst.")
        