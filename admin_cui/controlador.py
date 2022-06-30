import requests
import re

email_regex = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+(\.[a-z]{1,3})+$"

def email_valido():
    while True:
        email = input("Ingrese su email: ")
        if re.match(email_regex, email):
            return email
        else:
            print("Ingrese un email válido")

def validation():
    while True:
        print("VALIDATION \n Ingrese 1 para registrarse \n Ingrese 2 para acceder a su cuenta")
        opcion = int(input(""))
        email = email_valido()
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

    return email

def signout():
    resp = requests.get(url="http://127.0.0.1:5000/signout")
    print(resp.text+'\n')

def busqueda(token, email):
    print("HACEMOS UNA BUSQUEDA DE RESULTADOS:")
    consulta = input("INGRESE SU CONSULTA (EN LENGUAJE NATURAL - ingles): ")
    resp = requests.get(url="http://127.0.0.1:5000/search/"+consulta, headers = {"jwt_token": token, "email": email})
    print(resp.text+'\n')

def insercion(token, email):
    resultado = input("HACEMOS UNA INSERCION DE RESULTADOS, INGRESAR EL NOMBRE DEL PAIS A OBTENER DATOS DE SU LIGA (en ingles): ")
    resp = requests.get(url=("http://127.0.0.1:5000/admin/"+resultado), headers={"jwt_token": token, "email": email})
    print(resp.text+'\n')