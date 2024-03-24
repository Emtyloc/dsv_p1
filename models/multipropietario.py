from utils.db import db


class Multipropietario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comuna_id = db.Column(db.Integer, db.ForeignKey("comuna.id"))
    manzana = db.Column(db.Integer, nullable=False)
    predio = db.Column(db.Integer, nullable=False)
    propietario = db.Column(db.String(100), nullable=False)
    derecho_porcentual = db.Column(db.Float, nullable=False)
    año_inscripcion = db.Column(db.Integer, nullable=False)
    numero_inscripcion = db.Column(db.Integer, nullable=False)
    fecha_inscripcion = db.Column(db.DateTime)
    año_vigencia_inicial = db.Column(db.Integer, nullable=False)
    año_vigencia_final = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        comuna_id,
        manzana,
        predio,
        propietario,
        derecho_porcentual,
        año_inscripcion,
        numero_inscripcion,
        fecha_inscripcion,
        año_vigencia_inicial,
        año_vigencia_final,
    ):
        self.comuna_id = comuna_id
        self.manzana = manzana
        self.predio = predio
        self.propietario = propietario
        self.derecho_porcentual = derecho_porcentual
        self.año_inscripcion = año_inscripcion
        self.numero_inscripcion = numero_inscripcion
        self.fecha_inscripcion = fecha_inscripcion
        self.año_vigencia_inicial = año_vigencia_inicial
        self.año_vigencia_final = año_vigencia_final
