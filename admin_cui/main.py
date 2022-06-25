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


email = controlador.validation()

token = input("Ingrese el token que se le ha enviado al correo que proporciono: ")
opcion = 0
while opcion != 9:
    opcion = int(input("INGRESE 1 PARA BUSCAR TODO, 2 PARA INSERTAR NUEVOS DATOS, 3 PARA HACER SIGN OUT y 9 PARA SALIR: "))
    if opcion == 1:
        controlador.busqueda(token, email)
    elif opcion == 2:
        controlador.insercion(token, email)
    elif opcion == 3:
        controlador.signout()
        controlador.validation()
        token = input("Ingrese el token que se le ha enviado al correo que proporcionó: ")

    