from passlib.hash import pbkdf2_sha256
import pymongo
import jwt
import datetime
from Gmail.gmail import send_token_email
import re
import certifi

ca = certifi.where()

client = pymongo.MongoClient(
    "mongodb+srv://earr99:LnEX8MnvCm7ZEwEH@ginyusportsapi.jva4j.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.login


class User:
    def signup(self, email, password, secret_key):
        email_regex = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+(\.[a-z]{1,3})+$"
        # Revisando que el email sea válido - igual no deberían llegar emails no válidos,
        # pero si alguien tiene acceso al mismo puerto con otro programa, podría registrar
        # emails no válidos y generar problemas
        if re.match(email_regex, email):
            # Se crea el dict user
            user = {
                "email": email,
                "password": password
            }

            # Enciptar password
            user['password'] = pbkdf2_sha256.encrypt(user['password'])

            # Check si email ya existe
            if db.users.find_one({"email": user['email']}):
                return "Email already exists"

            if db.users.insert_one(user):
                token = jwt.encode({"user": user["email"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, secret_key)
                send_token_email(token, user["email"])
                return "Signup success, logged in"

            return "Signup failed"
            
        return "Email inválido"

    def signout(self):
        return "Signed out"

    def login(self, email, password, secret_key):
        user = db.users.find_one({
            "email": email
        })

        if user and pbkdf2_sha256.verify(password, user['password']):
            token = jwt.encode({"user" : user["email"], "exp" : datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, secret_key)
            send_token_email(token, user["email"])
            return "Login success"
            
        return "Invalid login credentials"

