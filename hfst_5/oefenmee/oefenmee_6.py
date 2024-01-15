# Werk verder met de klasse Hond van oefen mee 4.

class Hond:

    def __init__(self,naam,massa):
        self.naam = naam
        self.massa = massa

    def benoem(self, naam):
        self.naam = naam

    def blaf(self):
        print(self.naam, "blaf")
    
    def wegen(self,massa):
        self.massa = massa

    def weegschaal(self):
        print(f'{self.naam} massa:{self.massa}kg')
    
    
 
" Via onderstaande code kan je niveau 2 testen. "
hond_1=Hond("Florens",8)
hond_2=Hond("Fleur", 3)

hond_1.weegschaal()
hond_2.weegschaal()
