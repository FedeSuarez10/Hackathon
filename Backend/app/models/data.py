from extensions import db
import logging

class Data(db.Model):
    __tablename__ = 'data' 

    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    

    @property
    def data(self):
        """Return file data as a dictionary."""
        return {
            'id': self.id,
            'license_plate': self.license_plate,
        }

    def save(self):
        """Save the data entry to the database."""
        db.session.add(self)
        try:
            db.session.commit()
            return self 
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error saving file for target {self.id}: {str(e)}")
            raise e

    def __repr__(self):
        return f'<Files for target {self.id}>'
