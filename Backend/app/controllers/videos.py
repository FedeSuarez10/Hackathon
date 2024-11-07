import os
from flask import request, current_app, jsonify
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    """Vérifie si l'extension du fichier est autorisée."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload():
    """Logique pour télécharger une vidéo et l'enregistrer en local."""
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400      
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400 
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) 
        save_path = os.path.join(current_app.config['UPLOAD_FILES_FOLDER'], filename)  
        file.save(save_path) 
        
        return jsonify({"message": "File successfully uploaded"}), 201 
    else:
        return jsonify({"message": "File not allowed"}), 400  



# --------------------CRUD-------------------------------

# --------------------SPE_DU_CHEF------------------------

