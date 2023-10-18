"""
Volg de instructies van oefen mee 9.
Je zal een app maken om letters toe te voegen aan een entry op een specifieke positie?
De app bestaat uit 3 entries & 1 button.

"""
import tkinter as tk
app = tk.Tk()

def bereken():
   getal=int(veld.get())
   letter= str(veld2.get())
   veld3.insert(getal,letter) 

knop = tk.Button(master=app, text="berekenen",command=bereken)
knop.grid(row=3,column=0,columnspan=2)

veld = tk.Entry(master=app)
veld2 = tk.Entry(master=app)
veld3 = tk.Entry(master=app)


veld.grid(row=0, column=0) # Rij 1, kolom 0
veld2.grid(row=0, column=1) # Rij 1, kolom 0
veld3.grid(row=4, column=0, columnspan=2) # Rij 1, kolom 0


app.mainloop()