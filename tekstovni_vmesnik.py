from model import Model

model = Model()

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        osnovni_zaslon()

NAPISI_RECEPT = 'napiši recept'
DODAJ_RECEPT = 'dodaj recept'
DODAJ_ELEMENT = 'dodaj element'

def osnovni_zaslon():
    prikazi_recepte_in_listek()
    ukaz = preberi_ukaz()
    if ukaz == NAPISI_RECEPT:
        napisi_recept()
    elif ukaz == DODAJ_RECEPT:
        dodaj_recept()
    elif ukaz == DODAJ_ELEMENT:
        dodaj_element()



def dodaj_recept():
    ime = input('Ime recepta> ')
    kolicina = input('Količina> ')
    enota = input('Enota> ')
    model.listek.dodaj_recept(ime, kolicina, enota)


def dodaj_element():
    ime = input('Ime elementa> ')
    kolicina = input('Količina> ')
    enota = input('Enota> ')
    model.listek.dodaj_element(ime, kolicina, enota)