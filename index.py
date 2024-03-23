from app import app
from utils.db import db

from models.contact import Contact
from models.cne import CNE  
from models.comuna import Comuna

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
