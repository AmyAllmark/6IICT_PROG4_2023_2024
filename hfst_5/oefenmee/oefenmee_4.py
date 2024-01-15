# Werk verder met de klasse Hond van oefen mee 2.
class Hond:
    naam= "Molly"
    massa= 25
    def benoem(self, naam):
        self.naam = naam

    def blaf(self):
        print(self.naam, "blaf")
    
    def wegen(self,massa):
        self.massa = massa

    def weegschaal(zich):
        print(f'{zich.naam} massa:{zich.massa}kg')

" Via onderstaande code kan je niveau 1 testen. "
hond = Hond()
hond.benoem("Fleur")
print( hond.naam )
hond.blaf()

" Via onderstaande code kan je niveau 2 testen. "
dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
print( dier.massa )
dier.weegschaal()