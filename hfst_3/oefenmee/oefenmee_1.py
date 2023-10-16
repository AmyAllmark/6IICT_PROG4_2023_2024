""" 
Maak een app aan die 3 labels bevat.
De inhoud van de 3 labels is:
    - Label 1: hallo
    - Label 2: klas
    - Label 3: 6iict
"""

# Importeer tkinter module als tk.
import tkinter as tk

# Maak een nieuwe (lege) app aan.
app = tk.Tk()

# 1) Label aanmaken.
    # master: geef aan tot welke app het label behoort.
    # text: boodschap van het label.
label = tk.Label(master=app, text="Hallo!")
label2 = tk.Label(master=app, text="klas")
label3 = tk.Label(master=app, text="6IICT")
# 2) Label plaatsen op app.
label.pack()
label2.pack()
label3.pack()


# Start app.
app.mainloop()
