from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer CORS
import os

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "Aucun fichier vidéo fourni"}), 400

    video = request.files['video']
    
    if video.filename == '':
        return jsonify({"error": "Nom de fichier vide"}), 400

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)
    
    return jsonify({"message": "Vidéo sauvegardée avec succès", "path": video_path}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
