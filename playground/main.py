from pickle import TRUE
from pydoc import render_doc
from flask import Flask, jsonify, redirect, render_template, request, session
import requests

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = b'\xcb\x1a\xa9P\xddF\xc5\xb7\xa8\xe3\x01\xad'

@app.route("/")
def home():
    resp = None
    try:
        resp = requests.get(url="http://127.0.0.1:5000/")
        print(resp.text)
        return render_template("main_service.html")
    except:
        return render_template("main_fail.html")

@app.route("/login", methods=["POST"])
def login():
    creds = request.get_json()
    req = requests.post(url="http://127.0.0.1:5000/login", data={"email": creds["email"], "password": creds["pass"]})
    print(req.text)
    if req.text != "Login success":
        return jsonify({"status":-1})
    session["email"] = creds["email"]
    return jsonify({"status":1})

@app.route("/logout")
def logout():
    for ids in list(session.keys()):
        session.pop(ids)
    return redirect("/")

@app.route("/token", methods=["POST"])
def token():
    if not session.get("email"):
        return jsonify({"status": -2})
    creds = request.get_json()["token"]
    if len(creds) < 5:
        return jsonify({"status": -1})
    session["token"] = creds
    return jsonify({"status": 1})

@app.route("/buscar", methods=["POST"])
def buscar():
    busqueda = request.get_json()["query"]
    print(busqueda)
    try:
        resp = requests.get(url="http://127.0.0.1:5000/search/"+busqueda, headers = {"jwt_token": session["token"], "email": session["email"]})
    except:
        return jsonify({"status": -1})
    print(resp.text)
    return jsonify({"status": 1, "contenido": resp.text})


app.run(port=5005, debug=True)