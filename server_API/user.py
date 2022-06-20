from flask import session
from passlib.hash import pbkdf2_sha256
import pymongo
import jwt
import datetime
from Gmail.gmail import send_token_email

client = pymongo.MongoClient('localhost', 27017)
db = client.login


class User:
    def signup(self, email, password, secret_key):
        # Create the user object
        user = {
            "email": email,
            "password": password
        }

    # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            return "Email already exists"

        if db.users.insert_one(user):
            token = jwt.encode({"user": user["email"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, secret_key)
            send_token_email(token, user["email"])
            return "Signup success, logged in"

        return "Signup failed"

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

