import bottle

from model import Model, Recept

model = Model()


@bottle.get('/')
def osnovna_stran():
    return bottle.template(
        "osnovna_stran.html", recepti=model.knjiznica, listek=model.listek
        )


bottle.run(reloader=True, debug=True)