from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Aktualita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulek = db.Column(db.String(255), nullable=False)
    obsah = db.Column(db.Text, nullable=False)
    datum_publikace = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Aktualita {self.titulek}>'

class Dokument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.String(255), nullable=False)
    popis = db.Column(db.Text)
    cesta_k_souboru = db.Column(db.String(255), nullable=False)
    datum_nahrani = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Dokument {self.nazev}>'

class Obrazek(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    popis = db.Column(db.Text)
    cesta_k_souboru = db.Column(db.String(255), nullable=False)
    datum_nahrani = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Obrazek {self.id}>'
