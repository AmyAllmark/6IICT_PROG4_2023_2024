# Werk verder met de klasse Hond van oefen mee 6.

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
        print(f'{self.naam} massa: {self.massa}kg')
    
    def wijzig_naam(self, naam):
        self.naam = naam
    
    def eten(self,hoeveelheid):
        self.massa += hoeveelheid


" Via onderstaande code kan je niveau 1 testen. "
hond = Hond("Lucky", 5)
hond.wijzig_naam("Bolly")

" Via onderstaande code kan je niveau 2 testen. "
hond = Hond("Lucky", 5)
hond.eten(0.5)
hond.weegschaal()
hond.eten(0.5)
hond.weegschaal()
hond.eten(0.5)
hond.weegschaal()


" Stel de test voor niveau 3 zelf op. "