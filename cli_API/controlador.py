import requests

def validation():
    while True:
        print("VALIDATION \n Ingrese 1 para registrarse \n Ingrese 2 para acceder a su cuenta")
        opcion = int(input(""))
        email = input("Ingrese su email: ")
        password = input("Ingrese su token: ")
        if opcion == 1:
            req = requests.post(url="http://127.0.0.1:5000/signup", data={"email": email, "password": password})
            print(req.text)
            if req.text == "Signup success, logged in":
                break

        elif opcion == 2:
            req = requests.post(url="http://127.0.0.1:5000/login", data={"email": email, "password": password})
            print(req.text)
            if req.text == "Login success":
                break

        else:
            print("Ingrese una opción válida")

def signout():
    resp = requests.get(url="http://127.0.0.1:5000/signout")
    print(resp.text+'\n')

def busqueda():
    print("HACEMOS UNA BUSQUEDA TOTAL DE RESULTADOS:")
    resp = requests.get(url="http://127.0.0.1:5000/search/Cualquiera")
    print(resp.text+'\n')

def insercion():
    resultado = input("Hacemos una insercion, ingrese un resultado: ")
    resp = requests.get(url=("http://127.0.0.1:5000/admin/"+resultado))
    print(resp.text+'\n')