import bottle
import requests
import json
#estilos
@bottle.route('/css/:filename#.*#')
def send_static(filename):
    return bottle.static_file(filename, root='./css')

#pagina principal
@bottle.route('/')
def home_page():
    return bottle.template("index2")


#eleccion de clasificacion y liga a escojer
@bottle.route('/clasificacion')
def home_page():
    return bottle.template('clasificacion')

@bottle.route('/respuesta', method='POST')
def respuesta():
    clasificacion = bottle.request.forms.get("clasificacion")
    respuesta = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", 
                params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"json", 
                          "req":"tables", "league":clasificacion}) 
    numpartidos=len((json.loads(respuesta.text)["table"]))
    numero=int(numpartidos)
    equipos = []
    for i in xrange(numero):
        equipos.append([])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["team"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["points"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["wins"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["draws"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["losses"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["gf"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["ga"])
        equipos[i].append(json.loads(respuesta.text)["table"][i]["avg"])
                
    return bottle.template('respuesta',equipos=equipos)
#eleccion de rsultados y eleccion de liga
@bottle.route('/resultado')
def home_page():
    return bottle.template("resultado")


@bottle.route('/respuestaresul', method='POST')
def respuesta():
    resultado = bottle.request.forms.get("resultado")
    num_liga = bottle.request.forms.get("num_liga")
    resultados= requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"json", "req":"matchs", "league":resultado,"round":num_liga, "group":"1"})
    rondas = []
    numpartidos=len((json.loads(resultados.text)["match"]))
    numero=int(numpartidos)
    for i in xrange(numero):
        rondas.append([])
        rondas[i].append(json.loads(resultados.text)["match"][i]["round"])
        rondas[i].append(json.loads(resultados.text)["match"][i]["local"])
        rondas[i].append(json.loads(resultados.text)["match"][i]["visitor"])
        rondas[i].append(json.loads(resultados.text)["match"][i]["date"])
        rondas[i].append(json.loads(resultados.text)["match"][i]["hour"])
        rondas[i].append(json.loads(resultados.text)["match"][i]["minute"])
        rondas[i].append(json.loads(resultados.text)["match"][i]["result"])
       
    return bottle.template('respuestaresul',rondas=rondas)
bottle.run(host="localhost", port=8080)

