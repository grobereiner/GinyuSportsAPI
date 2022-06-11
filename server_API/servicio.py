from flask import Flask, redirect, request, session
import controlador
from user import User
from functools import wraps

app = Flask(__name__)
app.secret_key = b'\xcb\x1a\xa9P\xddF\xc5\xb7\xa8\xe3\x01\xad'


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return "Debe estar loggeado para acceder a esta función"

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
    return User().signup(request.form["email"], request.form["password"])

@app.route('/login', methods=['POST', 'GET'])
def login():
    return User().login(request.form["email"], request.form["password"])

@app.route('/signout')
def signout():
    return User().signout()



@app.route("/admin/<prompt>")
@login_required
def admin(prompt):
    return controlador.admin(prompt)

@app.route("/search/<query>")
@login_required
def search(query):
    return controlador.search(query)

app.run(port=5000, debug=True)