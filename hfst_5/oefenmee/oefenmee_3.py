# Op welke regels print deze code iets?
# Er za ook een fout ontstaan. Leg uit waarom. --> veranders door self want hij herkent kitten niet want die staat buiten de def
class Kat:
    naam = "Borysz"

    def miauw(self):
        print(f"{self.naam} zegt miauw")

kater = Kat()
kater.miauw() 

kitten = Kat()
kitten.miauw()