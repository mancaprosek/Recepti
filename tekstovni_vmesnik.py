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

#Pri poglej in uredi napiše, da je pričakoval 2 values,
#ampak da jih je too many.. ne štekam? Mejbi bi mogl bit to v modelu?

def poglej_recept():
    print("Izberi recept, ki ga želiš pogledati.")
    recepti = model.knjiznica
    izbran_recept = izberi(recepti)    
    (ime, velikost, sestavine, postopek) = izbran_recept()

    print("Ime: {ime}")
    print("Velikost: {velikost}")
    print("Sestavine: {sestavine}")
    print("Postopek: {postopek}")


def uredi_recept():
    print("Kateri recept želiš urediti?")
    moznosti1 = model.knjiznica
    recept = izberi(moznosti1)

    print("Kaj želiš urediti?")
    moznosti = [
        ("ime", uredi_ime),
        ("velikost", uredi_velikost),
        ("sestavine", uredi_sestavine),
        ("postopek", uredi_postopek)
    ]
    izbira = izberi(moznosti)
    izbira(recept)

def uredi_ime():
    #tuki bi moglo napisat ime od prej aka da vids kaj je originalno.
    ime = input('Novo ime> ')

#uredi velikost, sestavine in postopek.
#Najprej preveri če ime sploh dela...


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