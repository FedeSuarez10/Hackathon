from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer CORS
import os
from redis import Redis
from rq import Queue
from video_processor import process_video  # Importer la fonction de traitement de la vidéo
import uuid

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuration de Redis et RQ
redis_conn = Redis()
queue = Queue(connection=redis_conn)

# Dictionnaire pour stocker le statut des tâches
task_status = {}

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "Aucun fichier vidéo fourni"}), 400

    video = request.files['video']
    
    if video.filename == '':
        return jsonify({"error": "Nom de fichier vide"}), 400

    # Enregistrer la vidéo sur le disque
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(video_path)

    # Ajouter la tâche à la file d'attente pour le traitement de la vidéo
    job = queue.enqueue(process_video, video_path)
    task_status[job.id] = "Processing"

    return jsonify({"message": "Vidéo en cours de traitement", "task_id": job.id}), 200

@app.route('/status/<task_id>', methods=['GET'])
def get_status(task_id):
    status = task_status.get(task_id, "Unknown Task ID")
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)