import bottle
import os

from model import Model
model = Model('stanje.json')
SECRET = 'manca'



def nalozi_stanje(uporabnisko_ime):
    if uporabnisko_ime:
        return model.nalozi(uporabnisko_ime + ".json")
    else:
        bottle.redirect('/prijava')


def shrani_stanje():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SECRET)
    model.shrani(uporabnisko_ime)




@bottle.get('/')
def osnovna_stran():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SECRET)
    stanje = nalozi_stanje(uporabnisko_ime)
    return bottle.template("osnovna_stran.html", recepti=stanje)




@bottle.get('/registracija')
def registracija_get():
    return bottle.template("prijava_registracija.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post('/registracija')
def registracija_post():
    model = Model('stanje.json')
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if os.path.exists(str(uporabnisko_ime)):
        napake = {"uporabnisko_ime": "Uporabniško ime je že zasedeno."}
        return bottle.template("prijava_registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path='/', secret=SECRET)
        model.shrani(uporabnisko_ime + ".json")
        bottle.redirect('/')



@bottle.get('/prijava')
def prijava_get():
    return bottle.template("prijava_registracija.html", napake={}, polja={}, uporabnisko_ime=None)


@bottle.post('/prijava')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    if not os.path.exists(str(uporabnisko_ime + ".json")):
        napake = {"uporabnisko_ime": "Uporabniško ime ne obstaja."}
        return bottle.template("prijava_registracija.html", napake=napake, polja={"uporabnisko_ime": uporabnisko_ime}, uporabnisko_ime=None)
    else:
        bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path='/', secret=SECRET)
        bottle.redirect('/')



@bottle.post('/odjava')
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path='/', secret=SECRET)
    bottle.redirect('/')





@bottle.post('/dodaj_recept')
def dodaj_recept():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SECRET)
    ime = bottle.request.forms['ime']
    velikost = bottle.request.forms['velikost']
    postopek = bottle.request.forms['postopek']
    print(ime)

    recept = model.dodaj_recept(ime, velikost, {}, postopek)
    tr_st_sestavin = 1
    while True:
        try:
            ime_sestavine = bottle.request.forms['ime_sestavine_' + str(tr_st_sestavin)]
            kolicina_sestavine = bottle.request.forms['kolicina_sestavine_' + str(tr_st_sestavin)]
            enota_sestavine = bottle.request.forms['enota_sestavine_' + str(tr_st_sestavin)]
            recept.dodaj_sestavino(ime_sestavine, kolicina_sestavine, enota_sestavine)
        except:
            break
        tr_st_sestavin += 1
    model.shrani(uporabnisko_ime + ".json")
    bottle.redirect('/')


@bottle.post('/izbrisi_recept/<id:path>')
def izbrisi_recept(id):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SECRET)
    model.izbrisi_recept_id(id)
    model.shrani(uporabnisko_ime + ".json")   
    bottle.redirect('/')



@bottle.get('/poglej_recept/<id:path>')
def poglej_recept(id):
    for recept in model.knjiznica:
        if recept.id == int(id):
            return bottle.template("poglej_recept.html", recept=recept)
    bottle.redirect('/')



@bottle.get('/uredi_recept/<id:path>')
def uredi_recept(id):
    for recept in model.knjiznica:
        if recept.id == int(id):
            return bottle.template("uredi_recept.html", recept=recept)
    bottle.redirect('/')

@bottle.post('/uredi_recept/<id:path>')
def uredi_recept(id):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SECRET)
    for recept in model.knjiznica:
        if recept.id == int(id):
            recept.ime = bottle.request.forms['ime']
            recept.velikost = bottle.request.forms['velikost']
            recept.postopek = bottle.request.forms['postopek']

            recept.sestavine = {}
            tr_st_sestavin = 1
            while True:
                try:
                    ime_sestavine = bottle.request.forms['ime_sestavine_' + str(tr_st_sestavin)]
                    kolicina_sestavine = bottle.request.forms['kolicina_sestavine_' + str(tr_st_sestavin)]
                    enota_sestavine = bottle.request.forms['enota_sestavine_' + str(tr_st_sestavin)]
                    recept.dodaj_sestavino(ime_sestavine, kolicina_sestavine, enota_sestavine)
                except:
                    break
                tr_st_sestavin += 1


            break
    model.shrani(uporabnisko_ime + ".json")
    bottle.redirect('/')



@bottle.get('/spremeni_velikost/<id:path>')
def spremeni_velikost(id):
    for recept in model.knjiznica:
        if recept.id == int(id):
            return bottle.template("spremeni_velikost.html", recept=recept)
    bottle.redirect('/')


@bottle.post('/spremeni_velikost/<id:path>')
def spremeni_velikost(id):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SECRET)
    for recept in model.knjiznica:
        if recept.id == int(id):
            stara_velikost = recept.velikost
            recept.velikost = bottle.request.forms['velikost']
            i = int(recept.velikost) / int(stara_velikost)

            for ime_sestavine in recept.sestavine.keys():
                nova_kolicina = int(recept.sestavine[ime_sestavine][0]) * i
                recept.sestavine[ime_sestavine][0] = str(round(nova_kolicina))


            break

    model.shrani(uporabnisko_ime + ".json")
    bottle.redirect('/')




bottle.run(reloader=True, debug=True)