from flask import Flask, request, send_file
import bmqueue

cache_file = "cache.csv"

app = Flask(__name__)

bmq = bmqueue.BMQueue()

@app.route("/recibir", methods = ['POST'])
def recibir():
    result = str(request.get_data(cache=False, as_text=True))
    # with open(cache_file, "a") as f:
    #     f.write(result)
    #     f.close()
    bmq.enqueue(result)
    return ""

@app.route("/enviar")
def enviar():
    # texto = None
    # with open(cache_file, "r") as f:
    #     texto = f.read()
    #     f.close()
    # open(cache_file, "w").close()
    texto = bmq.dequeue()
    return texto


app.run(port = 5009)
