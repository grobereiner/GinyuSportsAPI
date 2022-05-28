from flask import Flask, jsonify, redirect, session
from passlib.hash import pbkdf2_sha256
from functools import wraps
import pymongo

#import login_routes

app = Flask(__name__)
app.secret_key = b'\xcb\x1a\xa9P\xddF\xc5\xb7\xa8\xe3\x01\xad'

client = pymongo.MongoClient('localhost', 27017)
db = client.login


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        #return jsonify(user), 200
        return redirect('/logged')

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
        if db.users.find_one({"email": user['email']}):
            return "Email already exists"
            #return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            print("signup success")
            return redirect('/logged') #self.start_session(user)

        return "Signup failed"

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
            print("login success")
            return redirect('/logged')  # self.start_session(user)

        return "Invalid login credentials" #jsonify({"error": "Invalid login credentials"}), 401


@app.route('/')
def login_home():
    print("Login service home")
    print("Press 1 to sign up")
    print("Press 2 to log in")
    num = int(input(""))
    if num == 1:
        return redirect('/signup')
    elif num == 2:
        return redirect('/login')

    return 

@app.route('/logged')
def logged():
    print("You are logged in, press 1 to sign out")
    num = int(input(""))
    if num == 1:
        return redirect('/signout')
        
    return

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return User().signup()


@app.route('/signout')
def signout():
    return User().signout()


@app.route('/login', methods=['POST', 'GET'])
def login():
    return User().login()


app.run(port=5003)
