import bottle

from model2 import Model
IME_DATOTEKE = 'stanje.json'
model = Model(IME_DATOTEKE)

#mata to!
 
@bottle.get('/')
def osnovna_stran():
    return bottle.template("osnovna_stran.html", recepti=model.knjiznica)

@bottle.post('/dodaj_recept')
def dodaj_recept():
    ime = bottle.request.forms['ime']
    velikost = bottle.request.forms['velikost']
    postopek = bottle.request.forms['postopek']
    print(ime)

    recept = model.dodaj_recept(ime, velikost, {}, postopek)
    tr_st_sestavin = 1
    while True:
        print("in")
        try:
            ime_sestavine = bottle.request.forms['ime_sestavine_' + str(tr_st_sestavin)]
            kolicina_sestavine = bottle.request.forms['kolicina_sestavine_' + str(tr_st_sestavin)]
            enota_sestavine = bottle.request.forms['enota_sestavine_' + str(tr_st_sestavin)]
            recept.dodaj_sestavino(ime_sestavine, kolicina_sestavine, enota_sestavine)
        except:
            break
        tr_st_sestavin += 1
    model.shrani(IME_DATOTEKE)
    bottle.redirect('/')

@bottle.post('/izbrisi_recept/<id:path>')
def izbrisi_recept(id):
    model.izbrisi_recept_id(id)
    print(id)
    model.shrani(IME_DATOTEKE)   
    bottle.redirect('/')


@bottle.get('/uredi_recept/<id:path>')
def uredi_recepti(id):
    print(id)
    for recept in model.knjiznica:
        if recept.id == int(id):
            return bottle.template("uredi_recept.html", recept=recept)
    bottle.redirect('/')

@bottle.post('/uredi_recept/<id:path>')
def uredi_recepti(id):
    print(id)
    for recept in model.knjiznica:
        if recept.id == int(id):
            recept.ime = bottle.request.forms['ime']
            recept.velikost = bottle.request.forms['velikost']
            recept.postopek = bottle.request.forms['postopek']

            recept.sestavine = {}
            tr_st_sestavin = 1
            while True:
                print("in")
                try:
                    ime_sestavine = bottle.request.forms['ime_sestavine_' + str(tr_st_sestavin)]
                    kolicina_sestavine = bottle.request.forms['kolicina_sestavine_' + str(tr_st_sestavin)]
                    enota_sestavine = bottle.request.forms['enota_sestavine_' + str(tr_st_sestavin)]
                    recept.dodaj_sestavino(ime_sestavine, kolicina_sestavine, enota_sestavine)
                except:
                    break
                tr_st_sestavin += 1


            break
    model.shrani(IME_DATOTEKE)
    bottle.redirect('/')

bottle.run(reloader=True, debug=True)