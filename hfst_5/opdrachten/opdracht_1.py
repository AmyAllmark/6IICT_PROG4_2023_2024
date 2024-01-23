# Maak de klasse Familie aan zoals omschreven in opdracht 1.

class Familie:
    ras = "mens"# omdat dit altijd zo is en de zelfde waarde zal moeten hebben
    def __init__(self, geslacht, leeftijd,naam,haar) :
        self.geslacht=geslacht
        self.leeftijd=leeftijd
        self.naam=naam
        self.haar=haar

    def is_leeftijd(self):
        return self.leeftijd
   
    
    def is_geslacht(self):
        return self.geslacht
    
    def is_naam(self):
        return self.naam
    
    def verf_haar(self, nieuwe_kleur):
        self.haar = nieuwe_kleur
        print(f'{self.naam} is nu {self.haar}')

    def verjaardag(self):
        self.leeftijd=self.leeftijd+1
        print(f'gefeliciteerd {self.naam} je bent nu {self.leeftijd}')

    def uitleg(self):
        print(f" {self.naam}: {self.geslacht}, {self.leeftijd} ,{self.haar}, {self.ras}")

  

" Via onderstaande code kan je de klasse Familie testen. "

vader = Familie(geslacht="man", haar="zwart", leeftijd=39, naam="Steve")
print(vader.is_leeftijd())  # 39
print(vader.is_geslacht())  # man
vader.verjaardag()          # Gefeliciteerd Steve, je bent nu 40
vader.verf_haar("blond")    # Steve is nu blond
print(vader.haar)
vader.uitleg()              # Steve: man, 40, blond, mens
