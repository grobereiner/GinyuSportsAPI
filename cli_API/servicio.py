import requests
import controlador

resp = None
errorNoHost = "EN ESTE MOMENTO NO HAY SERVICIO TOTAL"
terminar = 1
while terminar == 1:
    try:
        resp = requests.get(url="http://127.0.0.1:5000/")
        print(resp.text)
        break
    except:
        print(errorNoHost)
        terminar = int(input("INGRESE 1 PARA RECONECTAR: "))
        if terminar != 1:
            exit(0)


controlador.validation()

opcion = 0
while opcion != 9:
    opcion = int(input("INGRESE 1 PARA BUSCAR TODO, 2 PARA INSERTAR NUEVOS DATOS, 3 PARA HACER SIGN OUT y 9 PARA SALIR: "))
    if opcion == 1:
        controlador.busqueda()
    elif opcion == 2:
        controlador.insercion()
    elif opcion == 3:
        controlador.signout()
        controlador.validation()
    