"""
Volg de instructies van oefen mee 12.
In deel 1 van de oefen mee maak je het uiterlijk van een rekenmachine.
In deel 2 zal je deze ook echt laten werken.

    Tip! Je kan instellingen van widgets ook inladen via een dictionary.
         Op deze manier kan je veel gelijkaardige widgets snel opstellen en aanpassen.
         Er is een voorbeeld onderaan de oefen mee voorzien.
"""

import tkinter as tk
app = tk.Tk()

# Maak label aan waarin tekst van Entry komt te staan
label = tk.Label(master=app, text="           ", width=20,height=2)
label.grid(row=0, column=0,columnspan=3, padx= 20, pady=5)
kleur= "green"
label.config(bg=kleur) #fg= forground bg= background

def optellen():
    



knop1 = tk.Button(master=app, text="1",command=(),width=8,height=2)
knop1.grid(row=1,column=0)

knop2 = tk.Button(master=app, text="2",command=(),width=8,height=2)
knop2.grid(row=1,column=1)

knop3 = tk.Button(master=app, text="3",command=(),width=8,height=2)
knop3.grid(row=1,column=2)

knop4 = tk.Button(master=app, text="4",command=(),width=8,height=2)
knop4.grid(row=2,column=0)

knop5 = tk.Button(master=app, text="5",command=(),width=8,height=2)
knop5.grid(row=2,column=1)

knop6 = tk.Button(master=app, text="6",command=(),width=8,height=2)
knop6.grid(row=2,column=2)

knop7 = tk.Button(master=app, text="7",command=(),width=8,height=2)
knop7.grid(row=3,column=0)

knop8 = tk.Button(master=app, text="8",command=(),width=8,height=2)
knop8.grid(row=3,column=1)

knop9 = tk.Button(master=app, text="9",command=(),width=8,height=2)
knop9.grid(row=3,column=2)


knop0 = tk.Button(master=app, text="0",command=(),width=8,height=2)
knop0.grid(row=4,column=0)

knop_plus = tk.Button(master=app, text="+",command=(),width=8,height=2)
knop_plus.grid(row=4,column=1)

knop_min = tk.Button(master=app, text="-",command=(),width=8,height=2)
knop_min.grid(row=4,column=2)

knop_is = tk.Button(master=app, text="=",command=(),width=8,height=2)
knop_is.grid(row=5,column=0)

knop_CLR = tk.Button(master=app, text="CLR",command=(),width=18,height=2)
knop_CLR.grid(row=5,column=1, columnspan=2)




app.mainloop()
