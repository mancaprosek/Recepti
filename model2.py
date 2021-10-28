import json

class Model:
    def __init__(self):
        self.knjiznica = []

    def dodaj_recept(self, ime, velikost,  sestavine, postopek):
        recept = (ime, velikost, sestavine, postopek)
        self.knjiznica.append(recept)
    
    #tle zraven ni tega razreda recept
    
    def izbrisi_recept(self, indeks):
        self.knjiznica.pop(indeks)

    def izbrisi_knjiznico(self):
        self.knjiznica.clear()
    
    

class Recept:
    def __init__(self, ime, velikost, sestavine, postopek):
        self.ime = ime
        self.velikost = velikost
        self.sestavine = {}
        self.postopek = postopek
    
    def dodaj_sestavino(self, ime, kolicina, enota):
        sestavina = (ime, kolicina, enota)
        self.sestavine[ime] = (kolicina, enota)
    
    #ni razreda sestavina



class Sestavina:
    def __init__(self, ime, kolicina, enota):
        self.ime = ime
        self.kolicina = kolicina
        self.enota = enota