import json

class Model:
    def __init__(self):
        self.knjiznica = []

    def dodaj_recept(self, ime, velikost,  sestavine, postopek):
        recept = Recept(ime, velikost, sestavine, postopek)
        self.knjiznica.append(recept)
    
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
    
    def dodaj_sestavino(self, ime, kolicina):
        sestavina = Sestavina(ime, kolicina)
        self.sestavine[ime] = kolicina



class Sestavina:
    def __init__(self, ime, kolicina):
        self.ime = ime
        self.kolicina = kolicina