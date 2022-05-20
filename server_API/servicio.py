from flask import Flask
import controlador

app = Flask(__name__)

@app.route("/")
def home():
    return controlador.home()

@app.route("/admin/<prompt>")
def admin(prompt):
    return controlador.admin(prompt)

@app.route("/search/<query>")
def search(query):
    return controlador.search(query)

app.run(port=5000)