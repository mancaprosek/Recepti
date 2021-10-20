
#A ni tko da se nesmem na tekstovni vmesnik sklicevat?

import json

class Model:
    def __init__(self):
        self.knjiznica = []
        self.listek = []


    def napisi_recept(self, ime, velikost,  sestavine, postopek):
        recept = Recept(ime, velikost, sestavine, postopek)
        self.knjiznica.append(recept)
    #A rabim tkole napisat to drugo vrstico        

    def izbrisi_recept(self, indeks):
        self.knjiznica.pop(indeks)

    def dodaj_element(self, ime, kolicina, enota):
        element = Element(self, ime, kolicina, enota)
        self.listek.append(element)
    #Isto kot 15.. a je druga vrstica potrebna
    
    def izbrisi_element(self, indeks):
        self.listek.pop(indeks)

    def izbrisi_listek(self):
        self.listek.clear()

    

    #Tale cela zadeva z zapisovanjem je za popravit
    #ker imamo samo eno json datoteko
    #Kako to narediš, da združiš...?

    def recepte_v_slovar(self):
        return {
            'ime': self.knjiznica,
            'recepti': [Recept.v_slovar() for recept in self.knjiznica]
        }
    
    def elemente_v_slovar(self):
        return {
            'ime': self.listek ,
            'elementi': [Element.v_slovar() for element in self.listek]
        }
    

    @staticmethod
    def recepte_iz_slovarja(slovar_receptov):
        knjiznica = Model(slovar_receptov['ime'])
        knjiznica.recept = [Recept.iz_slovarja(knjiznica, recept) for recept in slovar_receptov['recepti']]
        return knjiznica
    
    @staticmethod
    def elemente_iz_slovarja(slovar_elementov):
        listek = Model(slovar_elementov['ime'])
        listek.element = [Element.iz_slovarja(listek, element) for element in slovar_elementov['elementi']]



    def shrani_recepte(self, ime_datoteke):
        with open(ime_datoteke, 'w') as dat:
            slovar_receptov = self.recepte_v_slovar
            json.dump(slovar_receptov, dat)
    
    def shrani_elemente(self, ime_datoteke):
        with open(ime_datoteke, 'w') as dat:
            slovar_elementov = self.elemente_v_slovar
            json.dump(slovar_elementov, dat)

    @staticmethod
    def nalozi_recepte(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar_receptov = json.load(dat)
            return Model.recepte_iz_slovarja(slovar_receptov)
    
    @staticmethod
    def nalozi_elemente(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar_elementov = json.load(dat)
            return Model.elemente_iz_slovarja(slovar_elementov)



class Recept:
    def __init__(self, ime, velikost, sestavine, postopek):
        self.ime = ime
        self.velikost = velikost
        self.sestavine = []
        self.postopek = postopek
    
    def dodaj_sestavino(self, ime, kolicina, enota):
        sestavina = Sestavina(ime, kolicina, enota)
        self.sestavine.append(sestavina)
    #druga vrstica potrebna?
    

    def v_slovar(self):
        return {
            'ime': self.ime,
            'velikost': self.velikost,
            'sestavine': self.sestavine,
            'postopek': self.postopek
        }
    
    @staticmethod
    def iz_slovarja(knjiznica, slovar_receptov):
        return Recept(
            knjiznica,
            slovar_receptov['ime'],
            slovar_receptov['velikost'],
            slovar_receptov['sestavine'],
            slovar_receptov['postopek'],
        )

    #manjka še urejanje recepta, spreminjanje velikosti in dodajanje na listek
    #Kako pa s pisanjem velikosti in postopka?



class Sestavina:
    def __init__(self, ime, kolicina, enota):
        self.ime = ime
        self.kolicina = kolicina
        self.enota = enota

    #a so enote potrebne, pomojem se da to lepš nardit

    #moram tukaj kaj posebaj še dati za spreminjanje? a sploh rabim te razrede?


class Element:
    def __init__(self, ime, kolicina, enota):
        self.ime = ime
        self.kolicina = kolicina
        self.enota = enota
    
    #enote res rabimo??

    def v_slovar(self):
        return {
            'ime': self.ime,
            'količina': self.kolicina,
            'enota': self.enota
        }
    
    @staticmethod
    def iz_slovarja(listek, slovar_elementov):
        return Element(
            listek,
            slovar_elementov['ime'],
            slovar_elementov['količina'],
            slovar_elementov['enota'],
        )

    #manjka urejanje elementa in združevanje istih. in tist slovar z enotami bi bil kul