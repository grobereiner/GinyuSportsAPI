from flask import Flask
import controlador
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://Grove:root@localhost:5432/ginyu"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Resultados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    team_one = db.Column(db.String(50))
    team_two = db.Column(db.String(50))
    resultado = db.Column(db.String(50))

# db.create_all()

@app.route("/<prompt>")
def main(prompt):
    return controlador.main(prompt)

# app.run(port=5001)