""" Oefening 3 (  / 8): klikker app.

Baseer je op oefening_3.exe om de klikkerapp op te bouwen.
Onderstaande vereisten bevatten de zaken waar je zeker op moet letten.

Grafische vereisten:
    - Bouw de app na zoals in de exe (de widgets moeten allemaal op dezelfde plaats staan).
    - De titel van de app is "klikker-spel".
    - De Entry bovenaan heeft bij de start van de app een waarde 0 reeds ingevuld.
    - De knop heeft een breedte van 15.
    - Het label dat de teller toont heeft als font "Helvetica" met een grootte 14.
    - Het label dat de teller toont heeft een padding van 10 boven en onder zich.

Functionele vereisten:
    - Op de knop duwen moet een teller verhogen met de waarde die momenteel in de Entry staat.
      Bevat de Entry GEEN geheel getal op dat moment? Reset de teller dan naar 0.
    - Na het verhogen van de teller moet ook het label onderaan wijzigen.
      ---> Het getal rechts in het label moet dezelfde waarde zijn als de teller.
      ---> Is de teller even, dan is het label groen. Is de teller oneven, dan is het label rood.

"""
# Importeer tkinter module als tk.
import tkinter as tk
 
# Maak een nieuwe (lege) app aan.
app = tk.Tk()
app.title("Klikker-spel")

teller=0
def DuwOpKnop():
    global teller
    waardeEntry= NummerEntry.get()

    if not waardeEntry.isnumeric():
        teller=0
    else:
        teller= teller+ int(waardeEntry)

    if teller %2 ==0: # even waarde
        TellerUitkomstLabel.config(fg="green", text=f'Teller:{teller}') # verander kleur tekst en de tekst zelf 
    
    else:             # oneven
        TellerUitkomstLabel.config(fg="red", text=f'Teller:{teller}')
    

labelVerhoog= tk.Label(master=app, text=" teller verhogen met: ")
labelVerhoog.grid(row=0, column=0)

NummerEntry= tk.Entry(master=app)
NummerEntry.grid(row=0, column=1)
NummerEntry.insert(0,"0") # bij start op scherm zie je dat er al een 0 is ingevuld in je entry

ButtonVerhoogTeller= tk.Button(master=app, text= "Verhoog de teller", width= 15,command=DuwOpKnop)
ButtonVerhoogTeller.grid(row=1,column=0,columnspan=2)

TellerUitkomstLabel= tk.Label(master=app,text= "Teller: 0", font=("Helvetica",14),fg="green")
TellerUitkomstLabel.grid(row=2,column=0,columnspan=2, pady=(10,10))





 
# Start app.
app.mainloop()
