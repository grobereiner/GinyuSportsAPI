"""
from flask import Flask, jsonify, session, redirect
from passlib.hash import pbkdf2_sha256
from validation import db

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        _email = input("Insert your email: ")
        _password = input("Insert your password: ")
        # Create the user object
        user = {
          "email": _email,
          "password": _password
        }

    # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
        if db.users.find_one({ "email": user['email'] }):
            return jsonify({ "error": "Email address already in use" }), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({ "error": "Signup failed" }), 400
  
    def signout(self):
        session.clear()
        return redirect('/')
  
    def login(self):
        _email = input("Insert your email: ")
        _password = input("Insert your password: ")
        user = db.users.find_one({
        "email": _email
        })

        if user and pbkdf2_sha256.verify(_password, user['password']):
            return self.start_session(user)
        
        return jsonify({ "error": "Invalid login credentials" }), 401
"""