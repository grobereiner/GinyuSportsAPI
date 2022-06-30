from flask import Flask, request, send_file
import bmqueue
from flask_wtf import CSRFProtect

cache_file = "cache.csv"

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

bmq = bmqueue.BMQueue()

@app.route("/recibir", methods = ['POST'])
def recibir():
    result = str(request.get_data(cache=False, as_text=True))
    bmq.enqueue(result)
    return ""

@app.route("/enviar")
def enviar():
    texto = bmq.dequeue()
    return texto


app.run(port = 5003, debug=True)
