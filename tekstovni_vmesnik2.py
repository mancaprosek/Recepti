from model2 import Model, Recept, Sestavina

IME_DATOTEKE = 'stanje.json'
model = Model.nalozi(IME_DATOTEKE)


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
    for recept in seznam:
        recepti.append((recept[0], recept))
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



############################################################
# tekstovni vmesnik
############################################################


def tekstovni_vmesnik():
    print('Pozdravljeni!')
    while True:
        try:
            print(30 * "-")
            prikazi_knjiznico()
            print('Kaj želiš storiti?')
            moznosti = [
                ("dodati recept", dodaj_recept),
                ("pogledati recept", poglej_recept),
                ("urediti recept", uredi_recept),
                ("izbrisati recept", izbrisi_recept),
                ("dodati sestavine", dodaj_sestavine)
                ]
            izbira = izberi(moznosti)
            print(30 * "-")
            izbira()
            print()
            Model.shrani(IME_DATOTEKE)

        except ValueError as e:
            print(e.args[0])

        except KeyboardInterrupt:
            print()
            print("Nasvidenje!")
            return



def prikazi_knjiznico():
    if model.knjiznica != []:
        print('Recepti:')
        for (ime, velikost, sestavine, postopek) in model.knjiznica:
            print(ime)
        print()
        print(30 * "-")
        


def dodaj_recept():
    ime = input('Ime recepta> ')
    velikost = vnesi_stevilo('Velikost> ')
    sestavine = {}

    ime_sestavine = input('Ime sestavine> ')
    kolicina_sestavine = vnesi_stevilo('Količina sestavine>')
    enota_sestavine = input('Enota sestavine> ')
    sestavine[ime_sestavine] = (kolicina_sestavine, enota_sestavine)

    while (input(f"Ali bi dodal še eno sestavino? [da/ne]") == "da"):
            ime_sestavine1 = input('Ime sestavine> ')
            kolicina_sestavine1 = vnesi_stevilo('Količina sestavine> ')
            enota_sestavine1 = input('Enota sestavine> ')
            sestavine[ime_sestavine1] = (kolicina_sestavine1, enota_sestavine1)

    postopek = input('Postopek> ')
    model.dodaj_recept(ime, velikost, sestavine, postopek)



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

    #tuki se neki pr indeksih zatakne, kao da je unhashable... ne stekam čist..

    if recepti == []:
        print("Knjižnica receptov je prazna.")
    else:
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
        ime, velikost, sestavine, postopek = izbira(izbran_recept)

        model.izbrisi_recept(indeksi[izbran_recept])
        model.dodaj_recept(ime, velikost, sestavine, postopek)


def dodaj_sestavine():
    recepti = tvori_seznam(model.knjiznica)
    indeksi = pridobi_indeks(model.knjiznica)

    if recepti == []:
        print("Ni recepta, ki bi mu lahko dodal sestavine.")

    else:
        print("Kateremu receptu želiš dodati sestavine?")
        izbran_recept = izberi(recepti)
        i = indeksi[izbran_recept]

        ime = input('Ime sestavine> ')
        kolicina = vnesi_stevilo('Količina> ')
        enota = input('Enota> ')
        Recept.dodaj_sestavino(izbran_recept, ime, kolicina, enota)

        while (input(f"Ali bi dodal še eno sestavino? [da/ne]") == "da"):
            ime = input('Ime sestavine> ')
            kolicina = vnesi_stevilo('Količina> ')
            enota = input('Enota> ')
            Recept.dodaj_sestavino(izbran_recept, ime, kolicina, enota)
    
#TUKI napiše   File "c:\Users\manca\OneDrive\FMF\Recepti\Recepti\model2.py", line 30, in dodaj_sestavino
#     self.sestavine[ime] = (kolicina, enota)
# AttributeError: 'tuple' object has no attribute 'sestavine'

#########################################
##### Funkcije za urejanje receptov #####

def uredi_ime(recept):
    print(recept[0])
    ime = input('Novo ime> ')
    return ime, recept[1], recept[2], recept[3]


def uredi_velikost(recept):
    print(recept[1])
    stara_velikost = recept[1]
    nova_velikost = vnesi_stevilo("Nova velikost> ")
    slovar_sestavin = recept[2]
    #to zaenkrat še ni slovar! ni še zrihtan!!

    i = int(nova_velikost) / int(stara_velikost)

    for sestavina in slovar_sestavin.keys():
        stara_kolicina = slovar_sestavin[sestavina]
        slovar_sestavin[sestavina] = int(stara_kolicina) * i

    return recept[0], nova_velikost, slovar_sestavin, recept[3]


def uredi_sestavine(recept):
    for ime in recept[2].keys():
        print(ime)
    print('Katero sestavino želiš urediti?')
    ime = input('Vnesi ime:> ')
    novo_ime = input('Vnesi novo ime:> ')
    nova_kolicina = input('Vnesi novo količino:> ')
    nova_enota = input('Vnesi novo enoto:>')
    recept[2].pop(ime)
    recept[2][novo_ime] = (nova_kolicina, nova_enota)
    return recept[0], recept[1], recept[2], recept[3]

#tuki isto ne dovoli za slovar


def uredi_postopek(recept):
    print(recept[3])
    postopek = input('Nov postopek> ')
    return recept[0], recept[1], recept[2], postopek

#########################################


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


tekstovni_vmesnik()

#Razredov ne zazna, to z modelom povezan ne štekam
#pri dodajanju sestavin neki ni zadovoljen
#dodajanje sestavin je še uganka, da bo lepo slovar