from utils.db import db
from enum import Enum


class RolActuadorEnum(str, Enum):
    ENAJENANTE = "enajenante"
    ADQUIRIENTE = "adquiriente"


class Actuador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formulario_id = db.Column(db.Integer, db.ForeignKey("formulario.id"))
    run_rut = db.Column(db.String(12))
    derecho_porcentual = db.Column(db.Float)
    rol_actuador = db.Column(db.String(20), nullable=False)

    def __init__(self, formulario_id, run_rut, rol_actuador: RolActuadorEnum):
        self.formulario_id = formulario_id
        self.run_rut = run_rut
        self.rol_actuador = rol_actuador.value

    __table_args__ = (
        db.CheckConstraint(
            'rol_actuador IN ("enajenante", "adquiriente")', name="check_rol_values"
        ),
    )
