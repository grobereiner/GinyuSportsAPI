import requests

welcome = "BIENVENIDO A LAS FUERZAS DEPORTIVAS GINYU"
error_ADMIN = "SERVICIO DE ADMIN EN MANTENIMIENTO"
error_SEARCH = "SERVICIO DE BUSQUEDA EN MANTENIMIENTO"

def home():
    return welcome

def admin(prompt):
    try:
        resp = requests.get(url="http://127.0.0.1:5001/"+prompt)
        return resp.text
    except  requests.exceptions.ConnectionError:
        return error_ADMIN

def search(query):
    try:
        resp = requests.get(url="http://127.0.0.1:5002/"+query)
        return resp.text
    except requests.exceptions.ConnectionError:
        return error_SEARCH