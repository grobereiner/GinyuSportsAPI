from flask import Flask, request
import controlador
from user import User, db
from functools import wraps
import jwt

app = Flask(__name__)
app.secret_key = b'\xcb\x1a\xa9P\xddF\xc5\xb7\xa8\xe3\x01\xad'


def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        email = request.headers["email"]

        if "jwt_token" in request.headers:
            token = request.headers["jwt_token"]
        else: 
            return "Ingrese un token"

        try:
            decoded_token = jwt.decode(token, app.secret_key, algorithms="HS256")
        except: 
            return "Token inválido, haga sign out y genere uno nuevo"

        if db.users.find_one({"email": decoded_token["user"]})["email"] == email:
            return f(*args, **kwargs)
        return "Token inválido, no hay match con la base de datos. Haga sign out"

    return wrap

@app.route("/")
def home():
    return controlador.home()

"""
@app.route('/validation')
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
"""

"""
@app.route('/logged')
def logged():
    print("You are logged in, press 2 to sign out")
    num = int(input(""))
    if num == 1:
        return redirect('/signout')
    return
"""

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return User().signup(request.form["email"], request.form["password"], app.secret_key)

@app.route('/login', methods=['POST', 'GET'])
def login():
    return User().login(request.form["email"], request.form["password"], app.secret_key)

@app.route('/signout')
def signout():
    return User().signout()



@app.route("/admin/<prompt>")
@token_required
def admin(prompt):
    return controlador.admin(prompt)

@app.route("/search/<query>")
@token_required
def search(query):
    return controlador.search(query)

app.run(port=5000, debug=True)