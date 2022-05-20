import requests
import controlador

resp = None
errorNoHost = "EN ESTE MOMENTO NO HAY SERVICIO TOTAL"
terminar = 1
while terminar == 1:
    try:
        resp = requests.get(url="http://127.0.0.1:5000/")
        break
    except:
        print(errorNoHost)
        terminar = int(input("INGRESE 1 PARA RECONECTAR: "))
        if terminar != 1:
            exit(0)

terminar = 0
while terminar != 1:
    controlador.busqueda()
    controlador.insercion()
    terminar = int(input("SI YA NO QUIERE REPETIR, PRESIONE 1"))