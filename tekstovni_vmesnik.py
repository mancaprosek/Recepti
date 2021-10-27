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
            print(f"Izberi število med 1 in {len(seznam)}.")


def tvori_seznam(seznam):
    recepti = []
    indeksi = {}
    indeks = 0
    for recept in seznam:
        recepti.append((recept[0], recept))
        indeksi[recept] = indeks
        indeks += 1
        print(recept[0])
    return recepti

def pridobi_indeks(sez):
    ind = {}
    indeks = 0
    for x in sez:
        ind[x] = indeks
        indeks += 1
        return ind

############################################################
# Pomožne funkcije za urejanje
############################################################


def uredi_ime1(recept):
    print(recept[0])
    ime = input('Novo ime> ')
    return ime, recept[1], recept[2], recept[3]

def uredi_velikost1(recept):
    print(recept[1])
    velikost = input('Nova velikost> ')
    return (recept[0], velikost, recept[2], recept[3])

def uredi_sestavine1(recept):
    print(recept[2])
    sestavine = input('Nove sestavine> ')
    return (recept[0], recept[1], sestavine, recept[3])
    

def uredi_postopek1(recept):
    print(recept[3])
    postopek = input('Nov postopek> ')
    return (recept[0], recept[1], recept[2], postopek)

#Narejene so funkcije za urejanje, ki jih je samo veliko.
#A bi to morala združit, kako bi to združila?

def uredi_ime2(element):
    print(element[0])
    ime = input('Novo ime> ')
    return (ime, element[1], element[2])

def uredi_velikost2(element):
    print(element[1])
    velikost = input('Nova velikost> ')
    return (element[0], velikost, element[2])

def uredi_enoto2(element):
    print(element[2])
    enota = input('Nova enota> ')
    return (element[0], element[1], enota)


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
                ("pogledati element", poglej_element),
                ("urediti element", uredi_element),
                ("izbrisati element", izbrisi_element),
                ("izbrisati listek", izbrisi_listek)
            ]
            izbira = izberi(moznosti)
            print(30 * "-")
            izbira()
            print()
            model.shrani(IME_DATOTEKE)

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
    model.napisi_recept(ime, velikost, sestavine, postopek)


def poglej_recept():
    recepti = tvori_seznam(model.knjiznica)

    if recepti == []:
        print("Knjižnica receptov je prazna.")
    else:
        print("Izberi recept, ki ga želiš pogledati.")
        izbran_recept = izberi(recepti)

        print(f"Ime: {izbran_recept[0]}")
        print(f"Velikost: {izbran_recept[1]}")
        print(f"Sestavine: {izbran_recept[2]}")
        print(f"Postopek: {izbran_recept[3]}")


def uredi_recept():
    recepti = tvori_seznam(model.knjiznica)
    indeksi = pridobi_indeks(model.knjiznica)

    if recepti == []:
        print("Knjižnica receptov je prazna.")
    else:
        print("Kateri recept želiš urediti?")
        izbran_recept = izberi(recepti)

        print("Kaj želiš urediti?")
        moznosti = [
            ("ime", uredi_ime1),
            ("velikost", uredi_velikost1),
            ("sestavine", uredi_sestavine1),
            ("postopek", uredi_postopek1)
        ]
        izbira = izberi(moznosti)
        ime, velikost, sestavine, postopek = izbira(izbran_recept)

        model.izbrisi_recept(indeksi[izbran_recept])
        model.napisi_recept(ime, velikost, sestavine, postopek)


def izbrisi_recept():
    recepti = tvori_seznam(model.knjiznica)
    indeksi = pridobi_indeks(model.knjiznica)

    if recepti == []:
        print("Knjižnica receptov je prazna.")

    else:
        print("Kateri recept želiš izbrisati?")
        izbran_recept = izberi(recepti)
        i = indeksi[izbran_recept]

        if (
            input(f"Ali si prepričan, da želiš izbrisati recept {izbran_recept[0]}? [da/ne]") == "da"
        ):
            model.izbrisi_recept(i)
            print(f"Recept {izbran_recept[0]} je bil uspešno izbrisan.")
        else:
            print("Brisanje je bilo preklicano, recept ostaja shranjen.")




def dodaj_element():
    ime = input('Ime elementa> ')
    kolicina = input('Količina> ')
    enota = input('Enota> ')
    model.listek.append((ime, kolicina, enota))


def poglej_element():
    elementi = tvori_seznam(model.listek)

    if elementi == []:
        print("Na listku ni nobenih elementov.")
    else:
        print("Izberi element, ki ga želiš pogledati.")
        izbran_element = izberi(elementi)

        print(f"Ime: {izbran_element[0]}")
        print(f"Velikost: {izbran_element[1]}")
        print(f"Enote: {izbran_element[2]}")


def uredi_element():
    elementi = tvori_seznam(model.listek)
    indeksi = pridobi_indeks(model.listek)

    if elementi == []:
        print("Na listku ni nobenih elementov.")
    else:
        print("Kateri element želiš urediti?")
        izbran_element = izberi(elementi)

        print("Kaj želiš urediti?")
        moznosti = [
            ("ime", uredi_ime2),
            ("velikost", uredi_velikost2),
            ("enota", uredi_enoto2)
        ]
        izbira = izberi(moznosti)
        ime, velikost, enota = izbira(izbran_element)

        model.izbrisi_element(indeksi[izbran_element])
        model.dodaj_element(ime, velikost, enota)


def izbrisi_element():
    elementi = tvori_seznam(model.listek)
    indeksi = pridobi_indeks(model.listek)
    
    if elementi == []:
        print("Na listku ni nobenih elementov.")
    else:
        print("Kateri element želiš izbrisati?")
        izbran_element = izberi(elementi)
        i = indeksi[izbran_element]

        if (
            input(f"Ali si prepričan, da želiš izbrisati element {izbran_element[0]}? [da/ne]") == "da"
        ):
            model.izbrisi_element(i)
            print(f"Element {izbran_element[0]} je bil uspešno izbrisan.")
        else:
            print(f"Brisanje je bilo preklicano, element {izbran_element[0]} ostaja shranjen.")


def izbrisi_listek():
    if (
        input(f"Ali si prepričan, da želiš izbrisati listek? [da/ne]") == "da"
    ):
        model.izbrisi_listek()
        print("Listek je bil uspešno izbrisan.")
    else:
        print("Brisanje je bilo preklicano, listek ostaja nespremenjen.")



tekstovni_vmesnik()