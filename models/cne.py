from utils.db import db


class CNE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    formularios = db.relationship("Formulario", backref="cne", lazy=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name
