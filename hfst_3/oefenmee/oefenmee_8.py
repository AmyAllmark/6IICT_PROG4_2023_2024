"""
Volg de instructies van oefen mee 8.
Je zal een simpel rekenmachine maken met behulp van 2 Entries, 1 label & 1 button.
    
    Tip! De methode .get() van entries geeft altijd een string.
         Je kan hier natuurlijk niet mee rekenen.
"""

import tkinter as tk
app = tk.Tk()


label = tk.Label(master=app, text="de som van de bovenste getallen zijn...")
label.grid(row=1, column=0, columnspan=2)

def bereken():
   som= int(veld.get())+int(veld2.get())# je moet ze ints maken anders print hij gewoon de twee getallen die je hebt ingegeven 
   print(som)



knop = tk.Button(master=app, text="Klik ook op mij!",command=bereken)
knop.grid(row=3,column=0,columnspan=2)
# 1) Inputveld aanmaken.
    # master: geef aan tot welke GUI het inputveld behoort.
veld = tk.Entry(master=app)
veld2 = tk.Entry(master=app)

if bereken != int:
    print("je hebt geen getal ingegeven maar tekst")




# 2) Inputveld plaatsen
veld.grid(row=0, column=0) # Rij 1, kolom 0
veld2.grid(row=0, column=1) # Rij 1, kolom 0

app.mainloop()