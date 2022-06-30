from flask import Flask
import controlador
from flask_wtf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/<prompt>")
def main(prompt):
    return controlador.main(prompt)

app.run(port=5001, debug=True)