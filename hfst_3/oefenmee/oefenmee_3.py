"""
Maak de app na volgens de foto bij oefen mee 3.
Je hebt maar 3 labels nodig om deze app te maken.
"""
# Importeer tkinter module als tk.
import tkinter as tk

# Maak een nieuwe (lege) app aan.
app = tk.Tk()

label_1 = tk.Label(master=app, text="Hallo")
label_1.grid(row=1, column=0) # Rij 1, kolom 0


label_1_2 = tk.Label(master=app, text="klas")
label_1_2.grid(row=1, column=1) # Rij 1, kolom 0


label_2 = tk.Label(master=app, text="6IICT")
label_2.grid(row=2, column=0) # Rij 1, kolom 0
app.mainloop()
