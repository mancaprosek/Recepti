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
    
    
    #občutek imam, da tega sploh ne rabim v modelu... Nisem prepričanaaaa
    # def v_slovar(self):
    #     return {
    #         'ime': self.knjiznica,
    #         'recepti': [Recept.v_slovar() for recept in self.knjiznica]
    #     }

    # @staticmethod
    # def iz_slovarja(slovar):
    #     knjiznica = Model(slovar['ime'])
    #     return knjiznica
        #***** v zapiskih
    #tega dela vmes, da ne rabim... Ker on je dal samo v spisek in opravila....


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


    def v_slovar(self):
        return {
            'ime': self.ime,
            'velikost': self.velikost,
            'sestavine': self.sestavine,
            'postopek': self.postopek 
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Recept(
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