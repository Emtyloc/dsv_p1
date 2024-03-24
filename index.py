from app import app
from utils.db import db

from models.contact import Contact
from models.formulario import Formulario
from models.cne import CNE
from models.comuna import Comuna
from models.actuador import Actuador
from models.multipropietario import Multipropietario

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

