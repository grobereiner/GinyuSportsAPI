from flask import Flask
import requests

app = Flask(__name__)

welcome = "BIENVENIDO A LAS FUERZAS DEPORTIVAS GINYU"
error_ADMIN = "SERVICIO DE ADMIN EN MANTENIMIENTO"
error_SEARCH = "SERVICIO DE BUSQUEDA EN MANTENIMIENTO"

@app.route("/")
def home():
    return welcome

@app.route("/admin/<prompt>")
def admin(prompt):
    try:
        resp = requests.get(url="http://127.0.0.1:5001/"+prompt)
        return resp.text
    except:
        return error_ADMIN


@app.route("/search/<query>")
def search(query):
    try:
        resp = requests.get(url="http://127.0.0.1:5002/"+query)
        return resp.text
    except:
        return error_SEARCH

app.run(port=5000)