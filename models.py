from mydb import db

class App(db.Model):
    nom = db.Column(db.String(50))
    niveau = db.Column(db.Integer(), nullable=True)
    etat = db.Column(db.String(30))