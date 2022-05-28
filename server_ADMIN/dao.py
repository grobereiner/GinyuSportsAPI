""" class Resultados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db)
    team_one = db.Column(db.String(50))
    team_two = db.Column(db.String(50))
    resultado = db.Column(db.String(50))
    pass """