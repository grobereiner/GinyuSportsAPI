import requests
import controlador

resp = None
errorNoHost = "EN ESTE MOMENTO NO HAY SERVICIO TOTAL"
try:
    resp = requests.get(url="http://127.0.0.1:5000/")
except:
    print(errorNoHost)
    exit(0)

controlador.busqueda()

controlador.insercion()