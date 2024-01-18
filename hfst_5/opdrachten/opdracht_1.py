# Maak de klasse Familie aan zoals omschreven in opdracht 1.

class Familie:
    ras = "mens"# omdat dit altijd zo is en de zelfde waarde zal moeten hebben
    def __init__(self, geslacht, leeftijd,naam) :
        self.geslacht=geslacht
        self.leeftijd=leeftijd
        self.naam=naam

    def is_leeftijd(self):
    
    def is_geslacht(self):

        


" Via onderstaande code kan je de klasse Familie testen. "

# vader = Familie(geslacht="man", haar="zwart", leeftijd=39, naam="Steve")

# print(vader.is_leeftijd())  # 39
# print(vader.is_geslacht())  # man
# vader.verjaardag()          # Gefeliciteerd Steve, je bent nu 40
# vader.verf_haar("blond")    # Steve is nu blond
# vader.uitleg()              # Steve: man, 40, blond, mens
