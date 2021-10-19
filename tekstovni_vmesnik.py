from model import Model

model = Model()

IME_DATOTEKE = 'stanje.json'


############################################################
# Pomožne funkcije za vnos
############################################################


def vnesi_stevilo(x):
    while True:
        try:
            stevilo = input(x)
            return int(stevilo)
        except ValueError:
            print("Prosim, da vnesete število!")
        

def izberi(seznam):
    if len(seznam) == 1:
        opis, element = seznam[0]
        print(f"Na voljo je samo {opis}.")
        return element
    for indeks, (opis, _) in enumerate(seznam, 1):
        print(f"{indeks}) {opis}")
    while True:
        izbira = vnesi_stevilo("> ")
        if 1 <= izbira <= len(seznam):
            _, element = seznam[izbira - 1]
            return element
        else:
            print(f"Izberi število med 1 in {len(seznam)}")


############################################################
# tekstovni vmesnik
############################################################


def tekstovni_vmesnik():
    print('Pozdravljeni!')

    while True:
        try:
            print('S čim se želiš ukvarjati? Izberi.')
            moznosti = [
                ("recepti", pokazi_recepte),
                ("listkom", pokazi_listek),
                ("napisati recept", napisi_recept),
                ("pogledati recept", poglej_recept),
                ("urediti recept", uredi_recept),
                ("izbrisati recept", izbrisi_recept),
                ("dodati element", dodaj_element),
                ("izbrisati listek", izbrisi_listek)
            ]
            izbira = izberi(moznosti)
            print(30 * "-")
            izbira()
            print()
            #model.shrani_recepte(IME_DATOTEKE)
            #model.shrani_elemente(IME_DATOTEKE)

        except ValueError as e:
            print(e.args[0])

        except KeyboardInterrupt:
            print()
            print("Nasvidenje!")
            return




def pokazi_recepte():
    for (ime, velikost, sestavine, postopek) in model.knjiznica:
        print(ime)


def pokazi_listek():
    for (ime, kolicina, enota) in model.listek:
        print(ime)


def napisi_recept():
    ime = input('Ime recepta> ')
    velikost = input('Velikost> ')
    sestavine = input('Sestavine> ')
    postopek = input('Postopek> ')
    model.knjiznica.append((ime, velikost, sestavine, postopek))



def poglej_recept():
    recepti = []
    for recept in model.knjiznica:
        recepti.append((recept[0], recept))
        print(recept[0])

    print("Izberi recept, ki ga želiš pogledati.")
    izbran_recept = izberi(recepti)

    print(f"Ime: {izbran_recept[0]}")
    print(f"Velikost: {izbran_recept[1]}")
    print(f"Sestavine: {izbran_recept[2]}")
    print(f"Postopek: {izbran_recept[3]}")


def uredi_recept():
    recepti = []
    indeksi = {}
    indeks = 0
    for recept in model.knjiznica:
        recepti.append((recept[0], recept))
        indeksi[recept] = indeks
        indeks += 1
        print(recept[0])

    print("Kateri recept želiš urediti?")
    izbran_recept = izberi(recepti)

    print("Kaj želiš urediti?")
    moznosti = [
        ("ime", uredi_ime),
        ("velikost", uredi_velikost),
        ("sestavine", uredi_sestavine),
        ("postopek", uredi_postopek)
    ]
    izbira = izberi(moznosti)
    izbira(izbran_recept)

    #tuki si moram nekako zrihtat sharanjevanje v model...


def uredi_ime(recept):
    print(recept[0])
    ime = input('Novo ime> ')
    recept = (ime, recept[1], recept[2], recept[3])

def uredi_velikost(recept):
    print(recept[1])
    velikost = input('Nova velikost> ')
    recept = (recept[0], velikost, recept[2], recept[3])

def uredi_sestavine(recept):
    print(recept[2])
    sestavine = input('Nove sestavine> ')
    recept = (recept[0], recept[1], sestavine, recept[3])

def uredi_postopek(recept):
    print(recept[3])
    postopek = input('Nov postopek> ')
    recept = (recept[0], recept[1], recept[2], postopek)




def izbrisi_recept():
    pass


def dodaj_element():
    ime = input('Ime elementa> ')
    kolicina = input('Količina> ')
    enota = input('Enota> ')
    model.listek.append((ime, kolicina, enota))


def izbrisi_listek():
    if (
        input(f"Ali si prepričan, da želiš izbrisati listek? [da/ne]") == "da"
    ):
        model.izbrisi_listek()
        print("Listek je bil uspešno izbrisan.")
    else:
        print("Brisanje je bilo preklicano, listek ostaja nespremenjen.")



tekstovni_vmesnik()