from extensions import db
import logging

class Data(db.Model):  
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    licence_plate = db.Column(db.String(10), unique=False, nullable=False, index=True)
    car_color = db.Column(db.String(50), nullable=False)


    @property
    def data(self):
        """Return user data as a dictionary."""
        return {
            'id': self.id,
            'licence_plate': self.licence_plate,
            'car_color': self.created_at,
        }

    def save(self):
        """Save the data to the database."""
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error saving data {self.id}: {str(e)}")  # Include exception details
            raise e

    def __repr__(self):
        return f'<User {self.id}>'
