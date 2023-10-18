"""
Volg de instructies van oefen mee 10.
Je zal een app maken waarmee je de eerste/laatste letter uit een entry kan verwijderen.
De app bestaat uit 1 entry & 2 buttons.

"""
import tkinter as tk
app = tk.Tk()

def verwijder_eerst():
    veld.delete(0,1) # verwijderd het eerste lettertje van je voor van voor

def verwijder_laatst():
    inhoud = veld.get()   # Haal huidige inhoud op.
    inhoud = inhoud[:-1]  # Verwijder laatste letter uit variabele.
    veld.delete(0,tk.END) # Maak volledige Entry leeg.
    veld.insert(0,inhoud) # Voeg gewijzigde inhoud terug toe

knop1 = tk.Button(master=app, text="Verwijder eerst",command=verwijder_eerst)
knop1.grid(row=1,column=0,padx=10)
knop2 = tk.Button(master=app, text="Verwijder laatst",command=verwijder_laatst)
knop2.grid(row=1,column=1)

veld = tk.Entry(master=app)


veld.grid(row=0, column=0,columnspan=2) # Rij 1, kolom 0

app.mainloop()