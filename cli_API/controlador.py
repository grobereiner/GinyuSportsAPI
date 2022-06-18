import requests
import re

def validation():
    while True:
        print("VALIDATION \n Ingrese 1 para registrarse \n Ingrese 2 para acceder a su cuenta")
        opcion = int(input(""))
        while True:
            email = input("Ingrese su email: ")
            email_regex = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+(\.[a-z]{1,3})+$"
            if re.match(email_regex, email):
                break
            else:
                print("Ingrese un email válido")
        password = input("Ingrese su contraseña: ")
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

def busqueda(token):
    print("HACEMOS UNA BUSQUEDA TOTAL DE RESULTADOS:")
    resp = requests.get(url="http://127.0.0.1:5000/search/Cualquiera", headers = {"jwt_token": token})
    print(resp.text+'\n')

def insercion(token):
    resultado = input("Hacemos una insercion, ingrese un resultado: ")
    resp = requests.get(url=("http://127.0.0.1:5000/admin/"+resultado), headers={"jwt_token" : token})
    print(resp.text+'\n')