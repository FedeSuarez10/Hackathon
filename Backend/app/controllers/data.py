import os
from flask import request, jsonify
from extensions import db
from app.models.data import Data
import logging


# --------------------CRUD-------------------------------
def create_data():
    data = request.json
    
    if data is None:
        return jsonify({'error': 'Missing data'}), 400
    
    existing_data = Data.query.filter_by(plaque=data['plaque']).first()
    
    if existing_data:
        return jsonify({'error': 'Data with this plaque already exists'}), 400

    try:
        new_data = Data(
            rang=data['rang'],
            marque=data['marque'],
            modele=data['modele'],
            plaque=data['plaque'],
            coleur=data['coleur'],
            heure=data['heure'],
            tranche_horaire=data['tranche_horaire']         
        )
        
        new_data.save()
        return jsonify(new_data.data), 201 
    
    except Exception as e:
        db.session.rollback()  
        logging.error(f"Error creating data: {str(e)}")
        return jsonify({'error': 'Could not create Data'}), 500
    


def read_data():
    datas = Data.query.all()
    return jsonify([data.data for data in datas]), 200

# --------------------SPE_DU_CHEF------------------------

def delete_all_data():
    try:
        Data.query.delete()
        db.session.commit()
        return jsonify({'message': 'All data deleted'}), 200
    except Exception as e:
        db.session.rollback()  
        logging.error(f"Error deleting all data: {str(e)}")
        return jsonify({'error': 'Could not delete all data'}), 500