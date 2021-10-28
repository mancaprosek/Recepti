import bottle

from model2 import Model
model = Model()

@bottle.get('/')
def osnovna_stran():
    return bottle.template("osnovna_stran.html", recepti=model.knjiznica)


bottle.run(reloader=True, debug=True)