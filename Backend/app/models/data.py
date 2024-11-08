from extensions import db
import logging

class Data(db.Model):  
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    rang = db.Column(db.Integer, unique=False)
    marque = db.Column(db.String(255), nullable=False)
    modele = db.Column(db.String(255), nullable=False)
    plaque = db.Column(db.String(10), unique=True, nullable=False, index=True)
    coleur = db.Column(db.String(50), nullable=False)
    heure = db.Column(db.String(50), nullable=False)
    tranche_horaire = db.Column(db.String(50), nullable=False)

    


    @property
    def data(self):
        """Return user data as a dictionary."""
        return {
            'id': self.id,
            'rang': self.rang,
            'marque': self.marque,
            'modele': self.modele,
            'plaque': self.plaque,
            'couleur': self.coleur,
            'heure': self.heure,
            'tranche_horaire': self.tranche_horaire,
        }

    def save(self):
        """Save the data to the database."""
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error saving Data {self.id}: {str(e)}")  
            raise e

    def __repr__(self):
        return f'<Data {self.id}>'
