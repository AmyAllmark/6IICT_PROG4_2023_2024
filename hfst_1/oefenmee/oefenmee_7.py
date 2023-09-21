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
    print(gasten.get(gebruiker," niet aanwezig"))

    if gebruiker in gasten:
        print(f"welkom {gasten[gebruiker]} {gebruiker}.")
        gasten.pop(gebruiker)
    else:
        print(f"{gebruiker} staat niet op de lijst.")
        