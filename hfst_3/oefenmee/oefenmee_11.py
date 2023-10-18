"""
Volg de instructies van oefen mee 11.
Je zal een app maken om de kleur van een label aan te passen.
De app bestaat uit 1 entry, 1 label & 1 button.

    Tip! Je zal de methode .config() moeten gebruiken.
         Hiermee kan je de onderdelen (kleur, tekst, ...) van een widget wijzigen.

"""
import tkinter as tk
app = tk.Tk()

# Maak label aan waarin tekst van Entry komt te staan
label = tk.Label(master=app, text="")
label.grid(row=1, column=0)


def wijzig():

    kleur=veld.get()
    if kleur == "red" or "green" or "pink"or "purple"or "blue"or "yellow"or "turquoise":
        # Wijzig de tekst en kleur van het label.
        label.config(text=f"Het label is nu {kleur}", fg=kleur)

knop1 = tk.Button(master=app, text="Wijzig",command=wijzig)
knop1.grid(row=0,column=2)

veld = tk.Entry(master=app)


veld.grid(row=0, column=0,columnspan=2) # Rij 1, kolom 0

app.mainloop()


