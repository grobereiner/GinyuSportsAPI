import requests

def busqueda():
    print("HACEMOS UNA BUSQUEDA TOTAL DE RESULTADOS:")
    resp = requests.get(url="http://127.0.0.1:5000/search/Cualquiera")
    print(resp.text)

def insercion():
    resultado = input("Hacemos una insercion, ingrese un resultado: ")
    resp = requests.get(url=("http://127.0.0.1:5000/admin/"+resultado))
    print(resp.text)