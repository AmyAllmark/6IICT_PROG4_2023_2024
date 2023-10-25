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

getal1= 0
getal2= 0
operator= ""

def knop1_ingedrukt():
    veld.insert(tk.END,"1")

def knop2_ingedrukt():
    veld.insert(tk.END,"2")

def knop3_ingedrukt():
    veld.insert(tk.END,"3")

def knop4_ingedrukt():
    veld.insert(tk.END,"4")

def knop5_ingedrukt():
    veld.insert(tk.END,"5")

def knop6_ingedrukt():
    veld.insert(tk.END,"6")

def knop7_ingedrukt():
    veld.insert(tk.END,"7")

def knop8_ingedrukt():
    veld.insert(tk.END,"8")

def knop9_ingedrukt():
    veld.insert(tk.END,"9")

def knop0_ingedrukt():
    veld.insert(tk.END,"0")

def plus_ingedrukt():
    global getal1
    # haal huidige waarde van veld op, zet om naar int en sla op in getal 1
    getal1= int(veld.get()) #
    global operator
    operator = "+"
    veld.insert(tk.END,"+")# print het in het veld na getal 1 als knop wordt ingedrukt 


def min_ingedrukt():
    global getal1
    # haal huidige waarde van veld op, zet om naar int en sla op in getal 1
    getal1= int(veld.get()) #
    global operator
    operator = "-"
    veld.insert(tk.END,"-")# print het in het veld na getal 1 als knop wordt ingedrukt 

def is_gelijk_aan():
    global getal2
    alles=veld.get() # sla heel de tekst dat in het veld staat op in variable alles
    positie = alles.find(operator)# kijk alles na van de tekst in het veld en kijk als de operator er in staat (+) sla die op in positie 
    getal2 = int(alles[positie+1:]) #herken de positie van getal 2 na het plus teken en alles op het eind

    if operator == "+":
        result = getal1+getal2
    elif operator == "-":
        result= getal1-getal2

    veld.delete(0,tk.END)# heel het veld deleate om de som te kunnen laten zien 
    veld.insert(0,str(result))

def CLR():
    veld.delete(0,tk.END)
    
    



# Maak label aan waarin tekst van Entry komt te staan
veld = tk.Entry(master=app, text="           ", width=20)
veld.grid(row=0, column=0,columnspan=3, padx= 20, pady=5)
kleur= "pink"
veld.config(bg=kleur) #fg= forground bg= background

knop1 = tk.Button(master=app, text="1",command=knop1_ingedrukt,width=8,height=2)
knop1.grid(row=1,column=0)

knop2 = tk.Button(master=app, text="2",command=knop2_ingedrukt,width=8,height=2)
knop2.grid(row=1,column=1)

knop3 = tk.Button(master=app, text="3",command=knop3_ingedrukt,width=8,height=2)
knop3.grid(row=1,column=2)

knop4 = tk.Button(master=app, text="4",command=knop4_ingedrukt,width=8,height=2)
knop4.grid(row=2,column=0)

knop5 = tk.Button(master=app, text="5",command=knop5_ingedrukt,width=8,height=2)
knop5.grid(row=2,column=1)

knop6 = tk.Button(master=app, text="6",command=knop6_ingedrukt,width=8,height=2)
knop6.grid(row=2,column=2)

knop7 = tk.Button(master=app, text="7",command=knop7_ingedrukt,width=8,height=2)
knop7.grid(row=3,column=0)

knop8 = tk.Button(master=app, text="8",command=knop8_ingedrukt,width=8,height=2)
knop8.grid(row=3,column=1)

knop9 = tk.Button(master=app, text="9",command=knop9_ingedrukt,width=8,height=2)
knop9.grid(row=3,column=2)


knop0 = tk.Button(master=app, text="0",command=knop0_ingedrukt,width=8,height=2)
knop0.grid(row=4,column=0)

knop_plus = tk.Button(master=app, text="+",command= plus_ingedrukt,width=8,height=2)
knop_plus.grid(row=4,column=1)

knop_min = tk.Button(master=app, text="-",command=min_ingedrukt,width=8,height=2)
knop_min.grid(row=4,column=2)

knop_is = tk.Button(master=app, text="=",command=is_gelijk_aan,width=8,height=2)
knop_is.grid(row=5,column=0)

knop_CLR = tk.Button(master=app, text="CLR",command=CLR,width=18,height=2)
knop_CLR.grid(row=5,column=1, columnspan=2)




app.mainloop()
