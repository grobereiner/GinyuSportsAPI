from flask import Flask
import controlador

app = Flask(__name__)

@app.route("/<query>")
def main(query):
    return controlador.main(query)

app.run(port=5002, debug=True)