from model import Model

DATOTEKA_RECEPTOV = 'recepti.json'
DATOTEKA_ELEMENTOV = 'elementi.json'
model = Model.preberi_iz_datoteke(IME_DATOTEKE)

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        osnovni_zaslon()

NAPISI_RECEPT = 'napiši recept'
DODAJ_ELEMENT = 'dodaj element'
ZAKLJUCI = 'zaključi'

def osnovni_zaslon():
    while True:
        ukaz = preberi_ukaz()
        if ukaz == NAPISI_RECEPT:
            napisi_recept()
        elif ukaz == DODAJ_ELEMENT:
            dodaj_element()
        elif ukaz == ZAKLJUCI:
            model.shrani_v_datoteko(IME_DATOTEKE)
            print('Nasvidenje!')
            break



def napisi_recept():
    ime = input('Ime recepta> ')
    velikost = input('Velikost> ')
    sestavine = input('Sestavine> ')
    postopek = input('Postopek> ')
    model.knjiznica.dodaj_recept(ime, velikost, sestavine, postopek)


def dodaj_element():
    ime = input('Ime elementa> ')
    kolicina = input('Količina> ')
    enota = input('Enota> ')
    model.listek.dodaj_element(ime, kolicina, enota)