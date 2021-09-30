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
    uvodni_pozdrav()
    while True:
        try:
            print('Izberi eno od možnosti.')
            moznosti1 = [
                ("recepti", pokazi_recepte),
                ("listek", pokazi_listek)
            ]
            izbira1 = izberi(moznosti1)
            print(30 * "-")
            izbira1()
            print()

            if izbira1() == pokazi_recepte:
                print("Kaj želiš storiti?")
                print("Izberi možnost.")
                moznosti2 = [
                    ("napisati recept", napisi_recept),
                    ("urediti recept", uredi_recept),
                    ("pogledati recept", poglej_recept)
                ]
                izbira2 = izberi(moznosti2)
                print(30 * "-")
                izbira2()
                print()
                model.shrani_recepte(IME_DATOTEKE)

            elif izbira1() == pokazi_listek:
                print("Kaj želiš storiti?")
                print("Izberi možnost.")
                moznosti2 = [
                    ("dodati element", dodaj_element),
                    ("izbrisati listek", izbrisi_listek),
                ]
                izbira2 = izberi(moznosti2)
                print(30 * "-")
                izbira2()
                print()
                model.shrani_elemente(IME_DATOTEKE)

        except ValueError as e:
            print(e.args[0])

        except KeyboardInterrupt:
            print()
            print("Nasvidenje!")
            return



def uvodni_pozdrav():
    print('Pozdravljeni!')



def pokazi_recepte():
    pass


def pokazi_listek():
    pass


def napisi_recept():
    ime = input('Ime recepta> ')
    velikost = input('Velikost> ')
    sestavine = input('Sestavine> ')
    postopek = input('Postopek> ')
    model.knjiznica.append((ime, velikost, sestavine, postopek))


def uredi_recept():
    pass


def poglej_recept():
    print("Izberi recept, ki ga želiš pogledati.")
    izbran_recept = izberi(model.knjiznica)    
    (ime, velikost, sestavine, postopek) = izbran_recept()

    print("Ime: {ime}")
    print("Velikost: {velikost}")
    print("Sestavine: {sestavine}")
    print("Postopek: {postopek}")




def dodaj_element():
    ime = input('Ime elementa> ')
    kolicina = input('Količina> ')
    enota = input('Enota> ')
    model.listek.dodaj_element(ime, kolicina, enota)


def izbrisi_listek():
    if (
        input(f"Ali si prepričan, da želiš izbrisati listek? [da/ne]") == "da"
    ):
        model.izbrisi_listek(model.listek)
        print("Listek je bil uspešno izbrisan.")
    else:
        print("Brisanje je bilo preklicano, listek ostaja nespremenjen.")



tekstovni_vmesnik()