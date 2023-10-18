"""
Beantwoord de vragen bij oefen mee 6.
"""

import tkinter as tk

app = tk.Tk()

 # Maak entry-veld voor ophalen woorden.
veld_get = tk.Entry(master=app)
veld_get.grid(row=0,column=0)

# Maak entry-veld waar opgehaalde woorden terecht komen.
veld_insert = tk.Entry(master=app)
veld_insert.grid(row=2,column=0)


# Maak functie die inhoud veld_get toevoegt aan einde van veld_insert.
def toevoegen():
    woord = veld_get.get()
    veld_insert.insert(tk.END, woord)
# Maak knop die functie toevoegen oproept
knop = tk.Button(master=app, text="Voeg toe!", command=toevoegen)
knop.grid(row=1,column=0)


def toon_tekst():
    tekst=veld.get()
    print(tekst)

    
app = tk.Tk()

# 1) Inputveld aanmaken.
    # master: geef aan tot welke GUI het inputveld behoort.
veld = tk.Entry(master=app)
# 2) Inputveld plaatsen
veld.pack()

# 1) Knop aanmaken.
knop = tk.Button(master=app, text="Klik op mij!", command=toon_tekst)
# 2) Knop plaatsen.
knop.pack()

app.mainloop()
