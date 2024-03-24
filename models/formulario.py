from utils.db import db


class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cne_id = db.Column(db.Integer, db.ForeignKey("CNE.id"))
    comuna_id = db.Column(db.Integer, db.ForeignKey("comuna.id"))
    manzana = db.Column(db.Integer)
    predio = db.Column(db.Integer)
    foja = db.Column(db.Integer)
    numero_inscripcion = db.Column(db.Integer)
    fecha_inscripcion = db.Column(db.DateTime)

    def __init__(self, id, cne_id, comuna_id, fecha_inscripcion):
        self.id = id
        self.cne_id = cne_id
        self.comuna_id = comuna_id
        self.fecha_inscripcion = fecha_inscripcion
