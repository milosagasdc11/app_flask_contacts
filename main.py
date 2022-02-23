#Importamos flask
from crypt import methods
import flask

#Creamos la app de flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hola_ubuntulog():
    return 'Succes!'

#run de appp
app.run()
    
    