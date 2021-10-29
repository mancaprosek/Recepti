import json
import random

class Model:
    def __init__(self, ime_datoteke):
        self.knjiznica = self.nalozi(ime_datoteke)

    def dodaj_recept(self, ime, velikost, sestavine, postopek):
        id = random.randint(0, 100000)
        recept = Recept(id, ime, velikost, sestavine, postopek)
        self.knjiznica.append(recept)
        return recept
    
    def izbrisi_recept(self, indeks):
        self.knjiznica.pop(indeks)

    def izbrisi_recept_id(self, id):
        ind = 0
        for idx, recept in enumerate(self.knjiznica):
            if recept.id == id:
                ind = idx
                break
        self.knjiznica.pop(ind)
                
    
    def shrani(self, ime_datoteke):
        with open(ime_datoteke, 'w') as f:
            json.dump([ob.__dict__ for ob in self.knjiznica], f)


    def nalozi(self, ime_datoteke):
        with open(ime_datoteke) as f:
            data = json.load(f)
            seznam = []
            for slovar in data:
                seznam.append(Recept.iz_slovarja(slovar))
            self.knjiznica = seznam
            return seznam


class Recept:
    def __init__(self, id,  ime, velikost, sestavine, postopek):
        self.id = id
        self.ime = ime
        self.velikost = velikost
        self.sestavine = sestavine
        self.postopek = postopek


    def dodaj_sestavino(self, ime, kolicina, enota):
        sestavina = Sestavina(ime, kolicina, enota)
        self.sestavine[ime] = (kolicina, enota)


    @staticmethod
    def iz_slovarja(slovar):
        return Recept(
            slovar['id'],
            slovar['ime'],
            slovar['velikost'],
            slovar['sestavine'],
            slovar['postopek']
        )


class Sestavina:
    def __init__(self, ime, kolicina, enota):
        self.ime = ime
        self.kolicina = kolicina
        self.enota = enota