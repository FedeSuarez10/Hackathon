from flask import flash, redirect, request, jsonify, send_from_directory
from extensions import db
import os  



# --------------------CRUD-------------------------------

# --------------------SPE_DU_CHEF------------------------
import os
from flask import request, flash, redirect, url_for, current_app
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    """Vérifie si l'extension du fichier est autorisée."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload():
    """Logique pour le téléchargement d'une vidéo."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        file.save(save_path)
        
        flash('File successfully uploaded')
        return {"message": "File successfully uploaded"}, 201
    else:
        flash('File not allowed')
        return {"message": "File not allowed"}, 400
