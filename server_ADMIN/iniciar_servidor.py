from flask import Flask
import controlador

app = Flask(__name__)


@app.route("/<prompt>")
def main(prompt):
    return controlador.main(prompt)

app.run(port=5001, debug=True)