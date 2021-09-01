class Model:
    def __init__(self):
        self.knjiznica = []
        self.listek = {}


    def napisi_recept(self, ime, velikost, sestavine, postopek):
        recept = Recept(ime, velikost, sestavine, postopek)
        self.knjiznica.append(recept)
    
    def izbrisi_recept(self, indeks):
        self.knjiznica.pop(indeks)

    
    def dodaj_element(self, ime, kolicina, enota):
        element = Element(self, ime, kolicina, enota)
        if ime not in self.listek.keys():
            self.listek(ime) = kolicina
        else:
            kolicina += self.listek(ime)
            self.listek(ime) = kolicina
    
    def izbrisi_element(self, ime):
        self.listek.pop(ime)

    def izbrisi_listek(self):
        self.listek.clear()




class Recept:
    def __init__(self, ime, velikost, sestavine, postopek):
        self.ime = ime
        self.velikost = velikost
        self.sestavine = []
        self.postopek = postopek
    
    def dodaj_sestavino(self, ime, kolicina, enota):
        sestavina = Sestavina(ime, kolicina, enota)
        self.sestavine.append(sestavina)



class Sestavina:
    def __init__(self, ime, kolicina, enota):
        self.ime = ime
        self.kolicina = kolicina
        self.enota = enota



class Element:
    def __init__(self, ime, kolicina, enota):
        self.ime = ime
        self.kolicina = kolicina
        self.enota = enota