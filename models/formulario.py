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
    es_valido = db.Column(db.Boolean)

    actuadores = db.relationship("Actuador", backref="formulario", lazy=True)

    def __init__(
        self,
        cne_id,
        comuna_id,
        manzana,
        predio,
        foja,
        numero_inscripcion,
        fecha_inscripcion,
        es_valido,
    ):
        self.cne_id = cne_id
        self.comuna_id = comuna_id
        self.manzana = manzana
        self.predio = predio
        self.foja = foja
        self.numero_inscripcion = numero_inscripcion
        self.fecha_inscripcion = fecha_inscripcion
        self.es_valido = es_valido
