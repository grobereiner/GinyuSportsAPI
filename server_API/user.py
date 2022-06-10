from flask import redirect, session
from passlib.hash import pbkdf2_sha256
# from functools import wraps
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.login


class User:
    def start_session(self, user):
        session['logged_in'] = True
        session['user'] = user
        # return redirect('/logged')

    def signup(self, email, password):
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
            self.start_session(user["email"])
            return "Signup success, logged in"

        return "Signup failed"

    def signout(self):
        session.clear()
        return "Signed out"

    def login(self, email, password):
        user = db.users.find_one({
            "email": email
        })

        if user and pbkdf2_sha256.verify(password, user['password']):
            self.start_session(email)
            return "Login success"
            
        return "Invalid login credentials"

